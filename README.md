## Code In Place 2021 - Project 

This repository contains the Final Project submission on [Steganography](https://en.wikipedia.org/wiki/Steganography) for [Code in Place](https://codeinplace.stanford.edu/), hosted by Stanford University.
Here is the [link](https://codeinplace-2021.netlify.app/2021/showcase/12) to the presentation.

### Overview

The project focuses on the concept of steganography, which involves hiding data in images. Specifically, we explore the technique of least significant bit (LSB) steganography, where the secret message is concealed in the least significant bits of the pixel RGB components. 
The project also covers the decoding process, which involves extracting the hidden information by reversing the encoding steps.
<img align="center" alt="Coding" width="750" src="https://github.com/TeslaNik/CodeInPlace/blob/main/ppt01.png">
#### Hide text in images

The main idea is that whatever text we have is converted to ASCII and then to 8-bit binary values. Now, we take three pixels, giving us access to nine least significant bits. Leaving one out, we fill the eight-bit binary value of the text inside the least significant bits. As we see, the change in the pixel color is barely visible.

To decode, we again take three pixels and extract the eight least significant bits, converting them back to ASCII and then text. 

<img align="center" alt="Coding" width="750" src="https://github.com/TeslaNik/CodeInPlace/blob/main/ppt02.png">

#### Hide image in images

We have an original image and a secret image. We convert both into 8-bit binary values and then convert the pixel components into 8-bit binary values.

Extracting the three most significant bits (MSB) from the secret image, we replace the three least significant bits of the original image. This results in minimal visible change in pixel values, although the secret and decoded pixels may have slight color variations as we only took limited information (3 MSBs.)

<img align="center" alt="Coding" width="750" src="https://github.com/TeslaNik/CodeInPlace/blob/main/ppt03.png">

### Results

Through practical examples, the project showcases the minimal visibility of changes in both text and image encoding. Successful retrieval of the hidden information is demonstrated, emphasizing the effectiveness of the LSB technique used.

### Acknowledgments

I would like to express my sincere appreciation to the organizers, mentors, and fellow participants of Code In Place 2021 for their support and guidance in the forums and discussions throughout the course.
