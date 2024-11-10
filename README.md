# License-Plate-Detection-and-Recognition-System-using-OpenCV-YOLOv5-PyTesseract


![License Plate Detection](https://drive.google.com/file/d/1X_9F7-nupk0Pxs8JXvG1Vz2WGZ8-xUSC/view?usp=sharing)

## 🚀 Overview

This project implements an advanced License Plate Detection and Recognition System using state-of-the-art computer vision techniques. It combines the power of YOLOv5 for object detection and PyTesseract for Optical Character Recognition (OCR) to accurately identify and read license plates from images of vehicles.

### 🎯 Key Features

- **Vehicle Detection**: Utilizes YOLOv5 to identify vehicles in images.
- **License Plate Localization**: Employs contour analysis for precise plate detection.
- **OCR Integration**: Leverages PyTesseract for accurate text extraction from license plates.
- **Real-time Processing**: Capable of processing images in real-time with efficient algorithms.
- **User-friendly Interface**: Simple command-line interface for easy interaction.

## 🛠️ Technologies Used

- Python 3.x
- OpenCV
- Ultralytics YOLOv5
- PyTesseract
- NumPy

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- Tesseract OCR installed on your system
- CUDA-capable GPU (recommended for optimal performance)

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/license-plate-detection.git
2. Navigate to the project directory:
   ```bash
   cd license-plate-detection
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
4. Download the YOLOv5 weights:
   ```bash
   wget https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5s.pt
5. Set up Tesseract OCR path in the script:
   ```bash
   pytesseract.pytesseract.tesseract_cmd = r'path/to/your/tesseract'

## 🚀 Usage

1. Place your vehicle images in the images/ directory.
2. Run the main script:
   ```bash
   python license_plate_detection.py
3.Enter the image number when prompted (e.g., for Cars1.png, enter 1).
4.View the results in the displayed windows and console output.

## 🧪 Performance Metrics

## 📊 Results Visualization
Results

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

Adithya N Raj - adithyanraj03@gmail.com <br>
Project Link: https://github.com/adithyanraj03/License-Plate-Detection-and-Recognition-System-using-OpenCV-YOLOv5-PyTesseract <br>⭐️ From Adithya N Raj
