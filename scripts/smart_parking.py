from car_detector import car_detector
from face_detector import face_detector
from aws_serv import aws_serv
import argparse
import cv2
import os

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

carDetector = car_detector(args.config, args.weights, args.classes)
faceDetector = face_detector('../user_database/userdatabase_1.csv', 4, '../user_database/', '.jpeg')

user_name, user_face = faceDetector.wait_for_face(0)
car_roi = carDetector.wait_for_car(args.source)

bucket_name = os.getenv('BUCKET_NAME')
access_id = os.getenv('ACCESS_ID')
secret_key = os.getenv('SECRET_KEY')

# Recognize plate text
image_binary = aws_serv.img_to_byte(car_roi)
rek_client = aws_serv.new_rekclient(access_id, secret_key)
objectName = aws_serv.text_picture(rek_client, image_binary)

# Upload image to bucket
s3_client = aws_serv.new_s3client(access_id, secret_key)
success = aws_serv.new_object(s3_client, objectName, image_binary, bucket_name)
if success:
	print(f'Added {bucketName} to {objectName}')