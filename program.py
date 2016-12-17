from PIL import Image

def convert_to_bw(image_path):
    image_file = Image.open(image_path)  # Open colour image
    bw_image_file = image_file.convert('L')  # Convert image to black and white
    bw_image_file.save('bw'+image_file.filename)  # Save new image
    image_file.show()
    bw_image_file.show()


def rotate(image_path, degrees):
    image_file = Image.open(image_path)  # Open original image
    rotated_image = image_file.rotate(degrees)  # rotate the image
    rotated_image.save('rotated'+image_file.filename)  # save new image
    image_file.show()
    rotated_image.show()

