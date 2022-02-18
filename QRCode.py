# Import QRCode from pyqrcode
import pyqrcode
#: import png

# String which represents the QR code
s = "https://correctmycode.in"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale=8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale=6)
