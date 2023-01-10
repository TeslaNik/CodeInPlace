"""
File: encode_image.py

My Final Project: Hiding an image in another image
Encoding part
"""

from simpleimage import SimpleImage
# input files
ORIGINAL_IMAGE = "original_image.png"
SECRET_IMAGE = "secret_image.png"
# output files
ENCODED_IMAGE = "encoded_image.png"


def main():
    # Load images
    image = SimpleImage(ORIGINAL_IMAGE)
    hidden_image = SimpleImage(SECRET_IMAGE)

    print("\nMax possible pixels to hide in image:" + str(image.width * image.height) + " px")
    print("Number of pixels to be hidden:" + str((hidden_image.width * hidden_image.height)+2) + " px")  # including image dimensions

    if image.width * image.height > ((hidden_image.width * hidden_image.height)+2):
        # Hide one image in another, save encoded image
        encoded_image = encode(image, hidden_image)
        encoded_image.pil_image.save(ENCODED_IMAGE)
        print("File saved as:", ENCODED_IMAGE)
        # image.show()
        # encoded_image.show()
    else:
        print("Cannot hide image due to capacity constraints.")


def encode(image, hidden_image):
    bin_str = image_to_bin(hidden_image)
    i = 0
    for y in range(image.height):
        for x in range(image.width):
            if i < len(bin_str):
                pixel = image.get_pixel(x, y)
                pixel = update_pixel(pixel, bin_str[i])
                image.set_pixel(x, y, pixel)
                i += 1
            else:
                print("\nImage successfully encoded!\n")
                return image
    print("\nImage successfully encoded!\n")
    return image


def image_to_bin(image):
    bin_list = [format(image.width, "09b"), format(image.height, "09b")]  # information about hidden image dimensions
    for pixel in image:
        string = "".join([asc_to_bin(pixel.red)[0:3], asc_to_bin(pixel.green)[0:3], asc_to_bin(pixel.blue)[0:3]])
        bin_list.append(string)
    return bin_list


def update_pixel(pixel, binary_string):
    values = [pixel.red, pixel.green, pixel.blue]
    bin_values = [asc_to_bin(n) for n in values]
    for j in range(3):
        bin_values[j] = bin_values[j][:-3] + binary_string[(3 * j): (3 * j + 3)]
        values[j] = bin_to_asc(bin_values[j])
    pixel.red, pixel.green, pixel.blue = values[0], values[1], values[2]
    return pixel


# For encoding
def str_to_bin(string):
    num_list = [str_to_asc(c) for c in string]
    bin_list = [asc_to_bin(n) for n in num_list]
    return bin_list


def str_to_asc(string):
    return ord(string)


def asc_to_bin(num):
    return format(num, '08b')


# For decoding
def bin_to_str(bin_list):
    num_list = [bin_to_asc(b) for b in bin_list]
    string = "".join([asc_to_str(n) for n in num_list])
    return string


def bin_to_asc(binary):
    return int(binary, 2)


def asc_to_str(num):
    return chr(num)


if __name__ == "__main__":
    main()
