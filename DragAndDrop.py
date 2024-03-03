import cv2
import Hand_Tracking_Module as htm

cap = cv2.VideoCapture(0)

pTime = 0


detector = htm.HandTracker(minDetectionConf=0.7)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmlist, bbox = detector.findPosition(img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)

