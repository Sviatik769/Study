import time
import cv2

time.sleep(2)
print("Conect to arduino...")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_defalt.xml')

cap = cv2.VideoCapture(0)

cap_width = 1280
cap_height =720

while True:
    ret, img = cap.read()
    cv2.rersizeWindow('img', cap_width, cap_height)
    cv2.line(img, (cap_width, cap_height//2)), (0, cap_height//2)
    cv2.line(img, (cap_width//2, 0), (cap_width//2, cap_height), (0, 255,0), 1)
    cv2.circle(img, (cap_width//2, cap_height//2), 5, (255, 255, 255), -1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.delectMultiScale(gray, 1.3)

    for (x, y, w, h) in faces:
        cv2.rectagle(img, (x, y), (x + w, y + h), (0, 255, 0), 5)
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = img[y:y + h, x:x + w]

        arr = {y: y + h, x: x + w}
        print('------------------')
        print('------------------')
        print(arr)

        print('X: %d   |   Y: %d' % (x, y))
        print('x+w: %d   |   y+h: %d' % (x + w, y + h))

        xx = int(x + (x + h)) / 2
        yy = int(y + (y + w)) / 2
        print('xx: %d   |   yy: %d' % (xx, yy))
        center = (xx, yy)

    cv2.imshow('img', img)