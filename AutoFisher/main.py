import numpy as np
from PIL import ImageGrab
# For input in DirectX games, normal libraries dont work.
from DirectKeys import PressKey, ReleaseKey, K, I, S, D, A, W
import time
import winsound
import pyautogui

# Defining variable for conditions and beep sounds.
#############################
frequency = 2000            #
duration = 500              #
fishcatched = 0             #
rhs = True                  # For reference if standing on Right side or not
fishfound = False           #
#############################

# winsound.Beep(frequency, duration) #For debuging creates a sound


time.sleep(5)  # Delay For getting back to game screen after running the script

# print(pyautogui.position()) #Print cursor position for debugging
# winsound.Beep(frequency, duration) #For debuging creates a sound


# For Deubugging (Gets pixels RGB value and prints it.)
#######################################################################################################
# img = ImageGrab.grab(bbox=(581,0,1339,76)).convert('RGB') #Capture part of screen and convert to RGB #
# img_np = np.array(img) #Convert to array                                                             #
# pixel= img_np[35, 455] #Get specific pixel                                                           #
# print (pixel)                                                                                        #
#######################################################################################################


while True:

    try:  # Sometimes fails due to OS Error
        img = ImageGrab.grab(bbox=(581, 0, 1339, 76)).convert('RGB')  # Capture part of screen
        img_np = np.array(img)  # Convert the pic to array
        pixel = img_np[35, 455]  # Get Pixel RGB Value in this case pixel at (x,y) ==> (35,455)
    except:
        print("ERROR CANNOT CAPTURE")
        print("RETRYING")



    if pixel[0] >= 210 and pixel[1] >= 210 and pixel[2] >= 212 and pixel[
        2] < 235:  # Checks for white color at that pixel. If found that means fish catch.

        fishfound = True
        fishcatched = fishcatched + 1

        PressKey(K)  # Press key K to reel in fish
        time.sleep(0.1)
        ReleaseKey(K)

        # winsound.Beep(frequency, duration + 1000)

        time.sleep(9.9+1.5)  # Wait for reeling in fish.


        # Move from right to left and vise versa after every 3 fish catched
        #######################################AFK KILLER ##################################
        if fishcatched == 3 and rhs is True:
            fishcatched = 0

            PressKey(S)
            time.sleep(2.5)
            ReleaseKey(S)

            PressKey(A)
            time.sleep(4)
            ReleaseKey(A)

            PressKey(W)
            time.sleep(2.5)
            ReleaseKey(W)

            rhs = False
        elif fishcatched == 3 and rhs is False:
            fishcatched = 0

            PressKey(S)
            time.sleep(3.2)
            ReleaseKey(S)

            PressKey(D)
            time.sleep(4)
            ReleaseKey(D)

            PressKey(W)
            time.sleep(2.5)
            ReleaseKey(W)

            rhs = True
        ####################################################################################

        ############################Restart Fishing#########################################
        PressKey(I)  # Open inventory
        ReleaseKey(I)

        # Move cursor and select fishing rod to fish again
        pyautogui.moveTo(740, 468, duration=0.1)
        time.sleep(0.1)
        pyautogui.click(button='right')
        pyautogui.moveTo(760, 485, duration=0.1)
        time.sleep(0.2)
        pyautogui.click(button='left')
        PressKey(I)
        ReleaseKey(I)
        PressKey(I)
        ReleaseKey(I)

        time.sleep(0.5)
        
        # Repeated because sometimes failes due to lag in server.
        pyautogui.moveTo(740, 468, duration=0.1)
        time.sleep(0.2)
        pyautogui.click(button='right')
        pyautogui.moveTo(760, 485, duration=0.1)
        time.sleep(0.2)
        pyautogui.click(button='left')
        PressKey(I)
        ReleaseKey(I)
        ####################################################################

        # SOLVED NO NEED BUT KEPT FOR REFERENCE
        # Wait for a another image that effects the code to get away()
        # time.sleep(7)

    else:

        PressKey(W)  # Keep pressing W (move forward) to make sure game doesnt think i am afk and change camera
        time.sleep(0.2)  # Multipurpose for release key delay and wait for next screen grab.
        ReleaseKey(W)

        isgreen = False
