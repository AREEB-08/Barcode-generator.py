
import qrcode
from PIL import Image, ImageDraw, ImageFont

# User input for the link to generate the QR code
link = input("Enter the link you want to create a QR code for: ")

# Create a QR Code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=8,
    border=3,
)
