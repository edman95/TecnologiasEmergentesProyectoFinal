import numpy as np
import keras
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
from PIL import Image
import os


directory = 'turtle2/' #Carpeta de origen en la que se encuentran las imagenes
id_base = 1607 #Nombre del último id +1 de las fotos en la carpeta de origen

def save_images(images, id_name):
    #Directorio donde se guardan las fotos
    dir_aug_imgs = 'turtle_augment/'
    for pica in images:
        im = Image.fromarray(pica)
        im.save(dir_aug_imgs + str(id_name) + '.jpg')
        id_name = id_name + 1
        
    return id_name


gen = ImageDataGenerator(rotation_range = 10, width_shift_range=0.1, 
                         height_shift_range = 0.1, shear_range = 0.15,
                        zoom_range=0.1, channel_shift_range = 10,
                        horizontal_flip=True)


# Para hacer data augment de las fotos que ya tengo:
for pica in os.listdir(directory):
    image_path = directory + pica
    image = np.expand_dims(plt.imread(image_path), 0)
    aug_iter = gen.flow(image)
    
    
    #Especificar cuántas se van a generar en el range, en este caso 3
    aug_images = [next(aug_iter)[0].astype(np.uint8) for i in range(3)]
    id_base = save_images(aug_images, id_base)
    