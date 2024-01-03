from python_imagesearch.imagesearch import imagesearch
import pyautogui
import cv2
import os
import time

with open(".env", "r") as env:
    EMAIL = env.readline().split("=")[1]
    PASS = env.readline().split("=")[1]

def main():
    # clickIfSafe("./fb-email-input.png")
    # pyautogui.typewrite(EMAIL)
    # clickIfSafe("./fb-password-input.png")
    # pyautogui.typewrite(PASS)
    # clickIfSafe("./fb-login-btn.png")
    name = input("Enter name to search: ")
    clickIfSafe("./mes-search-bar.png")
    pyautogui.typewrite(name)
    x, y = pyautogui.position()
    time.sleep(0.1)
    pyautogui.click(x, y+100)
    time.sleep(0.1)
    active_pos = imagesearch("mes-active.png")
    emoji_pos = imagesearch("mes-emoji.png")
    print("Capture: " + str(active_pos) + " " + str(emoji_pos))
    top_x = active_pos[0] - 50
    top_y = active_pos[1] - 30
    width = emoji_pos[0] - active_pos[0] + 140
    height = emoji_pos[1] - active_pos[1] + 75
    pyautogui.screenshot("./screen-" + name.strip() + ".png", region=(top_x, top_y, width, height))


def clickIfSafe(img_path):
    pos = imagesearch(img_path)
    im = cv2.imread(img_path)
    h, w, c = im.shape
    if pos[0] != -1:
        pyautogui.click(pos[0] + w/2, pos[1] + h/2)
    else:
        raise RuntimeError("Image " + str(img_path) + " not found")

main()