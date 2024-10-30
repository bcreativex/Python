import qrcode

def generate_qr(data, filename="qrcode.png"):
    qr = qrcode.make(data)
    qr.save(filename)
    print(f"QR Code saved as {filename}")

if __name__ == "__main__":
    text = input("Enter data for QR code: ")
    generate_qr(text)
