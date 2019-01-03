import Settings
from time import sleep

def top_color_change(self):
    temp = self.topColor_comboBox.currentIndex()
    print("top")
    if temp == 1:
        Settings.ASD.write(bytes("1~0~8~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~0~8~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~0~8~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~0~8~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~0~8~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~"+str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~0~8~0~0~0~0", 'UTF-8'))

def left_color_change(self):
    temp = self.leftColor_comboBox.currentIndex()
    print("left")
    if temp == 1:
        Settings.ASD.write(bytes("1~8~15~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~8~15~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~8~15~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~8~15~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~8~15~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~" +str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~8~15~0~0~0~0", 'UTF-8'))

def right_color_change(self):
    temp = self.rightColor_comboBox.currentIndex()
    print("right")
    if temp == 1:
        Settings.ASD.write(bytes("1~15~23~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~15~23~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~15~23~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~15~23~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~15~23~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~" +str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~15~23~0~0~0~0", 'UTF-8'))

def bottom_color_change(self):
    temp = self.bottomColor_comboBox.currentIndex()
    print("bottom")
    if temp == 1:
        Settings.ASD.write(bytes("1~23~30~255~0~0~0", 'UTF-8'))
    elif temp == 2:
        Settings.ASD.write(bytes("1~23~30~0~255~0~0", 'UTF-8'))
    elif temp == 3:
        Settings.ASD.write(bytes("1~23~30~0~0~255~0", 'UTF-8'))
    elif temp == 4:
        Settings.ASD.write(bytes("1~23~30~0~0~0~255", 'UTF-8'))
    elif temp == 5:
        Settings.ASD.write(bytes("1~23~30~" + str(Settings.custom_R) + "~" + str(Settings.custom_G) + "~" + str(Settings.custom_B) + "~" +str(Settings.custom_W), 'UTF-8'))
    else:
        Settings.ASD.write(bytes("1~23~30~0~0~0~0", 'UTF-8'))

def IR_trigger(self):

    if not Settings.IR_STAT:
        Settings.ASD.write(bytes("3~", 'UTF-8'))
        Settings.IR_STAT=True
        self.IR_pushButton.setText("INFRARED:ON")
    
    else:
        Settings.ASD.write(bytes("4~", 'UTF-8'))
        Settings.IR_STAT=False
        self.IR_pushButton.setText("INFRARED:OFF")

def Cooling_trigger(self):

    if not Settings.CL_STAT:
        Settings.ASD.write(bytes("5~", 'UTF-8'))
        Settings.CL_STAT=True
        self.Cooling.setText("COOLING:ON")
    
    else:
        Settings.ASD.write(bytes("6~", 'UTF-8'))
        Settings.CL_STAT=False
        self.Cooling.setText("COOLING:OFF")




        




