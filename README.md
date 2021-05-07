# Training-for-AI-Engineer

This project is built as a part of Training for AI Engineers at fusemachines. Dataset used in this project is ISEAR dataset. Dataset consist of 7 classes of emotion. It has been used for multi-class classification project. We have implemented BERT and LSTM with Glove embeddings as our classifier.


## Installing the dependencies

1. Create new poetry environment 

        poetry shell

2. Use `poetry` to install the dependencies

        poetry install    

## Running only the project logic

 1.      flask run

## Route for API with front-end
1. ```/``` :            Frontend for making predictions
2. ```/users```:        Retrieve all data from database
3. ```/users/<id>```:   Retrieve single item from database


### The resulting directory structure
------------

The directory structure of our project looks like this: 

```
.
├── data
│   ├── external
│   ├── interim
│   ├── processed
│   └── raw
├── docs
├── LICENSE
├── Makefile
├── models
├── notebooks
├── README.md
├── references
├── reports
│   └── figures
├── requirements.txt 
├── setup.py
├── src
│   ├── data
│   │   └── make_dataset.py
│   ├── features
│   │   └── build_features.py
│   ├── __init__.py
│   ├── models
│   │   ├── predict_model.py
│   │   └── train_model.py
│   └── visualization
│       └── visualize.py
└── tox.ini
```
