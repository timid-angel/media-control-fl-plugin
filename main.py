"""
This is the entry point to the application.
 - It imports the MediaControl class from the plugin module and initializes it.
 - It adds the plugin and lib directories to the system path to load the modules in `requirements.txt` locally.
"""
import sys
import os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from plugin import MediaControl

if __name__ == "__main__":
    MediaControl()
