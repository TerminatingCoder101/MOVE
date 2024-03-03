import cv2
import numpy as np
import time
import Hand_Tracking_Module as htm
import math
import osascript


cap = cv2.VideoCapture(0)
pTime = 0
detector = htm.HandTracker(minDetectionConf=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist, bbox = detector.findPosition(img, draw = False)

    if len(lmlist) != 0:
        #print(lmlist[2])

        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # cv2.circle(img, (x1,y1), 15, (255, 0, 0), cv2.FILLED)
        # cv2.circle(img, (x2,y2), 15, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255,0,0), 3)
        cv2.circle(img, (cx, cy), 15, (0, 255, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)

        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)


        vol = np.interp(length, [50,300], [0,100])
        print(vol)

        osascript.osascript("set volume output volume {}".format(vol))








    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)