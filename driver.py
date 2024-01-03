from python_imagesearch.imagesearch import imagesearch
import pyautogui
import cv2
import os
import time

with open(".env", "r") as env:
    EMAIL = env.readline().split("=")[1]
    PASS = env.readline().split("=")[1]

def main():
    login()
    name = input("Enter name to search: ")
    getMessengerScreenshot(name)
    

def login():
    # clickIfSafe("./fb-email-input.png")
    # pyautogui.typewrite(EMAIL)
    # clickIfSafe("./fb-password-input.png")
    # pyautogui.typewrite(PASS)
    # clickIfSafe("./fb-login-btn.png")
    pass

def getMessengerScreenshot(name):
    clickIfSafe("resources/mes-search-bar.png")
    pyautogui.typewrite(name)
    x, y = pyautogui.position()
    time.sleep(0.1)
    pyautogui.click(x, y+100)
    time.sleep(0.1)
    active_pos = imagesearch("resources/mes-active.png")
    emoji_pos = imagesearch("resources/mes-emoji.png")
    print("Capture: " + str(active_pos) + " " + str(emoji_pos))
    top_x = active_pos[0] - 50
    top_y = active_pos[1] - 30
    width = emoji_pos[0] - active_pos[0] + 130
    height = emoji_pos[1] - active_pos[1] + 75
    time.sleep(0.1)
    filename = "screen-" + name.strip() + ".png"
    pyautogui.screenshot(filename, region=(top_x, top_y, width, height))
    return filename

def clickIfSafe(img_path):
    pos = imagesearch(img_path)
    im = cv2.imread(img_path)
    h, w, c = im.shape
    if pos[0] != -1:
        pyautogui.click(pos[0] + w/2, pos[1] + h/2)
    else:
        raise RuntimeError("Image " + str(img_path) + " not found")

if __name__ == "__main__":
    main()