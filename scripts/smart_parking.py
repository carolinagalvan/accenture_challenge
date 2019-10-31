from car_detector import car_detector
from face_detector import face_detector
from smart_park_ui import park_ui
import datetime
import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument('-c', '--config', required=True,
                help = 'path to yolo config file')
ap.add_argument('-w', '--weights', required=True,
                help = 'path to yolo pre-trained weights')
ap.add_argument('-cl', '--classes', required=True,
                help = 'path to text file containing class names')
ap.add_argument('-s', '--source', required=True,
                help = 'path to text file containing class names')
args = ap.parse_args()

# Initialize both detectors 
carDetector = car_detector(args.config, args.weights, args.classes)
faceDetector = face_detector('../user_database/userdatabase_1.csv', 4, '../user_database/', '.jpeg')
gui = park_ui()
smart_panel = gui.get_ui()

while True:
    smart_panel = gui.reset_gui()
    cv2.imshow('Smart-Parking', smart_panel)

    car_roi = carDetector.wait_for_car(args.source)
    cv2.imshow('ROI', car_roi)
    cv2.waitKey()
    cv2.destroyWindow('ROI')

    user_name, user_face = faceDetector.wait_for_face(0)
    cv2.imshow('User', user_face)
    cv2.waitKey(500)
    cv2.destroyWindow('User')

    smart_panel = gui.update_user(user_name)
    cv2.imshow('Smart-Parking', smart_panel)

    if user_name == 'Unknown':
        smart_panel = gui.set_pass(False)
    else:
        smart_panel = gui.set_pass(True)

    cv2.imshow('Smart-Parking', smart_panel)
    
    if cv2.waitKey() & 0xFF == ord('q'):
        break