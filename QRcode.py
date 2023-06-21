import qrcode

input_URL_linkedIn = "https://www.linkedin.com/in/mickael-maujean-992932bb/"
input_URL_github = "https://github.com/MickaelMaujean"


qr1= qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr2= qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr1.add_data(input_URL_linkedIn)
qr1.make(fit=True)
qr2.add_data(input_URL_github)
qr2.make(fit=True)

img1 = qr1.make_image(fill_color="blue", back_color="white")
img1.save("qrcode_linkedin.png")
img2 = qr2.make_image(fill_color="black", back_color="white")
img2.save("qrcode_github.png")