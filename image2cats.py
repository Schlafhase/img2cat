import cv2
import skimage
import numpy as np
import os


#nd_arr structure: [[img, img, img]]

def concat_vh(nd_arr):
    return cv2.vconcat([cv2.hconcat(list_h) # structure: [img, img, img]
                        for list_h in nd_arr])

def to_cat(img, cat_images, window_size=100):
    heigth = img.shape[0]
    width = img.shape[1]
    y_tiles = heigth//window_size
    x_tiles = width//window_size
    windows = []
    #print(heigth, width)

    for x in range(heigth//window_size):

        for y in range(width//window_size):
            windows.append(img[x*window_size:(x+1)*window_size, y*window_size:(y+1)*window_size])
            cv2.imwrite(f"./debug/windows/{x}-{y}.png", windows[-1])

    
    out = []

    for i, window in enumerate(windows):
        most_similar_image = None
        highest_similarity = 0.0

        for filename in os.listdir(cat_images):
            cat_img = cv2.imread(f"{cat_images}/{filename}")
            cat_img = cv2.resize(cat_img, (window_size, window_size))
            #print(cat_img.shape, window.shape)
            similarity = skimage.metrics.structural_similarity(cat_img, window, channel_axis=-1)

            if similarity > highest_similarity:
                highest_similarity = similarity
                most_similar_image = cat_img

        out.append(most_similar_image)

    img_arr = []
    for i in range(y_tiles):
        img_arr.append(out[i*x_tiles:(i+1)*x_tiles])
        #print(i*14, (i+1)*14)
    #print(type(img_arr[0][0]))
    output = concat_vh(img_arr)
    #print(output[0].shape, output[1].shape)
    # cv2.imshow("Rows", output[0])
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    return output
