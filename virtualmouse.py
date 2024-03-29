import cv2
import mediapipe as mp
import pyautogui
import subprocess
import functions as f


def mouse():
    capt = cv2.VideoCapture(0)
    hand_detector = mp.solutions.hands.Hands()
    drawing_utils = mp.solutions.drawing_utils
    screen_width, screen_height = pyautogui.size()
    index_y = 0
    previous_positions = []
    while True:
        _, frame = capt.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                for id, landmark in enumerate(landmarks):
                    x = int(landmark.x*frame_width)
                    y = int(landmark.y*frame_height)
                    if id == 8:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        index_x = screen_width/frame_width*x
                        index_y = screen_height/frame_height*y

                    if id == 4:
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                        thumb_x = screen_width/frame_width*x
                        thumb_y = screen_height/frame_height*y
                        #print('outside', abs(index_y - thumb_y))
                        if abs(index_y - thumb_y) < 65:
                            print('clicking')
                            subprocess.run(["move", "click"])
                            pyautogui.sleep(1)
                        elif abs(index_y - thumb_y) < 200:
                            # f.m_index(index_x,index_y)
                            pyautogui.moveTo(index_x, index_y)
        cv2.imshow('Virtual Mouse', frame)
        cv2.waitKey(1)

# prev = mouse()
# while True:
#     curr = mouse()
#     delta_x = curr[0] - prev[0]
#     delta_y = curr[1] - prev[1]
#     subprocess.run(["move", "mouse", str(delta_x), str(delta_y)])
#     prev = curr



def main():
    mouse()

if __name__ == "__main__":
    main()