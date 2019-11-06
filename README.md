# Smart-Parking by Visionaries

Smart Parking es un sistema de administración de estacionamiento inteligente basado en redes neuronales y algoritmos de machine learning que permiten reconocer a los usuarios, ya sea por su cara o utilizando la placa de su vehículo.

El proyecto se divide en diferentes clases, las cuales se encuentran en el directorio scripts:

- car_detector: utiliza YOLO para detectar la presencia de vehículos en la cámara, para posteriormente tomar una imagen del área de interés que será utilizada para leer la placa del mismo.

- face_detector: utiliza la librería de Python llamada face_detection (basada en dlib) para detectar e identificar caras en la imagen. Esto permite dar acceso al usuario al estacionamiento.

- aws_serv: es utilizada parar enlazarse con AWS Rekognition y detectar texto en una imagen, la cual, en este escenario, es la placa del vehículo.

- smart_park_ui: es la clase que se encarga de crear y administrar la interfaz gráfica principal del sistema. Utiliza OpenCV.

- parking_spot_assign: clase que permite administrar los lugares de estacionamiento a asignar, utilizando OpenCV. 

El script principal, el cual emplea todas las clases, es llamado smart_parking.py. Este se puede correr bajo diferentes configuraciones, las cuales pueden ser modificadas utilizando los config files de la carpeta config. Existen dos modos principales:

- Stream: utiliza la cámra del dispositivo para correr el algoritmo. 

 `$ python smart_parking.py --config ../config/config_stream.ini`

- Video: utiliza videos de vehículos tomados en el estacionamiento de accenture para la parte de detección de placas. La detección facial es con la cámara del dispositivo.

 `$ python smart_parking.py --config ../config/config_video.ini`


Dependencias:

- OpenCV
- Numpy
- face_recognition (https://github.com/ageitgey/face_recognition)
- YOLO (https://pjreddie.com/darknet/yolo/)
- AWS Rekognition

