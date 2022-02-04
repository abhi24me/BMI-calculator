import qrcode as qr
from PIL import Image

qrc = qr.QRCode(version=1,
                error_correction=qr.constants.ERROR_CORRECT_H,
                box_size=10,border=4,)
qrc.add_data("https://github.com/abhi24me")
qrc.make(fit=True)
img=qrc.make_image(fill_color="green",back_color="white")
img.save("gitHub_profile.png")
