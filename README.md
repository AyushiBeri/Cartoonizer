# Cartoonizer
 Cartoonify Image with OpenCV and Python

This project demonstrates how to transform an image into a cartoon-like version using OpenCV. By applying edge detection, color quantization, and bilateral filtering, we can create a fun cartoonified effect.

## Features

- **Edge Detection:** Converts the image to grayscale and finds the edges.
- **Color Quantization:** Reduces the number of colors in the image to make it look more cartoonish.
- **Bilateral Filtering:** Smooths the image while preserving edges to enhance the cartoon effect.

## How It Works

1. **Read Image:** The program reads the image using OpenCV.
2. **Edge Detection:** It converts the image to grayscale and applies adaptive thresholding to detect edges.
3. **Color Quantization:** Reduces the number of colors in the image using the k-means clustering algorithm.
4. **Bilateral Filter:** The image is smoothed, preserving edges to maintain the cartoon effect.
5. **Combine Results:** The filtered image is combined with the edge-detection mask to produce a cartoon-like result.


## Parameters
-**line_size:** Controls the thickness of the detected edges.
-**blur_value:** Controls the amount of blur applied to the image for edge detection.
-**total_color**: Number of colors to reduce the image to during color quantization.


## Example
Here's an example of a source image transformed into a cartoon:



![girl](https://github.com/user-attachments/assets/83c3fdba-9e71-4b07-b476-bce3a3dc0241)
**||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||**
![Screenshot 2024-09-12 203321](https://github.com/user-attachments/assets/854131cc-99e8-47f6-b3bf-982db5eeb374)

## Requirements
-**Python 3.x**
-**OpenCV**
-**NumPy**

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cartoonify-image-opencv.git

2. Install the required dependencies:
   ```bash
   pip install opencv-python numpy

3. Run the Python script:
   ```bash
   python cartoonify.py


