# DeepLearning_nmt
Project repo for deep learning, based on nmt of Tensorflow tutorial.

## Data
Data that used to train our model is available at: https://drive.google.com/open?id=1RIcqkbwe3tVxLFdQefZS9owtNxsRAtwv

## Dependency

1. Python >= 3.5 (please forget Python 2)
2. Tensorflow >= 1.4

## How to use
These three model folders *nmt_model_naive_50w*, , *nmt_attention_model_bahdanau_50w*, *nmt_attention_model_scaled_luong_50w*, *nmt_attention_model_scaled_luong_50w_deeper* in this repo can produce the translations using four models we have trained. Train logs and checkpoints are contained inside each model folder.

You will need to do the following to use the checkpoints and generate translations from English to Chinese:

1. Clone this git repo:
```
git clone https://github.com/Epica-Wang/DeepLearning_nmt_final
```

2. Run the Python code to load the checkpoints and make inference.
  * First please make sure you active tensorflow on your local machine. Please type this command in your terminal:
  ```
  source activate tensorflow
  ```
  * To use naive nmt model, please run:
  ```
  python predict_naive.py
  ```
  Then type English sentence you want to translate. Parameters used for the model and translation will be printed on your screen.

  * To use nmt model with scaled_luong attention mechanism, please run:
  ```
  python predict_scaled_luong.py
  ```

  * To use nmt model with bahdanau attention mechanism, please run:
  ```
  python predict_bahdanau.py
  ```

  * To use nmt model with a deeper version of scaled_luong attention mechanism, first you need to download checkpoints from (since Github does not allow to upload file larger than 1GB):
  ```
  https://drive.google.com/open?id=1qScfa599n0Soak1L3Ja0pjpy2xHHAB-t
  ```
  Then run:
  ```
  python predict_scaled_luong_deeper.py
  ```
