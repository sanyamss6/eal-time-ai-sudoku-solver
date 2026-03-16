import cv2
import numpy as np

# open webcam
cap = cv2.VideoCapture(0)

print("Starting camera... show sudoku puzzle")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # blur image
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # detect edges
    edges = cv2.Canny(blur, 50, 150)

    # display windows
    cv2.imshow("Camera Feed", frame)
    cv2.imshow("Edges", edges)

    # press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
