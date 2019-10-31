import cv2
import numpy as np

class car_detector:
    
    def __init__(self, config_, weights_, classes_, use_net_):

        self.classesclasses = None
        with open(classes_, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]
        
        self.COLORS = np.random.uniform(0, 255, size=(len(self.classes), 3))
        self.net = cv2.dnn.readNet(weights_, config_)
        self.use_net = use_net_

    def get_output_layers(self, net):
    
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        return output_layers

    def draw_prediction(self, img, class_id, confidence, x, y, x_plus_w, y_plus_h):

        label = str(' ')
        color = self.COLORS[1]
        cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)
        cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    def wait_for_car(self, source_):

        roi = np.zeros((430,430))
        carArea = 0
        lifeCounter = 0
        
        if source_ == 'camera_laptop':
            cap = cv2.VideoCapture(0)
        elif source_ == 'camera_logitech':
            cap = cv2.VideoCapture(1)
        else:
            cap = cv2.VideoCapture(source_)
        
        if (cap.isOpened()== False): 
            print("Error opening video stream or file")

        while (1):
            
            ret, image = cap.read()
            if ret:
                image = cv2.resize(image, (600, 400))
                image = cv2.flip(image, +1)

                Width = image.shape[1]
                Height = image.shape[0]
                scale = 0.00392
                
                blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

                self.net.setInput(blob)

                outs = self.net.forward(self.get_output_layers(self.net))

                class_ids = []
                confidences = []
                boxes = []
                conf_threshold = 0.5
                nms_threshold = 0.4

                for out in outs:
                    for detection in out:
                        scores = detection[5:]
                        class_id = np.argmax(scores)
                        confidence = scores[class_id]
                        if confidence > 0.5:
                            center_x = int(detection[0] * Width)
                            center_y = int(detection[1] * Height)
                            w = int(detection[2] * Width)
                            h = int(detection[3] * Height)
                            x = center_x - w / 2
                            y = center_y - h / 2
                            class_ids.append(class_id)
                            confidences.append(float(confidence))
                            boxes.append([x, y, w, h])

                indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

                for i in indices:
                    i = i[0]
                    if class_ids[i] != 0:
                        box = boxes[i]
                        x = box[0]
                        y = box[1]
                        w = box[2]
                        h = box[3]
                        self.draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))
                        roi = image[round(y):round(y+h), round(x):round(x+w)]
                        carArea = roi.shape[0] * roi.shape[1]
                        
                cv2.imshow('License Plate Camera', image)
                
                if self.use_net == 'Yes':
                    if carArea >= 42000:
                        lifeCounter += 1
                        if lifeCounter == 3:
                            #cv2.imshow('roi', roi)
                            break
                elif cv2.waitKey(10) & 0xFF == ord('f'):
                    roi = image
                    break
            
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release() 
        cv2.destroyWindow('License Plate Camera')
        #cv2.destroyWindow('roi')
        return roi

        
