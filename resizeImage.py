# Importing Image class from PIL module  
import os
from PIL import Image  

directory = "turtle/" #Directorio donde se encuentran las fotos
saveDirectory = "turtle2/" #Directorio donde se guardan las fotos

for pica in os.listdir(directory):
	# Opens a image in RGB mode
	picaDir = directory + pica
	print(picaDir)
	im = Image.open(picaDir)
	im1 = im
	im1 = im
	newSize = (224,224)
	im1 = im1.resize(newSize)
	im1.save(saveDirectory + pica, "JPEG")

"""
for conjunto in os.listdir(directory):
	conjDir = directory + "/" + conjunto
	#print(conjDir)
	for animal in os.listdir(conjDir):
		animDir = conjDir + "/" + animal
		#print(animDir)
		for pica in os.listdir(animDir):
			# Opens a image in RGB mode
			picaDir = animDir + "/" + pica
			print(picaDir)
			im = Image.open(picaDir)
			im1 = im
			im1 = im
			newSize = (224,224)
			im1 = im1.resize(newSize)
			im1.save(picaDir, "JPEG")
"""