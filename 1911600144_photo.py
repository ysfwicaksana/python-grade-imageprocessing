# install python3-tk di PC supaya muncul dialog box
# install Pillow (PIL: Python Image Library)
# import matplotlib
# saran : pakai virtualenv
from matplotlib import image
from matplotlib import pyplot

# import foto
image = image.imread('yusuf.png')
newImage = image * [1, 0.95, 0.9]

#plotting image di pyplot
pyplot.subplot(1,2,1)
pyplot.imshow(image)

pyplot.subplot(1,2,2)
pyplot.imshow(newImage)
pyplot.show()