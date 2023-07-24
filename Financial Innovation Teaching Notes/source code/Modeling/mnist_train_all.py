from sklearn.metrics import confusion_matrix
import keras
from keras.layers import LSTM
from keras.layers import Dense, Activation, Conv2D, MaxPool2D, Dropout, Flatten
from keras.datasets import mnist
from keras.models import Sequential
from keras.optimizers import Adam


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

def cnn_preprocess(x_train, x_test, y_train, y_test):
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    y_train = keras.utils.to_categorical(y_train, 10)
    y_test = keras.utils.to_categorical(y_test, 10)
    return (x_train, x_test, y_train, y_test)

def lstm_model(n_input, n_step, n_hidden, n_classes):
    model = Sequential()
    model.add(LSTM(n_hidden, batch_input_shape=(None, n_step, n_input), unroll=True))
    model.add(Dense(n_classes))
    model.add(Activation('softmax'))
    return model

def cnn_model():
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=(5,5), padding='same', activation='relu', input_shape=(28, 28, 1)))
    model.add(MaxPool2D(strides=2))
    model.add(Conv2D(filters=48, kernel_size=(5,5), padding='valid', activation='relu'))
    model.add(MaxPool2D(strides=2))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(84, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    return model

def trainning(model, x_train, y_train, x_test, y_test, 
              learning_rate, training_iters, batch_size):
    adam = Adam(lr=learning_rate)
    model.summary()
    model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train,
              batch_size=batch_size, epochs=training_iters,
              verbose=1, validation_data=(x_test, y_test))

def print_confusion_result(x_train, x_test, y_train, y_test, model):
    # get train & test predictions
    train_pred = model.predict_classes(x_train)
    test_pred = model.predict_classes(x_test)
    
    # get train & test true labels
    train_label = y_train
    test_label =  y_test
    
    # confusion matrix
    train_result_cm = confusion_matrix(train_label, train_pred, labels=range(10))
    test_result_cm = confusion_matrix(test_label, test_pred, labels=range(10))
    print(train_result_cm, '\n'*2, test_result_cm)

def mnist_lstm_main():
    # training parameters
    learning_rate = 0.001
    training_iters = 1
    batch_size = 128

    # model parameters
    n_input = 28
    n_step = 28
    n_hidden = 256
    n_classes = 10

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test, y_train_o, y_test_o = lstm_preprocess(x_train, x_test, y_train, y_test, n_step, n_input, n_classes)

    model = lstm_model(n_input, n_step, n_hidden, n_classes)
    trainning(model, x_train, y_train_o, x_test, y_test_o, learning_rate, training_iters, batch_size)
    scores = model.evaluate(x_test, y_test_o, verbose=0)
    print('LSTM test accuracy:', scores[1])
    print_confusion_result(x_train, x_test, y_train, y_test, model)

def mnist_cnn_main():
    # training parameters
    learning_rate = 0.001
    training_iters = 1
    batch_size = 64

    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test, y_train_o, y_test_o = cnn_preprocess(x_train, x_test, y_train, y_test)

    model = cnn_model()
    trainning(model, x_train, y_train_o, x_test, y_test_o, learning_rate, training_iters, batch_size)
    scores = model.evaluate(x_test, y_test_o, verbose=0)
    print('CNN' test accuracy:', scores[1])
    print_confusion_result(x_train, x_test, y_train, y_test, model)


if __name__ == '__main__':
    mnist_lstm_main()
    
    mnist_cnn_main()