from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
import numpy as np
import csv
model=VGG16(weights='imagenet')
# model.summary()

with open("Features.csv","a") as csvfile:
	writer=csv.writer(csvfile)
	for num in range(7010,7510):
		count=0
		if(num==7067 or num==7101 or num==7255 or num==7260 or num==7453):
			continue
		while count<=270:
			if((count==0 or count==54 or count==108 or count==162 or count==216)):
				img_name="frame"+str(num)+"%d.jpg" % count
				img_path = "./frames1/frame"+str(num)+"%d.jpg" % count
				img = image.load_img(img_path, target_size=(224,224))
				img_data = image.img_to_array(img)
				img_data = np.expand_dims(img_data, axis=0)
				img_data = preprocess_input(img_data)

				vgg_feature = model.predict(img_data)
				model_extract=Model(input=model.input,output=model.get_layer('fc2').output)
				fc2_features=model_extract.predict(img_data)
				print(fc2_features.shape)
				writer.writerow([img_name,str(fc2_features.tolist())])
			count+=1
csvfile.close()