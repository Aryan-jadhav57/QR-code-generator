import qrcode


# taking upi id as a input
upi_id = input("enter your UPI_ID = ")


# upi://pay?pa=UPI_ID%apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE


# pa = payment jisko karna hai
# pn = recepient name ex aryan
# am = amount dalraheho
# cu = currency
# tn = message after payment



# defining the payment URl based on the UPI iD and the payment app

phonepe_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'
Google_pay_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'


# create QR code for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
Google_pay_qr = qrcode.make(Google_pay_url)


# save the Qr code to the image file(optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
Google_pay_qr.save('Google_pay_qr.png')

# display the QR code ( you need to install PIL/Pillow library)
phonepe_qr.show()
paytm_qr.show()
Google_pay_qr.show()

