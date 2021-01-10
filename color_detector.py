import cv2
import numpy as np

class ColorDetector():
    def __init__(self, capture):
        self.capture = capture

    def run_detection(self):
        while True:
            _, frame = self.capture.read()
            cv2.imshow('Color Detector', frame)
            blue_mean = np.mean(frame[:, :, :1])
            green_mean = np.mean(frame[:, :, 1:2])
            red_mean = np.mean(frame[:, :, 2:])
            print("********************\nblue: "+str(blue_mean)+"\ngreen: "+str(green_mean)+"\nred: "+str(red_mean)+"\n********************")
            if blue_mean > green_mean and blue_mean > red_mean:
                print("Blue")
            if green_mean > red_mean and green_mean > blue_mean:
                print("Green")
            if red_mean > blue_mean and red_mean > green_mean:
                print("Red")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.capture.release()
        cv2.destroyAllWindows()

color_detector = ColorDetector(capture=cv2.VideoCapture(0))
color_detector.run_detection()