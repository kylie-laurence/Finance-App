import qrcode

url = "https://your-streamlit-app-url.com"

qr = qrcode.make(url)
qr.save("app_qr.png")

print("QR code saved as app_qr.png")
