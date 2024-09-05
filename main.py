from pathlib import Path
import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import webbrowser
import pyautogui

KEYBOARD_MAPPING = {
    "pause/resume": "playpause",
    "next": "nexttrack",
    "prev": "prevtrack",
    "stop": "stop",
    "volume_inc": "volumeup",
    "volume_dec": "volumedown",
    "mute": "volumemute"
}

COMMAND_NAMES = {
    "pause_or_resume_media": "pause/resume",
    "next_media": "next",
    "prev_media": "prev",
    "stop_media": "stop",
    "volume_inc": "vu",
    "volume_dec": "vd",
    "mute": "mute",
}

COMMANDS = [
        {
            "title": COMMAND_NAMES["pause_or_resume_media"],
            "subTitle": "Pause or resume playing media",
            "icoPath": "images/app.png",
            "score": 1,
            "jsonRPCAction": {
                "method": "pause_or_resume_media",
                "parameters": []
            }
        },
        {
            "title": COMMAND_NAMES["next_media"],
            "subTitle": "Plays next media if it is available",
            "icoPath": "images/app.png",
            "score": 1,
            "jsonRPCAction": {
                "method": "next_media",
                "parameters": []
            }
        },
        {
            "title": COMMAND_NAMES["prev_media"],
            "subTitle": "Plays previous media if it is available",
            "icoPath": "images/app.png",
            "score": 1,
            "jsonRPCAction": {
                "method": "prev_media",
                "parameters": []
            }
        },
        {
            "title": COMMAND_NAMES["stop_media"],
            "subTitle": "Stops playing media",
            "icoPath": "images/app.png",
            "score": 1,
            "jsonRPCAction": {
                "method": "stop_media",
                "parameters": []
            }
        },
        {
            "title": COMMAND_NAMES["volume_inc"],
            "subTitle": "Increases volume by indicated amount",
            "icoPath": "images/app.png",
            "score": 1,
            "jsonRPCAction": {
                "method": "volume_inc",
                "parameters": []
            }
        },
        {
            "title": COMMAND_NAMES["volume_dec"],
            "subTitle": "Decreases volume by indicated amount",
            "icoPath": "images/app.png",
            "score": 1,
            "jsonRPCAction": {
                "method": "volume_dec",
                "parameters": []
            }
        },
        {
            "title": COMMAND_NAMES["mute"],
            "subTitle": "Mutes system volume",
            "icoPath": "images/app.png",
            "score": 1,
            "jsonRPCAction": {
                "method": "mute",
                "parameters": []
            }
        }
    ]

class Nutils(FlowLauncher):

    def query(self, query: str) -> list:
        if len(query) == 0:
            return []
        
        return self.resolve_query(query.strip().lower())

    def resolve_query(self, arg: str) -> list:        
        query_result = []
        for command in COMMANDS:
            if arg in command["title"]:
                query_result.append(command)
            
        return query_result

    def context_menu(self, data):
        return [
            {
                "title": "Hello World Python's Context menu",
                "subTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "icoPath": "Images/app.png",  # related path to the image
                "jsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher.Plugin.HelloWorldPython"]
                },
                "score": 0
            }
        ]

    def pause_or_resume_media(self):
        pyautogui.press(KEYBOARD_MAPPING["pause/resume"])
    
    def next_media(self):
        pyautogui.press(KEYBOARD_MAPPING["next"])
    
    def prev_media(self):
        pyautogui.press(KEYBOARD_MAPPING["prev"], presses=2)
    
    def stop_media(self):
        pyautogui.press(KEYBOARD_MAPPING["stop"])


    def open_url(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    Nutils()
