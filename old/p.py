import qrcode

url = "https://example.com/files/A3-2024-ARID-3766.pdf"
img = qrcode.make(url)
img.save("pdf_qr.png")
