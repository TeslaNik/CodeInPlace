"""
File: decode_image.py

My Final Project: Hiding an image in another image
Decoding part
"""

from simpleimage import SimpleImage
# input files
ENCODED_IMAGE = "encoded_image.png"

# output files
HIDDEN_IMAGE = "hidden_image.png"


def main():
    # Retrieve hidden image from encoded image
    secret_image = SimpleImage(ENCODED_IMAGE)
    decoded_image = decode(secret_image)
    decoded_image.pil_image.save(HIDDEN_IMAGE)


def decode(image):
    print("Decoding...")
    bin_str = []
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            bin_str.append(search_pixel(pixel))
    final_width = bin_to_asc(bin_str[0])
    final_height = bin_to_asc(bin_str[1])
    final = SimpleImage.blank(final_width, final_height)
    i = 2
    for y in range(final.height):
        for x in range(final_width):
            if i < len(bin_str):
                pixel = final.get_pixel(x, y)
                pixel = retrieve_pixel(pixel, bin_str[i])
                final.set_pixel(x, y, pixel)
                i += 1
            else:
                print("\nImage successfully retrieved!")
                print("\nHidden image size:" + str(final_width) + "x" + str(final_height) + " px")
                print("File saved as: " + HIDDEN_IMAGE + str("\n"))
                return final
    print("\nImage successfully retrieved!")
    print("\nImage size:" + str(final_width) + "x" + str(final_height) + " px")
    print("File saved as: " + HIDDEN_IMAGE + str("\n"))
    return final


def retrieve_pixel(pixel, binary_string):
    values = [pixel.red, pixel.green, pixel.blue]
    bin_values = [asc_to_bin(n) for n in values]
    for j in range(3):
        bin_values[j] = binary_string[(3 * j): (3 * j + 3)] + "00000"  # bin_values[j][3:]
        values[j] = bin_to_asc(bin_values[j])
    pixel.red, pixel.green, pixel.blue = values[0], values[1], values[2]
    return pixel


def search_pixel(pixel):
    values = [pixel.red, pixel.green, pixel.blue]
    bin_values = [asc_to_bin(n) for n in values]
    string = "".join([bin_values[0][-3:], bin_values[1][-3:], bin_values[2][-3:]])
    return string


def encode(image, hidden_image):
    bin_str = image_to_bin(hidden_image)
    i = 0
    for y in range(image.height):
        for x in range(0, (image.width - 3), 3):  # assumes image is of width >= 3 pixels
            if i < len(bin_str):
                pixel = image.get_pixel(x, y)
                pixel = update_pixel(pixel, bin_str[i])
                image.set_pixel(x, y, pixel)
                i += 1
            else:
                return image
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
