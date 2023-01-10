"""
File: encode_text.py
Text used: http://shakespeare.mit.edu/julius_caesar/index.html
My Final Project: Hiding text in an image
Encoding part
"""

from simpleimage import SimpleImage
# input files
ORIGINAL_IMAGE = "original_image.png"
SECRET_TEXT = "julius.txt"
# output files
ENCODED_IMAGE = "encoded_text.png"


def main():
    # Load image, text
    image = SimpleImage(ORIGINAL_IMAGE)
    text = read_txt(SECRET_TEXT)
    print("\nMax possible hidden characters in image: ", (image.width // 3) * image.height)
    print("Actual hidden text characters: ", len(text) + 1)

    if (image.width // 3)*image.height > (len(text) + 1):
        # Hide text in image, save encoded image
        encoded_image = encode(image, text)
        encoded_image.pil_image.save(ENCODED_IMAGE)
        print("File saved as:", ENCODED_IMAGE)
    else:
        print("Cannot hide text due to capacity constraints.")


def encode(image, text):
    bin_str = str_to_bin(text)
    bin_str.append('11111111')  # to signal the end of text
    i = 0
    for y in range(image.height):
        for x in range(0, (image.width - 3), 3):  # assumes image is of width >= 3 pixels
            if i < len(bin_str):
                pixels = [image.get_pixel(x, y), image.get_pixel(x + 1, y), image.get_pixel(x + 2, y)]
                pixels = update_3_pixels(pixels, bin_str[i])
                image.set_pixel(x, y, pixels[0])
                image.set_pixel(x + 1, y, pixels[1])
                image.set_pixel(x + 2, y, pixels[2])
                i += 1
            else:
                print("\nText successfully encoded!\n")
                return image
    print("\nText successfully encoded!\n")
    return image


def write_txt(text, filename):
    f = open(filename, "w+")
    f.write(text)
    f.close()


def update_3_pixels(pixels, binary_string):
    values = [pixels[0].red, pixels[0].green, pixels[0].blue, pixels[1].red, pixels[1].green, pixels[1].blue,
              pixels[2].red, pixels[2].green]
    # Convert pixel values from base 10 to base 2
    bin_values = [asc_to_bin(n) for n in values]
    # Replace LSB value of 8 pixel components with 8 binary values of text character
    for j in range(len(bin_values)):
        bin_values[j] = bin_values[j][:-1] + binary_string[j]
    # Convert back new binary values to base 10
    values = [bin_to_asc(b) for b in bin_values]
    # Assign new pixel values
    pixels[0].red, pixels[0].green, pixels[0].blue = values[0], values[1], values[2]
    pixels[1].red, pixels[1].green, pixels[1].blue = values[3], values[4], values[5]
    pixels[2].red, pixels[2].green = values[6], values[7]
    return pixels


def read_txt(filename):
    with open(filename, 'r') as file:
        text = file.read().rstrip('\n')
    return text


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
