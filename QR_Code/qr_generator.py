import qrcode

#Ask user fro website url to generate qr code
data= input("Enter the text or URL to generate QR code:")

#Create a qr code 
qr= qrcode.make(data)

#save the qr code image
qr.save("My_qycode.png")

print("QR Code generated and saved successfully")



