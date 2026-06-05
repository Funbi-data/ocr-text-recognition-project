import cv2
import pytesseract

# Load image
img = cv2.imread("sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Extract text
text = pytesseract.image_to_string(gray)

print("Detected Text:")
print(text)