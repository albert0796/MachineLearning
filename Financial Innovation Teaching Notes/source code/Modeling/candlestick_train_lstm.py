from sklearn.metrics import confusion_matrix
import pickle
import keras
from keras.layers import LSTM
from keras.layers import Dense, Activation, Conv2D, MaxPool2D, Dropout, Flatten
from keras.datasets import mnist
from keras.models import Sequential
from keras.optimizers import Adam


def load_pkl(pkl_name):
    # load data from data folder
    with open(pkl_name, 'rb') as f:
        data = pickle.load(f)
    return data

def lstm_preprocess(x_train, x_test, y_train, y_test, n_step, n_input, n_classes):
    x_train = x_train.reshape(-1, n_step, n_input)
    x_test = x_test.reshape(-1, n_step, n_input)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    y_train = keras.utils.to_categorical(y_train, n_classes)
    y_test = keras.utils.to_categorical(y_test, n_classes)
    return (x_train, x_test, y_train, y_test)

def lstm_model(n_input, n_step, n_hidden, n_classes):
    model = Sequential()
    model.add(LSTM(n_hidden, batch_input_shape=(None, n_step, n_input), unroll=True))
    model.add(Dense(n_classes))
    model.add(Activation('softmax'))
    return model

def train_lstm(model, x_train, y_train, x_test, y_test, 
        learning_rate, training_iters, batch_size):
    adam = Adam(lr=learning_rate)
    model.summary()
    model.compile(optimizer=adam,
        loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train,
        batch_size=batch_size, epochs=training_iters,
        verbose=1, validation_data=(x_test, y_test))

def print_result(data, x_train, x_test, model):
    # get train & test pred-labels
    train_pred = model.predict_classes(x_train)
    test_pred = model.predict_classes(x_test)
    # get train & test true-labels
    train_label = data['train_label'][:, 0]
    test_label = data['test_label'][:, 0]
    # confusion matrix
    train_result_cm = confusion_matrix(train_label, train_pred, labels=range(9))
    test_result_cm = confusion_matrix(test_label, test_pred, labels=range(9))
    print(train_result_cm, '\n'*2, test_result_cm)

def mnist_lstm_main():
    # training parameters
    learning_rate = 0.001
    training_iters = 10
    batch_size = 128

    # model parameters
    n_input = 40
    n_step = 10
    n_hidden = 256
    n_classes = 10

    data = load_pkl('./data/label8_eurusd_10bar_1500_500_val200_gaf_culr.pkl')
    x_train, y_train, x_test, y_test = data['train_gaf'], data['train_label'][:, 0], data['test_gaf'], data['test_label'][:, 0]
    x_train, x_test, y_train, y_test = lstm_preprocess(x_train, x_test, y_train, y_test, n_step, n_input, n_classes)

    model = lstm_model(n_input, n_step, n_hidden, n_classes)
    train_lstm(model, x_train, y_train, x_test, y_test, learning_rate, 
               training_iters, batch_size)
    scores = model.evaluate(x_test, y_test, verbose=0)
    print('LSTM test accuracy:', scores[1])
    print_result(data, x_train, x_test, model)

if __name__ == '__main__':
    mnist_lstm_main()