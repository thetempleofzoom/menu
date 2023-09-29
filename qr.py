import qrcode
# make sure to install 'pillow' as well whihc works in b/g

# for local server. when deployed online, replace
# this is website to open when qr code is scanned
image = qrcode.make('https://127.0.0.1/8000')
image.save('qr.png')
