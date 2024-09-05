from pathlib import Path
import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import webbrowser

class Nutils(FlowLauncher):

    def query(self, query):
        return [
            {
                "title": "Hello World, this is where title goes. {}".format(('Your query is: ' + query, query)[query == '']),
                "subTitle": "This is where your subtitle goes, press enter to open Flow's url",
                "icoPath": "Images/app.png",
                "jsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher"]
                },
                "score": 1
            },
            {
                "title": "pause/resume",
                "subTitle": "Pause or resume playing media",
                "icoPath": "images/app.png",
                "score": 1,
                "jsonRPCAction": {
                    "method": "pause_resume_media",
                    "parameters": []
                }
            },
            {
                "title": "next",
                "subTitle": "Plays next media if it is available",
                "icoPath": "images/app.png",
                "score": 1,
                "jsonRPCAction": {
                    "method": "next_media",
                    "parameters": []
                }
            },
            {
                "title": "prev",
                "subTitle": "Plays previous media if it is available",
                "icoPath": "images/app.png",
                "score": 1,
                "jsonRPCAction": {
                    "method": "prev_media",
                    "parameters": []
                }
            },
            {
                "title": "stop",
                "subTitle": "Stops playing media",
                "icoPath": "images/app.png",
                "score": 1,
                "jsonRPCAction": {
                    "method": "stop_media",
                    "parameters": []
                }
            }
        ]

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

    def open_url(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    Nutils()
