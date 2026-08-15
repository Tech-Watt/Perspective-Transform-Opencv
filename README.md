# Perspective Transform with OpenCV

A Python computer vision project that demonstrates perspective transformation (homography) using OpenCV. This technique transforms a skewed or angled view of a document into a flat, rectangular, bird's-eye view.

## Overview

This project takes an image of a paper photographed from an angle and applies a perspective transform to correct the distortion, resulting in a straightened, rectangular output image.

## Features

- **Perspective Transformation**: Corrects skewed or angled views of documents
- **Side-by-side Visualization**: Displays original and transformed images for comparison
- **Image Export**: Saves the transformed result as an output file

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Tech-Watt/Perspective-Transform-Opencv.git
cd Perspective-Transform-Opencv
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- `opencv-python` - OpenCV library for computer vision operations
- `cvzone` - Computer vision helper library for simplified OpenCV operations

## Usage

1. Place your input image in the project directory (or use the provided `paper.jpg`)

2. Run the script:
```bash
python main.py
```

3. The script will:
   - Display a side-by-side comparison window showing the original and transformed images
   - Save the transformed image as `output_image.jpg`
   - Wait for a key press to close the display window

## How It Works

1. **Load Image**: Reads the input image (`paper.jpg`)

2. **Define Source Points**: Specifies the four corner coordinates of the document in the original skewed image

3. **Define Destination Points**: Maps those corners to a perfect rectangle (400x500 pixels)

4. **Calculate Transform Matrix**: Uses `cv2.getPerspectiveTransform()` to compute the transformation matrix

5. **Apply Transformation**: Applies `cv2.warpPerspective()` to unwarp the image

6. **Display and Save**: Shows the comparison and saves the result

## Customization

To use your own image:

1. Replace `paper.jpg` with your image file (or update the filename in `main.py`)

2. Update the source coordinates in the code to match the corners of your document:
```python
coordinates = np.float32([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])
```

3. Adjust the output dimensions if needed:
```python
width = 400
height = 500
```

## Use Cases

- **Document Scanning**: Straighten photos of documents, receipts, or business cards
- **OCR Preprocessing**: Prepare images for text recognition
- **Augmented Reality**: Correct perspective in AR applications
- **License Plate Recognition**: Normalize angled license plate images
- **Book Scanning**: Flatten pages photographed at an angle

## Technical Details

The perspective transform is computed using a 3x3 transformation matrix that maps the source quadrilateral to the destination rectangle. This is a common technique in computer vision for correcting perspective distortion caused by camera angle.

## Example

**Input**: An angled photograph of a paper document  
**Output**: A flat, rectangular, straightened version of the document

The transformation preserves the content while correcting the geometric distortion.

## License

This project is open source and available for educational and commercial use.

## Author

Tech-Watt

## Contributing

Contributions, issues, and feature requests are welcome!
