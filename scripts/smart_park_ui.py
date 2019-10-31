import cv2
import numpy as np

class park_ui:
    def __init__(self):
        self.width = 500
        self.height = 500

        self.panel = np.zeros((self.width, self.height, 3), np.uint8)
        self.panel[:] = (0, 0, 0)
        self.font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(self.panel, 'Smart-Parking', (130, 35), self.font, 1.0, (255, 255, 255), 1)
        cv2.putText(self.panel, 'User: ', (10, 70), self.font, 1.0, (255, 255, 255), 1)
        cv2.putText(self.panel, 'License Plate: ', (10, 100), self.font, 1.0, (255, 255, 255), 1)
        self.panel[250:, :] = (0,0,255)

    def get_ui(self):
        return self.panel
    
    def update_user(self, user_name_):
        cv2.putText(self.panel, user_name_, (100, 70), self.font, 1.0, (255, 255, 255), 1)
        return self.panel

    def update_license_plate(self, user_plate_):
        cv2.putText(self.panel, user_plate_, (160, 70), self.font, 1.0, (255, 255, 255), 1)
        return self.panel

    def set_pass(self, pass_):
        if pass_:
            self.panel[250:, :] = (0,255,0)
        else:
            self.panel[250:, :] = (0,0,255)
        return self.panel

    def reset_gui(self):
        self.panel[:] = (0, 0, 0)
        self.font = cv2.FONT_HERSHEY_DUPLEX

        cv2.putText(self.panel, 'Smart-Parking', (130, 35), self.font, 1.0, (255, 255, 255), 1)
        cv2.putText(self.panel, 'User: ', (10, 70), self.font, 1.0, (255, 255, 255), 1)
        cv2.putText(self.panel, 'License Plate: ', (10, 100), self.font, 1.0, (255, 255, 255), 1)

        self.panel[250:, :] = (0,0,255)
        return self.panel
