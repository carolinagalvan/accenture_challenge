import cv2
import numpy as np

class park_ui:
    def __init__(self):
        self.width = 350
        self.height = 500

        self.panel = np.zeros((self.width, self.height, 3), np.uint8)
        self.panel[:] = (0, 0, 0)
        self.font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(self.panel, 'Smart-Parking', (130, 35), self.font, 1.0, (255, 255, 255), 1)
        cv2.putText(self.panel, 'User: ', (10, 70), self.font, 1.0, (255, 255, 255), 1)
        cv2.putText(self.panel, 'License Plate: ', (10, 105), self.font, 1.0, (255, 255, 255), 1)
        cv2.putText(self.panel, 'Assigned Spot: ', (10, 140), self.font, 1.0, (255, 255, 255), 1)
        self.panel[180:, :] = (0,0,255)
        cv2.putText(self.panel, 'NO ENTRY', (130, 270), self.font, 1.0, (255, 255, 255), 1)


    def get_ui(self):
        return self.panel
    
    def update_user(self, user_name_):
        cv2.putText(self.panel, user_name_, (100, 70), self.font, 1.0, (255, 255, 255), 1)
        return self.panel

    def update_license_plate(self, user_plate_):
        cv2.putText(self.panel, user_plate_, (240, 105), self.font, 1.0, (255, 255, 255), 1)
        return self.panel

    def update_parking(self, parking_spot_):
        cv2.putText(self.panel, 'A'+str(parking_spot_), (250, 140), self.font, 1.0, (255, 255, 255), 1)
        return self.panel

    def set_pass(self, pass_):
        if pass_:
            self.panel[180:, :] = (0,255,0)
            cv2.putText(self.panel, 'Access Granted', (130, 270), self.font, 1.0, (255, 255, 255), 1)
        else:
            self.panel[180:, :] = (0,0,255)
            cv2.putText(self.panel, 'Access Denied', (130, 270), self.font, 1.0, (255, 255, 255), 1)
        return self.panel

    def reset_gui(self):
        self.panel[:] = (0, 0, 0)
        self.font = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(self.panel, 'Smart-Parking', (130, 35), self.font, 1.0, (255, 255, 255), 1)
        cv2.putText(self.panel, 'User: ', (10, 70), self.font, 1.0, (255, 255, 255), 1)
        cv2.putText(self.panel, 'License Plate: ', (10, 105), self.font, 1.0, (255, 255, 255), 1)
        cv2.putText(self.panel, 'Assigned Spot: ', (10, 140), self.font, 1.0, (255, 255, 255), 1)
        self.panel[180:, :] = (0,0,255)
        cv2.putText(self.panel, 'No Access', (140, 270), self.font, 1.0, (255, 255, 255), 1)

        return self.panel
