import qrcode


encoder = qrcode.QRCode(version = 3)
encoder.add_data('AI Search')
img = encoder.make_image(fill_color = 'white', back_color = 'blue')
img.show()
img.save('QR.jpg')
