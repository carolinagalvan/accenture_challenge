import cv2
import numpy as np
import pandas as pd

class parkingManager:
    def __init__(self, user_number_):
        self.width = 400
        self.parking_lot_img = np.zeros((100,self.width,3))
        self.parking_lot = pd.DataFrame(np.zeros((user_number_, 3)))
        self.parking_lot.columns = ['Occupied', 'User', 'License Plate']
        self.user_number = user_number_
        self.spot_width = int(self.width / self.user_number)
        self.font = cv2.FONT_HERSHEY_DUPLEX

    def get_free_spots(self):
        free_spots = 0
        for i in self.parking_lot['Occupied']:
            if i == 0:
                free_spots += 1
        return free_spots
    
    def assign_spot(self, user_):
        spot = self.parking_lot[self.parking_lot.Occupied == 0].index[0]
        self.parking_lot.loc[spot, 'Occupied'] = 1
        self.parking_lot.loc[spot, 'User'] = user_[0]
        self.parking_lot.loc[spot, 'License Plate'] = user_[1]
        return spot
    
    def free_spot(self, user_):
        spot = self.parking_lot[self.parking_lot.User == user_[0]].index[0]
        self.parking_lot.loc[spot, 'Occupied'] = 0
        self.parking_lot.loc[spot, 'User'] = 0
        self.parking_lot.loc[spot, 'License Plate'] = 0
        return spot
    
    def update_image(self):
        spot = 0
        for i in self.parking_lot['Occupied']:
            start = self.spot_width * (spot)
            end = self.spot_width * (spot) + 101
            if i == 0:
                self.parking_lot_img[:, start:end] = (0,255,0)
            else:
                self.parking_lot_img[:, start:end] = (0,0,255)
            spot += 1

        for i in range(self.user_number + 1):
            point = i * 100
            cv2.line(self.parking_lot_img,(point,0),(point,100),(255,255,255),5)
                    
        for i in range(self.user_number):
            point = i * 100 + 40
            cv2.putText(self.parking_lot_img, 'A' + str(i), (point, 30), self.font, 0.7, (255, 255, 255), 1)
        
        occupied = self.parking_lot[self.parking_lot.Occupied == 1].index
        for i in occupied:
            user = self.parking_lot.loc[i, 'User']
            license_plate = self.parking_lot.loc[i, 'License Plate']
            point = int(i) * 100 + 5
            cv2.putText(self.parking_lot_img, user, (point, 50), self.font, 0.3, (255, 255, 255), 1)
            cv2.putText(self.parking_lot_img, license_plate, (point, 70), self.font, 0.3, (255, 255, 255), 1)

        
        return self.parking_lot_img
            


