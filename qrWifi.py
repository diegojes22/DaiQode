# Libraries
from enum import Enum
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Classes
class SecurityTypes(Enum):
    '''Tipos de seguridad para la conexión WiFi.'''
    WPA : str = "WPA"
    WEP : str = "WEP"
    NOPASS : str = "nopass"

class QrWiFi:
    '''Class to represent a WiFi network and generate its QR code.'''

    # Constructor method
    def __init__(self, ssid : str, password : str = '', security : str = SecurityTypes.WPA.value):
        '''Constructor. Initializes the QrWiFi class with the provided parameters.'''
        self.ssid : str = ssid
        self.password : str = password
        self.security : str = security  # WPA, WPA2, WEP o nopass

        self.icon : Image.Image = None
        self._make_qr()

    # Setters
    def set_icon(self, icon_path: str):
        '''Set the icon for the WiFi QR code.'''
        if(self.qr is None):
            return
        # Try open and append a icon
        try:
            self.icon = Image.open(icon_path).convert("RGBA") #open

            # Resize icon
            width, height = self.qr.size
            icon_size = width // 4
            self.icon = self.icon.resize((icon_size, icon_size), Image.LANCZOS)

            # Paste icon
            pos = ((width - icon_size) // 2, (height - icon_size) // 2)
            self.qr.paste(self.icon, pos, mask=self.icon if self.icon.mode == 'RGBA' else None)
        except Exception as e:
            print(f"Error to load icon: {e}")
            self.icon = None

    def get_qr_code(self):
        '''Get the QR code image.'''
        return self.qr

    def _make_qr(self):
        '''Generate the QR code for the WiFi network.'''
        wifi_text : str = f"WIFI:T:{self.security};S:{self.ssid};P:{self.password};;"
        self.qr = qrcode.make(wifi_text)

class WiFiCard:
    '''Class to represent a WiFi card.'''

    # Constructor method
    def __init__(self, source: QrWiFi):
        self.source = source

    def set_font(self, font: str):
        '''Set the font for the WiFi card.'''
        self.font = font

    def set_bottom_logo(self, logo_path: str):
        '''Set the bottom logo for the WiFi card.'''
        try:
            self.logo = Image.open(logo_path).convert("RGBA")
        except Exception as e:
            print(f"Error to load logo: {e}")
            self.logo = None

    def draw(self) -> Image.Image:
        '''Draw the WiFi card and return a Image.'''

        # prepare qr and image
        qr = self.source.get_qr_code().resize((190, 190))
        img = Image.new("RGB", (400, 200), "#ffffff")

        # draw the card
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 0, 399, 199], fill=None, outline="#007eff", width=5)
        draw.rectangle([0, 0, 399, 199], fill=None, outline="#151515", width=1)

        img.paste(qr, (5, 5))

        # draw text
        main_font = self.new_font(font=self.font, size=20)
        tag_font = self.new_font(font=self.font, size=14)

        draw.text((200, 10), "WiFi:", fill="#007eff", font=tag_font)                # WiFi SSID
        draw.text((200, 30), f"{self.source.ssid} ", fill="black", font=main_font)
        draw.text((200, 70), "Contraseña", fill="#007eff", font=tag_font)           # Password
        draw.text((200, 90), f"{self.source.password}", fill="black", font=main_font)

        # paste logo in bottom right
        if self.logo:
            self.logo = self.logo.resize((self.logo.width//2, self.logo.height//2), Image.LANCZOS)
            img.paste(self.logo, (290, 150), mask=self.logo)

        return img

    def new_font(self, font: str = "arial.ttf", size: int = 18) -> ImageFont.FreeTypeFont:
        '''Create a new font instance for the WiFi card.'''
        try:
            return ImageFont.truetype(font, size)

        except Exception as e:
            print(f"Error to load font {font}: {e}")
            return ImageFont.load_default()