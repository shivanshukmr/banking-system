# colour, fonts and images to be used
# save all images in assets
from PIL import ImageTk, Image  # needed to execute png, jpeg type files

colour_title = "#0859c6"  # colour to be used for the title frame background
font_title = "White"  # default title font colour
colour = "#87ceeb"  # default main frame background colour
font_c = "#000000"  # default font colour that would be used in the window
box = "#badbff"  # default textbox colour that would be used in the window
icon = "banking-system\src\gui\Assets\images\icon2.ico"  # icon of the window (15x15, 32x32 or 64x64), nedds to be in .ico form
bankcli_asciiart = ImageTk.PhotoImage(
    Image.open("banking-system\src\gui\Assets\images\logo.jpg")
)  # bankname image
