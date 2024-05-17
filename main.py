import pyautogui
import time
import webbrowser
import os
from pathlib import Path

# Mouse Functions
# print(pyautogui.size())  # Prints resolution of screen (width=3440, height=1440)
# print(pyautogui.position())  # Prints position of mouse currently
# pyautogui.moveTo(100, 100, 4)  # moves mouse to position over time, can remove
# pyautogui.moveRel(100, 100, 3) # moves relative to current position
# pyautogui.click(500, 500, 3, 3, button="left")

# pyautogui.scroll(500)
# Mouse up and down (click and dragging)
# pyautogui.mouseDown(500, 500, button="left")
# pyautogui.moveTo(550, 500, 3)


def download_image(file_name):
    pyautogui.moveTo(1720, 720)
    pyautogui.rightClick()
    pyautogui.moveRel(10, 50)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.write(file_name)
    pyautogui.press('enter')
    file_path = Path("C:/Users/jason/Downloads", file_name + ".png")
    time.sleep(1)
    print(os.path.exists(file_path))


def main():
    # Open webpage
    webpage = "https://imgur.com/rfiCiqa"
    webimage = webpage + ".png"
    webbrowser.open(webimage, 0)

    time.sleep(1)

    # Download image
    file_name = "hello"
    download_image(file_name)

    # Close webpage
    os.system("taskkill /im chrome.exe")


if __name__ == "__main__":
    main()
    # test_coordinate()
