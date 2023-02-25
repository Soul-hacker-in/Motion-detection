import cv2 as cv
import numpy as np

cap = cv.VideoCapture('Video/movement.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # collecting the frame1 and frame2 abs difference
    diff = cv.absdiff(frame1, frame2)
    # converting into gray scale image
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    # for blurring
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    # for finding threshold
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    # for dilation
    dilated = cv.dilate(thresh, kernel=None, iterations=3)
    # for finding the contours
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # Putting Text into cap
    cv.putText(frame1, "PRESS 'ESC' To Quit.", (382, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    # for drawing each an every contour as rectangle
    for contour in contours:
        [x, y, w, h] = cv.boundingRect(contour)
        if cv.contourArea(contour) < 850:
            continue
        cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv.putText(frame1, "Movement {}".format('Detected'), (12, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    # Now drawing the contours
    # cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    # for displaying the frame
    cv.imshow('Inter', frame1)
    # Reassigning the values for next iteration
    frame1 = frame2
    ret, frame2 = cap.read()
    # for Terminate The code
    if cv.waitKey(40) == 27:
        break

cv.destroyAllWindows()
cap.release()
