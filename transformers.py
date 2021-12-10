from transformers import ViTFeatureExtractor, ViTModel
from PIL import Image
import numpy as np
import json
import os

feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224-in21k')
model = ViTModel.from_pretrained('google/vit-base-patch16-224-in21k')

def encoding(final_path_list):
  a = []
  for path in final_path_list:
    image = Image.open(path)
    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    output_state = outputs.pooler_output
    k = output_state.detach().numpy().reshape([1,768])
    a.append(k)
  return a

def image_concatenate(image_emb_arr):
  k = image_emb_arr[0]
  for j in image_emb_arr[1:]:
    k = np.concatenate((k, j), axis=0)
  return k
folder='/content/gdrive/MyDrive/Capstone'
name_2=folder+'/'+'Frames'
image_name_path = os.listdir(name_2)
path_1 = name_2 + '/' + image_name_path[0]
path_2 = name_2 + '/' + image_name_path[1]
path_3 = name_2 + '/' + image_name_path[2]
path_4 = name_2 + '/' + image_name_path[3]
path_5 = name_2 + '/' + image_name_path[4]
path_6 = name_2 + '/' + image_name_path[5]
path_7 = name_2 + '/' + image_name_path[6]
path_8 = name_2 + '/' + image_name_path[7]
path_9 = name_2 + '/' + image_name_path[8]
path_10 = name_2 + '/' + image_name_path[9]
path_11 = name_2 + '/' + image_name_path[10]
path_12 = name_2 + '/' + image_name_path[11]
path_13 = name_2 + '/' + image_name_path[12]
path_14 = name_2 + '/' + image_name_path[13]
path_15 = name_2 + '/' + image_name_path[14]
final_path_list = []
final_path_list.append(path_1)
final_path_list.append(path_2)
final_path_list.append(path_3)
final_path_list.append(path_4)
final_path_list.append(path_5)
final_path_list.append(path_6)
final_path_list.append(path_7)
final_path_list.append(path_8)
final_path_list.append(path_9)
final_path_list.append(path_10)
final_path_list.append(path_11)
final_path_list.append(path_12)
final_path_list.append(path_13)
final_path_list.append(path_14)
final_path_list.append(path_15)
k = encoding(final_path_list)
j = image_concatenate(k)
j = np.expand_dims(j, axis=0)
data_final= j.tolist()

with open("/content/gdrive/MyDrive/Capstone/dump_file.json", "w") as outfile:
    json.dump(data_final, outfile)
