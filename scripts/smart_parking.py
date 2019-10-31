from car_detector import car_detector
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

carDetector = car_detector(args.config, args.weights, args.classes)
placa = carDetector.wait_for_car(args.source)
cv2.imshow('ROI', placa)
cv2.waitKey()