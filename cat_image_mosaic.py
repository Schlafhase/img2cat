#Look at https://github.com/Schlafhase/img2cat/wiki for explanation how to use the function



import cv2
import numpy as np
from PIL import Image
import glob
from scipy import spatial
from random import randint
import os

def read_image(source: str) -> np.ndarray:

    with Image.open(source) as im:
        im_arr = np.asarray(im)
        #im_arr = im_arr[..., ::-1]
    return im_arr

def create_img_array(images_filepath, img_size, logs=False):
    if logs: print("Loading images")
    images = []
    for file in os.listdir(images_filepath):
        if file.endswith(".png"):
            images.append(cv2.resize(read_image(f"{images_filepath}/{file}"), (img_size, img_size)))

    if logs: print(f"Found {len(images)} images")

    images_array = np.asarray(images)
    return (images_array, images)

def create_mosaic(img: np.ndarray, images_tuple, resolution=10, cat_size=100, accuracy=40, saveto="output.png", logs=False):
    if logs: print("Starting...")
    pixelated_img = img[::resolution,::resolution]
    images_array = images_tuple[0]
    images = images_tuple[1]

    #print(images_array.shape)
    #print(images_array[0])
    image_values = np.apply_over_axes(np.mean, images_array, [1,2]).reshape(len(images),3)
    if logs: print("Assigned color values to all images")
    tree = spatial.KDTree(image_values)
    if logs: print("Created Tree")
    target_res = pixelated_img.shape
    image_idx = np.zeros(target_res, dtype=np.uint32)

    for i in range(target_res[0]):
        for j in range(target_res[1]):

            template = pixelated_img[i, j]
            if accuracy > len(images_array): accuracy=len(images)

            match = tree.query(template, k=accuracy)
            pick = randint(0, accuracy-1)
            image_idx[i, j] = match[1][pick]
    if logs: print("Chose images")

    canvas = Image.new("RGB", (cat_size*target_res[1], cat_size*target_res[0]-1))

    #print(target_res[0], target_res[1])
    for i in range(target_res[1]):
        for j in range(target_res[0]):
            #print(image_idx[j, i])
            arr = images[image_idx[j, i][0]]
            x, y = i*cat_size, j*cat_size
            im = Image.fromarray(arr)
            canvas.paste(im, (x,y))
    
    canvas_array = np.asarray(canvas)
    canvas_array = canvas_array[..., ::-1]
    cv2.imwrite(saveto, canvas_array)
    #canvas.save(saveto)

    if logs: print("Done")

