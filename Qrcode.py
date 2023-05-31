import qrcode
img = qrcode.make(' https://www.allsvenskan.se/tabell')
img.save('Allsvenskan.png')
