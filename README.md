# AI & Machine Learning Fundamentals

Repository show the sample and easy structure to construct the image classification pipeline in pytorch.

Train.py function is the one which calls each script: Loads the data using data_retrieval.py, model using example_model.py and utilities by using the utils.py

**Good Luck!**

## Installation

Just run:
```sh
    pip install -r requirements.txt
```

If you are using Python environments,  it is highly recommended to initiate the environment with system-site packages access to use GPU-related technologies without problems (e.g.: CUDA):

```sh
    python3 -m venv env --system-site-packages
```

In the command above, `env` is the name of the environment. You can change it to any name you want.

Then, activate the environment:

- **Linux/macOS**:
```sh
    source env/bin/activate
```

- **Windows**:
```cmd
    env\Scripts\activate
```

## Train the model
To train model, start train file:

```sh
    python3 train.py
```


## TensorBoard
To visualize the training process, run the following command:

```sh
    tensorboard --logdir=runs
```

Then, open the browser and go to `http://localhost:6006/` to see the training process.
