# colour, fonts and images to be used
# save all images in assets
from PIL import ImageTk, Image  # needed to execute png, jpeg type files

colour = "#0859c6"  # colour to be used for the background
font_c = "White"  # default font colour that would be used in the window
box = "#badbff"  # default textbox coour that would be used in the window
icon = "banking-system\src\core\images\icon.ico"  # icon of the window (15x15, 32x32 or 64x64), nedds to be in .ico form
bankcli_asciiart = ImageTk.PhotoImage(
    Image.open("banking-system\src\core\images\logo.png")
)  # bankname image
