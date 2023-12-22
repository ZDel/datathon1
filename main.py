import csv 
from deepface import DeepFace
import os 

images = 'images/'

with open('results.csv', 'w') as csvfile:
  spamwriter = csv.writer(csvfile, delimiter='|')
  spamwriter.writerow(['Filename', 'Gender', 'Race/ethnicity', 'Age'])
  for image in os.listdir(images):
    try:
      objs = DeepFace.analyze(img_path = os.path.join(images, image), 
            actions = ['age', 'gender', 'race'])
      spamwriter.writerow([image,objs[0]['dominant_gender'] , objs[0]['dominant_race'], objs[0]['age']])
    except:
      spamwriter.writerow([image, 'Unknown', 'Unknown', -1])
      print('error on ' + image)
