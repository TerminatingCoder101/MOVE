import math

import cv2
import mediapipe as mp
import time
import pyscreenshot
import pyautogui



class HandTracker():
    def __init__(self, mode = False, maxHands = 2, modelComplexity = 1, minDetectionConf = 0.5, minTrackConf = 0.5):

        static_image_mode=mode
        max_num_hands=maxHands
        model_complexity=modelComplexity
        min_detection_confidence=minDetectionConf
        min_tracking_confidence=minTrackConf


        self.myHands = mp.solutions.hands
        self.hands = self.myHands.Hands(static_image_mode, max_num_hands, model_complexity, min_detection_confidence, min_tracking_confidence)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img):


        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)


        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:

                self.mpDraw.draw_landmarks(img, hand_landmarks, self.myHands.HAND_CONNECTIONS)



        return img

    def findPosition(self, img, handNo = 0, draw = True):

        xList = []
        yList = []
        bbox = []
        self.lmList = []

        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[handNo]

            for id, ln in enumerate(hand.landmark):

                # print(id, ln)

                h, w, c = img.shape
                cx, cy = int(ln.x*w), int(ln.y*h)
                xList.append(cx)
                yList.append(cy)


                self.lmList.append([id, cx, cy])

                # print(id, cx, cy)

                if draw:
                    cv2.circle(img, (cx,cy), 5, (255, 0, 255), cv2.FILLED)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)

            bbox = xmin, ymin, xmax, ymax

            if draw:
                cv2.rectangle(img, (xmin -20, ymin-20), (xmax +20, ymax+20), (0, 255, 0), 2 )

        return self.lmList, bbox

    # def swipe(self, pTime, initial_position):
    #     while True:
    #         position = self.lmList[4]
    #
    #         cTime = time.time()
    #
    #         if abs(initial_position[0]-position[0])>100 and cTime-pTime>1:
    #             return True
    #
    #         if cTime-pTime > 3:
    #             return False

    def left_right(self):

        tip_x_position, tip_y_position = self.lmList[8][1], self.lmList[8][2]
        knuckle_x_position, knuckle_y_position = self.lmList[5][1], self.lmList[5][2]

        if abs(tip_y_position-knuckle_y_position) <50:
            if tip_x_position-knuckle_x_position>100:
                return "Right"
            elif tip_x_position-knuckle_x_position< -100:
                return "Left"







    def fingersUp(self):

        fingers = []

        #Thumb

        for id in range(1, 5):

            if self.lmList[self.tipIds[id]][2]< self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers



    def findDistance(self, p1, p2, img, draw = True,  r= 15, t = 3):
        x1, y1 = self.lmList[p1][1: ]
        x2, y2 = self.lmList[p2][1: ]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), t)
            cv2.circle(img, (x1, y1), r, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), r, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (cx, cy), r, (0, 255, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)

        return length, img, [x1, x2, y1, y2, cx, cy]









def main():
    cap = cv2.VideoCapture(1)

    pTime = 0
    cTime = 0

    detector = HandTracker()

    while True:
        success, img = cap.read()

        img = cv2.flip(img, 1)


        img = detector.findHands(img)

        lmList, bbox = detector.findPosition(img)

        if len(lmList) != 0:
            fingers = detector.fingersUp()

            if fingers == [0,1,1,1]:

                pyautogui.press("down")
                # screenshot=pyscreenshot.grab()
                # screenshot.show()

            if fingers == [1,0,0,0]:
                pyautogui.press("up")

            if fingers == [0,1,0,0]:
                print("bad")

            if detector.left_right() == "Left":
                pyautogui.press("left")

            if detector.left_right() == "Right":
                pyautogui.press("right")


            # initial_position = lmList[4]

            # if detector.swipe(pTime, initial_position):
            #     print("swipe")
            # print (fingers)
        #     print(lmList[4])





        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)




        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()