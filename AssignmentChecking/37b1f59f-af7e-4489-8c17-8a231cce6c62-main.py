import numpy as np
import cv2
import os


def image_to_array():
    try:
        path = r"C:\Users\Hasan\PycharmProjects\practice\photos"

        files = os.listdir(path)

        images_name = []

        count_of_images = 0

        for file in files:
            if file.endswith((".png", ".jpg")):
                count_of_images += 1
                images_name.append(file)

        if count_of_images >= 1:
            images_array = np.zeros([count_of_images, 200, 200, 3])

            for i, image_name in enumerate(images_name):
                image_array = cv2.imread(path + "\\" + image_name, 1)
                height, width, _ = image_array.shape

                if ((height, width) > (200, 200)) or ((height, width) < (200, 200)):
                    image_array = cv2.resize(image_array, (200, 200))
                    images_array[i] = image_array
                else:
                    images_array[i] = image_array
            print(f"{count_of_images} images stored successfully!")
            return images_array
        else:
            print("No images found!")
    except FileNotFoundError as e:
        print(e.strerror)
        print(e.__str__())


def main():
    image_to_array()


if __name__ == '__main__':
    main()
