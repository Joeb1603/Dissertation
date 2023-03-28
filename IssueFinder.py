import os
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import natsort
import shutil

# Set the directory path
#annotations_path = os.path.join(os.getcwd(),'labels')
#images_path = os.path.join(os.getcwd(),'images')
annotations_path = 'E:\\Dissertation\\dataset\\labels'
images_path = 'E:\\Dissertation\\dataset\\images'



# Create a dictionary to store the count for each class
class_counts = {}

annotations = os.listdir(annotations_path)
images = os.listdir(images_path)

print(f"\n{len(annotations)}=={len(images)}?\n")

if len(annotations)==len(images):
    print("No issues\n")
else:

    images = natsort.natsorted(images)
    #print(images[0])
    items = [-1]
    for thing2 in images:
        thing = thing2.split('.')[0]
        if int(thing)!=int(items[-1])+1:
            print(f"{thing} not {items[-1]+1}")
            items_to_delete = []
            current_num = int(items[-1]+1)
            while current_num<int(thing):
                items_to_delete.append(current_num)
                current_num+=1
            print(f"Items to be deleted: {' '.join(str(x) for x in items_to_delete)}\n")
            for item in items_to_delete:
                try:
                    os.remove(os.path.join(annotations_path, f'{item}.txt'))
                except FileNotFoundError:
                    print(f"File: {os.path.join(annotations_path, f'{item}.txt')} not found, can not delete\n")

        items.append(int(thing))
    print("\n")