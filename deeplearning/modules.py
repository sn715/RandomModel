# import
import tensorflow as tf

# create a function
def simple_neuralnetwork_model(
    x=None, 
    y=None,
    hidden = [128, 64, 32],
    output_dim = 10,
    validation_split=0.2,
    loss='mse',
    optimizer='sgd',
    epochs=2,
    verbose=True
):
    # build model
    model = tf.keras.models.Sequential(name="model_sam")

    # flatten
    model.add(tf.keras.layers.Flatten(name="flatten"))

    # hidden
    # things to change:
    # width of each layer: (units/neurons) you can change the number of units!!!
    # depth of the network: you can have any number of Dense layers you like!!!
    # summarize: [128, 64, 32]
    for i in range(len(hidden)):
        model.add(tf.keras.layers.Dense(hidden[i], activation='relu', name='layer'+str(i+1)))

    # output
    model.add(tf.keras.layers.Dense(output_dim, activation='softmax', name='output'))

    # compile
    model.compile(loss=loss, optimizer=optimizer, metrics=['accuracy'])

    # fit
    history = model.fit(x=x, y=y, validation_split=validation_split, epochs=epochs)

    # print summary
    if verbose:
        print(model.summary())

    # output: use dictionary, i.e. {}
    return {
        'model': model,
        'history': history
    }
