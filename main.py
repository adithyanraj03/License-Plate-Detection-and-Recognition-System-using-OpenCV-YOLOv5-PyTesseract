import os
import cv2
import numpy as np
from ultralytics import YOLO
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    return edges


def detect_license_plate(image_path):
    # Load YOLOv5 model
    model = YOLO('yolov5su.pt')

    # Read image
    image = cv2.imread(image_path)

    # Detect vehicles
    results = model(image)

    # Process each detected vehicle
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Check if the detected object is a vehicle (class 2, 5, or 7 in COCO dataset)
            if box.cls in [2, 5, 7]:  # car, bus, truck
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                vehicle_roi = image[y1:y2, x1:x2]

                # Preprocess the vehicle ROI
                preprocessed_roi = preprocess_image(vehicle_roi)

                # Apply license plate detection on the preprocessed ROI
                contours, _ = cv2.findContours(preprocessed_roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

                for contour in contours:
                    area = cv2.contourArea(contour)
                    if area > 1000:  # Adjust this threshold as needed
                        x, y, w, h = cv2.boundingRect(contour)
                        aspect_ratio = w / float(h)
                        if 2 < aspect_ratio < 5:  # Common aspect ratio for license plates
                            plate_roi = vehicle_roi[y:y + h, x:x + w]

                            # Perform OCR on the plate ROI
                            plate_text = ocr_license_plate(plate_roi)

                            # Draw rectangle around the license plate
                            cv2.rectangle(image, (x1 + x, y1 + y), (x1 + x + w, y1 + y + h), (0, 255, 0), 2)

                            # Put the OCR result on the image
                            cv2.putText(image, plate_text, (x1 + x, y1 + y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                                        (0, 255, 0), 2)

                            return image, plate_roi, plate_text

    return image, None, None


def ocr_license_plate(plate_image):
    # Preprocess the plate image for better OCR results
    gray = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Perform OCR
    config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(thresh, config=config)

    # Clean the text
    clean_text = ''.join(e for e in text if e.isalnum())

    return clean_text


def main():
    while True:
        user_input = input("Enter image number (or 'q' to quit): ")

        if user_input.lower() == 'q':
            break

        image_path = f"images/Cars{user_input}.png"

        if not os.path.exists(image_path):
            print(f"Error: Image {image_path} does not exist.")
            continue

        # Display original image
        original_image = cv2.imread(image_path)
        cv2.imshow("Original Image", original_image)
        cv2.waitKey(1)  # This will display the image and continue execution

        result_image, plate_image, plate_text = detect_license_plate(image_path)

        if plate_image is not None:
            cv2.imshow("Detected License Plate", plate_image)
            cv2.imshow("Result", result_image)
            print(f"Detected license plate text: {plate_text}")
        else:
            print("No license plate detected")

        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()