import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

num_classes = 5
img_size = 224
#model = tf.keras.applications.efficientnet.EfficientNetB0(weights='imagenet', drop_connect_rate = 0.5)

# load dataset
dataset = np.load('./my_database.npz')
data = dataset["data"]
labels = dataset["labels"]

# split the data into train and validation sets
train_data, val_data, train_labels, val_labels = train_test_split(data, labels, test_size=0.2, random_state=42)

# image augmentation to improve classification
img_augmentation = tf.keras.models.Sequential(
    [
        tf.keras.layers.RandomRotation(factor=0.15),
        tf.keras.layers.RandomTranslation(height_factor=0.1, width_factor=0.1),
        tf.keras.layers.RandomFlip(),
        tf.keras.layers.RandomContrast(factor=0.1),
    ],
    name="img_augmentation",
)

inputs = tf.keras.layers.Input(shape=(img_size, img_size, 3))
x = img_augmentation(inputs)


model = tf.keras.applications.VGG16(
    include_top=False,
    weights="imagenet",
    input_tensor=x,
)

# freeze the pretrained weights
model.trainable = False

# here we initialize the model with pre-trained ImageNet weights, and we fine-tune it on our own dataset.

# rebuild top
x = tf.keras.layers.GlobalAveragePooling2D(name="avg_pool")(model.output)
x = tf.keras.layers.BatchNormalization()(x)

top_dropout_rate = 0.25
x = tf.keras.layers.Dropout(top_dropout_rate, name="top_dropout")(x)
outputs = tf.keras.layers.Dense(num_classes, activation="softmax", name="pred")(x)

# compile
model = tf.keras.Model(inputs, outputs, name="VGG16")
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-2)
model.compile(optimizer=optimizer,
              loss="categorical_crossentropy",
              metrics=["accuracy"])

# train weights in 5 epochs
epochs = 5
model.fit(x=train_data,
          y=train_labels,
          validation_data=(val_data, val_labels),
          epochs=epochs,
          verbose=2)

model.save("./my_model.h5")


# evaluate accuracy of the convolution network and the used model
dataset = np.load("./my_database.npz")
data = dataset["data"]
labels = dataset["labels"]

model = tf.keras.models.load_model('my_model.h5')
model.evaluate(x=data, y=labels)