import os
import requests


def find_home():
    homedir = os.environ['HOME']
    return homedir


def check_config_folder():
    homedir = find_home()
    if not os.path.exists(f"{homedir}/.config/alacritty"):
        #  os.makedirs(f"{homedir}/.config/alacritty"
        return False
    else:
        return True


def create_config_folder():
    homedir = find_home()
    if not check_config_folder():
        os.makedirs(f"{homedir}/.config/alacritty")
    #  check if it actually worked
    if check_config_folder():
        print("ok")
        return True
    else:
        print("failed to create config folder")
        return False


def create_config_file():
    url = "https://raw.githubusercontent.com/alacritty/alacritty/master/alacritty.yml"
    homedir = find_home()
    base_config = requests.get(url)
    f = open(f"{homedir}/.config/alacritty/alacritty.yml", "w", encoding="utf8")
    f.write(str(base_config.text))
    f.close()
    if not os.path.exists(f"{homedir}/.config/alacritty/alacritty.yml"):
        return False
    else:
        return True


def prime():
    if create_config_folder():
        create_config_file()
        return True
    else:
        return False
