import qrcode
img = qrcode.make(' https://www.premierleague.com/tables')
img.save('premierleague.png')
