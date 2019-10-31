import boto3
import cv2

# Facade to used aws services (rekognition and storage)
class aws_serv:
	
	# Function that takes a Mat-Image
	# : []Byte
	def img_to_byte(img):
		_, encoded_image = cv2.imencode('.png', img)
		image_binary = encoded_image.tobytes()
		return image_binary

	# Creates a new client for storage
	def new_s3client(id, secret, region='us-east-2'):
		s3_client = boto3.client('s3', aws_access_key_id=id, aws_secret_access_key=secret,region_name=region)
		return s3_client

	# Creates a new object for bucket
	def new_object(client, objectName, data, bucketName):
		success = client.put_object(Bucket=bucketName, Key=objectName, Body=data)
		return success

	# Creates a new client for rekognition
	def new_rekclient(id, secret, region='us-east-2'):
		rek_client = boto3.client('rekognition', aws_access_key_id=id, aws_secret_access_key=secret,region_name=region)
		return rek_client

	# Function that retrieves text for a given Mat:image
	def text_picture(client, image_binary):
		response=client.detect_text(Image={'Bytes':image_binary})
		textDetections=response['TextDetections']
		return textDetections[0]['DetectedText']
        