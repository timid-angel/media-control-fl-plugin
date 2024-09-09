import pyautogui
from math import ceil
from flowlauncher import FlowLauncher

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

APP_IMG = "images/app.png"


class MediaControl(FlowLauncher):

    def query(self, query: str) -> list:
        arguments = list(map(lambda x: x.strip(), query.lower().split(" ")))
        query_data = []
        for arg in arguments:
            if arg != "":
                query_data.append(arg)

        commands = [
            {
                "title": COMMAND_NAMES["pause_or_resume_media"],
                "subTitle": "Pause or resume playing media",
                "icoPath": APP_IMG,
                "score": 1,
                "jsonRPCAction": {
                    "method": "pause_or_resume_media",
                    "parameters": []
                }
            },
            {
                "title": COMMAND_NAMES["next_media"],
                "subTitle": "Plays next media if it is available",
                "icoPath": APP_IMG,
                "score": 1,
                "jsonRPCAction": {
                    "method": "next_media",
                    "parameters": []
                }
            },
            {
                "title": COMMAND_NAMES["prev_media"],
                "subTitle": "Plays previous media if it is available",
                "icoPath": APP_IMG,
                "score": 1,
                "jsonRPCAction": {
                    "method": "prev_media",
                    "parameters": []
                }
            },
            {
                "title": COMMAND_NAMES["stop_media"],
                "subTitle": "Stops playing media",
                "icoPath": APP_IMG,
                "score": 1,
                "jsonRPCAction": {
                    "method": "stop_media",
                    "parameters": []
                }
            },
            {
                "title": COMMAND_NAMES["volume_inc"] + ((" " + query_data[1]) if len(query_data) > 1 else " #"),
                "subTitle": f"Increases volume by {(query_data[1] if len(query_data) > 1 else "the specified amount")}" if (len(query_data) <= 1 or query_data[1].isdigit()) else "Invalid input: second argument must be a non-negative number",
                "icoPath": APP_IMG,
                "score": 1,
                "jsonRPCAction": {
                    "method": "volume_inc",
                    "parameters": [query_data[1]] if len(query_data) > 1 else []
                }
            },
            {
                "title": COMMAND_NAMES["volume_dec"] + ((" " + query_data[1]) if len(query_data) > 1 else " #"),
                "subTitle": f"Decreases volume by {(query_data[1] if len(query_data) > 1 else "the specified amount")}" if (len(query_data) <= 1 or query_data[1].isdigit()) else "Invalid input: second argument must be a non-negative number",
                "icoPath": APP_IMG,
                "score": 1,
                "jsonRPCAction": {
                    "method": "volume_dec",
                    "parameters": [query_data[1]] if len(query_data) > 1 else []
                }
            },
            {
                "title": COMMAND_NAMES["mute"],
                "subTitle": "Mutes system volume",
                "icoPath": APP_IMG,
                "score": 1,
                "jsonRPCAction": {
                    "method": "mute",
                    "parameters": []
                }
            }
        ]

        if len(query) == 0:
            return commands

        return self.resolve_query(query.strip().lower(), commands)

    def resolve_query(self, arg: str, commands: list) -> list:
        query_result = []
        for command in commands:
            if arg in command["title"]:
                query_result.append(command)

        return query_result

    def pause_or_resume_media(self):
        pyautogui.press(KEYBOARD_MAPPING["pause/resume"])

    def next_media(self):
        pyautogui.press(KEYBOARD_MAPPING["next"])

    def prev_media(self):
        pyautogui.press(KEYBOARD_MAPPING["prev"], presses=2)

    def stop_media(self):
        pyautogui.press(KEYBOARD_MAPPING["stop"])

    def volume_inc(self, amount=1):
        if type(amount) == str and not amount.isdigit():
            return

        amount = min(int(amount), 100)
        pyautogui.press(
            KEYBOARD_MAPPING["volume_inc"], presses=ceil(amount / 2))

    def volume_dec(self, amount=1):
        if type(amount) == str and not amount.isdigit():
            return

        amount = min(int(amount), 100)
        pyautogui.press(
            KEYBOARD_MAPPING["volume_dec"], presses=ceil(amount / 2))

    def mute(self):
        pyautogui.press(KEYBOARD_MAPPING["mute"])

    def open_url(self, url):
        webbrowser.open(url)