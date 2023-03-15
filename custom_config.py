import os


def check_if_config_exists():
    homedir = os.environ["HOME"]
    if os.path.exists(f"{homedir}/.config/alacritty/alacritty.yml"):
        return True
    else:
        return False


def set_font_options():
    homedir = os.environ["HOME"]
    if check_if_config_exists():
        print("###Customize alacritty.yml file (input will be appended to the end of the original file)")
        print("Case sensitive!")
        fontsize = int(input("Font size to be used (integer): "))
        fontfamily = input("Font family [case sensitive!] (e.g. IBM Plex Mono, leave empty for default): ")
        fontstyle = ""
        if fontfamily:
            fontstyle = input("Font style (e.g. Regular, Bold): ")
        f = open(f"{homedir}/.config/alacritty/alacritty.yml", "a", encoding="utf8")
        if fontfamily:
            f.write(f"font:\n  normal:\n    family: {fontfamily}\n    style: {fontstyle}\n  size: {fontsize}")
        else:
            f.write(f"font:\n  size: {fontsize}")
    else:
        print("The config file doesn't exist!")


def color_scheme():

