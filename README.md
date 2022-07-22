# RandomModel

![main](https://thumbs.gfycat.com/SeparateFrayedChafer-max-1mb.gif)

This is my neural network model.

## Teammates

- Teammates are: John, Tony, ...
- Contact: xxx@gmail.com

## User Manual

Please use the following code to install.

```
# install this library
!pip install git+https://github.com/yiqiao-yin/RandomModel.git
```

```
import deeplearning.modules
```

Run the function by using the code below

```
test_run_result = simple_neuralnetwork_model(
    x=X_train, 
    y=y_train_onehot,
    hidden = [256, 128, 64, 32, 16],
    output_dim = 10,
    validation_split=0.1,
    loss='mse',
    optimizer='sgd',
    epochs=10,
    verbose=True
)
```

Output is stored in a dictionary

```
# display keys of the dictionary
test_run_result.keys()
```
