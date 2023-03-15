# alacritty-conf-gen
A WIP configuration file generator for Alacritty, written in Python 3.
I didn't want to install npm just for https://github.com/rajasegar/alacritty-themes
The point of this thing is to make it easy to create a very basic alacritty config (and for me to practice programming in python, of course)

TODO:
  -add support for color schemes (just like alacritty-themes)
    >somehow I need to get a list of available themes in a separate directory, probably something like ~/.config/alacritty/themes
    >likely going to copy that from the original alacritty-themes repository, or get my own collection of themes
  -add advanced configuration mode with extra options
    >might be pointless since advanced users can just edit the configuration file directly
