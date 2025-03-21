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

# Add user-provided link to the QR code
qr.add_data(link)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Create a new image with added height for the text
width, height = img.size
text = input("Enter the text you want to add below the QR code: ")
text_color = input("Enter the text color (e.g., 'black', '#FF5733'): ")
font_size = int(input("Enter the font size you want for the text: "))
new_height = height + 70  # Increase height for the text
new_img = Image.new('RGB', (width, new_height), 'white')
new_img.paste(img, (0, 0))

# Draw the text
draw = ImageDraw.Draw(new_img)

# Load a custom font or default to a basic one
try:
    font_path = "arial.ttf"  # Change this to the path of your .ttf file
    font = ImageFont.truetype(font_path, font_size)
except IOError:
    print("Custom font not found. Using default font.")
    font = ImageFont.load_default()

# Calculate text dimensions
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]  # right - left
text_height = text_bbox[3] - text_bbox[1]  # bottom - top

text_x = (width - text_width) // 2
text_y = height + 10  # Position the text below the QR code

# Draw the text in the specified color
draw.text((text_x, text_y), text, fill=text_color, font=font)

# Save the image with a custom filename
custom_filename = input("Enter the filename to save the QR code (without extension): ")
filename = f"{custom_filename}.png"
new_img.save(filename)

print(f"✅ QR code saved as '{filename}' with the text below.")
