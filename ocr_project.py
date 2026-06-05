import cv2
import pytesseract

# Tell Python where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read image
image = cv2.imread("sample.png")

# Convert image to text
text = pytesseract.image_to_string(image)

print("Detected Text:")
print(text)