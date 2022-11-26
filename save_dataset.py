from PIL import Image
import os
import numpy as np
from sklearn.metrics import label_ranking_average_precision_score

def one_hot(array):
    unique, inverse = np.unique(array, return_inverse=True)
    onehot = np.eye(unique.shape[0])[inverse]
    return onehot


vectorized_images = []
path_to_files = "./database/"
img_paths = os.listdir(path_to_files)

# loading labels from filenames and onehot encode them
labels = np.array([fname[:-7] for fname in img_paths])
one_hot_labels = one_hot(labels)
#print(labels)

# changing the size of an image   
for _, file in enumerate(img_paths):
    image = np.array(Image.open(path_to_files + file).resize((224, 224)))
    vectorized_images.append(image) 
    
np.savez("./my_database.npz", data=vectorized_images, labels=one_hot_labels)