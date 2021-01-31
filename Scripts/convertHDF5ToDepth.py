import h5py
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image

images, labels = [], []

# Open the HDF5 file
file = h5py.File("mychair.off.h5", "r+")

print(file)
images = np.array(file["/tensor"])

print(len(images))

for i in range(0,100,20):
    image = images[i]

    image = image / np.max(image) * 255.0

    plt.imshow(image)
    plt.show()

    img = Image.fromarray(image)
    img = img.convert("L")
    img.save("image_" + str(i) + ".png")