# Explainable AI for Local Search Attack on Candlestick Learner

Cheng-han Wu, Jun-Hao Chen, Samuel Yen-Chi Chen and Yun-Cheng Tsai

## Results
- Successful attacking rate for a model trained by method 1 & 2

#### Method 1: No limitation of perturbation
| Label  | 8th | 9th | 10th(\%) |
| ------------- | ------------- | ------------- | ------------- |
| 1  | 9.7 | 33.8 | 28.4 |
| 2  | 56.1 | 47.0 | 8.4 |
| 3  | 11.5 | 12.0 | 91.5 |
| 4  | 22.7 | 80.6 | 30.3 |
| 5  | 6.1 | 9.6 | 54.5 |
| 6  | 5.5 | 54.3 | 24.1 |
| 7  | 10.3 | 26.7 | 81.3 |
| 8  | 8.1 | 88.1 | 7.8 |

#### Method 2: limitation of perturbation on the Last Three Candlesticks
| Label  | 8th | 9th | 10th(\%) |
| ------------- | ------------- | ------------- | ------------- |
| 1  | 10.8 | 53.9 | 58.7 |
| 2  | 85.0 | 49.1 | 3.7 |
| 3  | 25.5 | 12.7 | 90.4 |
| 4  | 34.8 | 88.1 | 34.5 |
| 5  | 6.1 | 8.4 | 77.2 |
| 6  | 8.1 | 80.6 | 38.9 |
| 7  | 17.1 | 25.0 | 88.3 |
| 8  | 25.9 | 86.4 | 13.6 |

## Data
- label8_eurusd_10bar_1500_500_val200_gaf_culr.pkl

## Usages
#### 1. Environment
- cd (path of the file folder)
- pip install -r requirements.txt 

#### 2. Carry out training aid augmented generator, re-training of GAF-CNN and modified local search attack method
- python main.py

## References
1. Foolbox open-source (<https://github.com/bethgelab/foolbox>)
