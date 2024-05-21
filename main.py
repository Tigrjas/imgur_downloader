import pyautogui
import time
import webbrowser
import os
import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename='logfiles.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
count = 160


def download_image(name: str, link: str) -> None:
    # Initial browser open to incorrect page
    webbrowser.open(link, 0)
    time.sleep(3)
    os.system("taskkill /im chrome.exe /f")

    # Actual browser opening
    webbrowser.open(link, 0)
    time.sleep(2)

    # Process of downloading image
    pyautogui.moveTo(1720, 720)
    pyautogui.rightClick()
    pyautogui.moveRel(10, 50)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.write(name)
    pyautogui.press('enter')
    file_path = Path("C:/Users/jason/Downloads", name + ".png")

    # Make sure file is downloaded
    while not os.path.exists(file_path):
        time.sleep(1)

    # Logging information
    global count
    count += 1
    logger.info(f"{name} - downloaded ({count})")

    # Close webpage
    os.system("taskkill /im chrome.exe /f")
    time.sleep(2)


def find_imgur_link(content: str) -> str:
    # Regex pattern to extract the Imgur link
    imgur_pattern = re.compile(r'https://i\.imgur\.com/[^\s)]+')

    # Find all matches
    imgur_matches = imgur_pattern.findall(content)

    # Print the first match if it exists
    if imgur_matches:
        return imgur_matches[0]
    else:
        return "none"


def process_file(root, file_name):
    file_path = os.path.join(root, file_name)
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        name = file_name[:-3]
        link = find_imgur_link(content)
        logger.info(f"{name} - {link}")
        if link == "none":
            return
        download_image(name, link)


def test():
    # Purpose scan through the directory
    directory = r"C:\Users\jason\Desktop\download_imgur_project\Person"
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            process_file(root, file_name)


def main():
    directory = r"C:\Users\jason\Desktop\download_imgur_project\Person"

    for root, dirs, files in os.walk(directory):
        for file_name in files:
            process_file(root, file_name)


if __name__ == "__main__":
    main()
    # test()
