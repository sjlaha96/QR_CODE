import qrcode as qr
import PIL
from PIL import Image

qr_code_func=qr.QRCode(box_size=9, border=3)

qr_code_func.add_data("https://www.linkedin.com/in/subhajit-laha/")

img=qr_code_func.make_image(fill_color="red",back_color="yellow")
img.save("linkedin_sl.png")

print("Code generated successfully")