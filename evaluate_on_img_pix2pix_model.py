from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from numpy import expand_dims
from matplotlib import pyplot

def load_image(filename, size=(256,256)):
    pixels = load_img(filename, target_size=size)
    pixels = img_to_array(pixels)
    pixels = (pixels - 127.5) / 127.5
    pixels = expand_dims(pixels, 0)
    return pixels

src_image = load_image('k.PNG')
print('Loaded', src_image.shape)
model = load_model('model_043840.h5')
gen_image = model.predict(src_image)
gen_image = (gen_image + 1) / 2.0
pyplot.imshow(gen_image[0])
pyplot.axis('off')
pyplot.show()
