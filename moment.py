import numpy as np
from PIL import Image
import glob
import matplotlib.pyplot as plt

img_size = 500
bar_width = 50

coord = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

files = glob.glob('icloudphoto/*')
for i in range(9):
	comb = np.ones((img_size*3+bar_width*2,)*2+(3,),np.uint8)*255
	for j,file in enumerate(files[i*9:i*9+9]):
		a,b=coord[j]
		a=a*img_size+a*bar_width
		b=b*img_size+b*bar_width
		img = np.array(Image.open(file))
		img = Image.fromarray(img[:,504:-504,:])
		img = img.resize((img_size, img_size), resample=Image.LANCZOS)
		comb[a:a+img_size,b:b+img_size,:] = np.array(img)
	# plt.imshow(comb)
	# plt.show()
	Image.fromarray(comb).save('%d.png'%i)
