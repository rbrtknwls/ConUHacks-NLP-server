import tensorflow as tf
from tensorflow import keras
image_size = (180, 180)
model = keras.models.load_model("save_at_1.h5")

img = keras.preprocessing.image.load_img(
    "data/ose_Data/Not_Normal/b.jpeg", target_size=image_size
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis

predictions = model.predict(img_array)
score = predictions[0]
print(
    "This image is %.2f percent nose and %.2f percent nose."
    % (100 * (1 - score), 100 * score)
)
