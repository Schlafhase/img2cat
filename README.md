# Welcome to the img2cat documentation!

### How to use the Function
The function `create_mosaic` takes 6 arguments:
* img: The Image you want to convert as a numpy array
* images_tuple: A tuple created by giving the `create_img_array` function the filepath of your (cat) images and the size you want them to be
* resolution: How much the input image gets pixelated (Higher values result in a lower quality)
* cat_size: How big one (cat) image should be (Should be the same as in the `create_img_array` function for best results)
* accuracy: Determines how random the images are (When set to 1 or lower gives an error for some reason) (Set to 2 for the most accurate image)
* saveto: The filepath you want to save the result to

# Example:
    import cv2
    import cat_image_mosaic
    
    cats_filepath = "./cat_images"

    cat_images = cat_image_mosaic.create_img_array(images_filepath=cats_filepath, img_size=25)
    im = cv2.imread("input6.png")
    
    cat_image_mosaic.create_mosaic(img=im, images_tuple=cat_images, resolution=75, cat_size=25, accuracy=5, logs=True)

I used a public dataset with 9000 cat images for the example (https://www.kaggle.com/datasets/crawford/cat-dataset)

Input Image:

![input6](https://github.com/Schlafhase/img2cat/assets/106097366/95c5b0d7-d552-4faf-98c1-a012cf740c48)

Output Image:

![image](https://github.com/Schlafhase/img2cat/assets/106097366/f4e6fe9b-e54d-4079-bb29-e2a6f8d564ed)
