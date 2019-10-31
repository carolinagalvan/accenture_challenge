from car_detector import car_detector
from face_detector import face_detector
from smart_park_ui import park_ui
from aws_serv import aws_serv
import configparser
import datetime
import argparse
import cv2
import os

ap = argparse.ArgumentParser()
ap.add_argument('-c', '--config', required=True,
                help = 'path to config file')
args = ap.parse_args()

configFile = configparser.ConfigParser()
configFile.read(args.config)

bucket_name = os.getenv('BUCKET_NAME')
access_id = os.getenv('ACCESS_ID')
secret_key = os.getenv('SECRET_KEY')

# Initialize both detectors 
carDetector = car_detector(configFile['YOLO']['configFile'], 
                           configFile['YOLO']['weightsFile'], 
                           configFile['YOLO']['classesFile'],
                           configFile['YOLO']['useYOLO'])

faceDetector = face_detector(configFile['DATABASE']['databasePath'], 
                             int(configFile['DATABASE']['numberOfUsers']), 
                             configFile['DATABASE']['photoPrefix'], 
                             configFile['DATABASE']['photoSuffix'])
gui = park_ui()
smart_panel = gui.get_ui()

while True:
    smart_panel = gui.reset_gui()
    cv2.imshow('Smart-Parking', smart_panel)

    car_roi = carDetector.wait_for_car(configFile['SOURCE']['carDetectSrc'])
    cv2.imshow('ROI', car_roi)
    cv2.waitKey()
    cv2.destroyWindow('ROI')

    # Recognize plate text
    image_binary = aws_serv.img_to_byte(car_roi)
    rek_client = aws_serv.new_rekclient(access_id, secret_key)
    objectName = aws_serv.text_picture(rek_client, image_binary)

    smart_panel = gui.update_license_plate(objectName)
    cv2.imshow('Smart-Parking', smart_panel)

    # Upload image to bucket
    s3_client = aws_serv.new_s3client(access_id, secret_key)
    success = aws_serv.new_object(s3_client, objectName, image_binary, bucket_name)
    if success:
        print(f'Added {bucket_name} to {objectName}')

    user_name, user_face = faceDetector.wait_for_face(configFile['SOURCE']['faceDetectSrc'])
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