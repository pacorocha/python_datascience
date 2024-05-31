import cv2
import matplotlib.pyplot as plt

def main():
    try:
        # Load the image
        image_path = 'animal.jpeg'
        image = cv2.imread(image_path)

        if image is None:
            raise FileNotFoundError(f"Image at path '{image_path}' not found.")

        # Get the shape of the image
        shape = image.shape
        print(f"The shape of the image is: {shape}")

        # Print the pixel content of the image (first 5 rows for brevity)
        print("Pixel content of the image (first 5 rows):")
        print(image[:5])

        # Zoom the image (cropping)
        zoomed_image = image[100:500, 100:500]

        # Get the new shape after slicing
        new_shape = zoomed_image.shape
        print(f"New shape after slicing: {new_shape}")

        # Convert the zoomed image to grayscale
        zoomed_image_gray = cv2.cvtColor(zoomed_image, cv2.COLOR_BGR2GRAY)
        print("Zoomed image pixel content in grayscale (first 5 rows):")
        print(zoomed_image_gray[:5])

        # Display the image with scale
        plt.figure()
        plt.imshow(cv2.cvtColor(zoomed_image_gray, cv2.COLOR_BGR2RGB))
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Zoomed Image')
        plt.show()

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()