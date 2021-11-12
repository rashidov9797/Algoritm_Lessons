import qrcode as qr
import  image as img

qr.QRCode(
  version=16,
  box_size=10,
  border=5
)


data_link="https://github.com/rashidov9797"
# my github portfolio link
qr.add_data(data_link)
qr.make(fir=True)
img=qr.make_image(fill='black',back_color='white')
img.save('test.png')