"""
File: decode_text.py
Text used: http://shakespeare.mit.edu/julius_caesar/index.html
My Final Project: Hiding text in an image
Decoding part
"""

from simpleimage import SimpleImage
# input files
ENCODED_IMAGE = "encoded_text.png"

# output files
HIDDEN_TEXT = "hidden_text.txt"


def main():
    encoded_image = SimpleImage(ENCODED_IMAGE)
    hidden_text = decode(encoded_image)
    write_txt(hidden_text, HIDDEN_TEXT)


def write_txt(text, filename):
    f = open(filename, "w+")
    f.write(text)
    f.close()


def decode(image):
    string = ''
    for y in range(image.height):
        for x in range(0, (image.width - 3), 3):
            pixels = [image.get_pixel(x, y), image.get_pixel(x + 1, y), image.get_pixel(x + 2, y)]
            values = [pixels[0].red, pixels[0].green, pixels[0].blue, pixels[1].red, pixels[1].green, pixels[1].blue,
                      pixels[2].red, pixels[2].green]
            bin_comp = [asc_to_bin(n) for n in values]
            bin_string = "".join([b[-1] for b in bin_comp])
            if bin_string == '11111111':
                print("\nSuccessfully retrieved text!")
                print("\nNo. of text characters: ", len(string))
                print("File saved as: " + HIDDEN_TEXT + "\n")
                return string
            else:
                string = string + bin_to_str(bin_string)
    print("\nNo. of text characters: ", len(string))
    print("File saved as: " + HIDDEN_TEXT + "\n")
    return string


def asc_to_bin(num):
    return format(num, '08b')


def bin_to_str(binary):
    num = bin_to_asc(binary)
    string = asc_to_str(num)
    return string


def bin_to_asc(binary):
    return int(binary, 2)


def asc_to_str(num):
    return chr(num)


if __name__ == "__main__":
    main()
