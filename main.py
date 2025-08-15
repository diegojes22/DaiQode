# libraries
from qrWifi import QrWiFi, WiFiCard
import pathAdmin
import random

from otherData import myvars

# Variables
wifiSSID : list[str] = []
wifiPassword : list[str] = []

main_wifi_keyword = myvars.my_main_wifi_keyword

# functions
def gen_random_wifi(wifis: list[str], passwords: list[str], main_keyword: str = main_wifi_keyword):
    '''Generate a random WiFi QR code.'''
    ssid = f"{main_keyword}_{random.randint(1000, 9999)}"
    password = '123456780-qwertyuiopasdfghjklzxcvbnm_/()' # character for a random password

    password = ''.join(random.sample(password, len(password)))
    password = password[:random.randint(10, 14)]  # Ensure password is between 10 and 14 characters long

    wifis.append(ssid)
    passwords.append(password)

# generate list
for i in range(30):
    gen_random_wifi(wifiSSID, wifiPassword, main_wifi_keyword)

for ssid, password in zip(wifiSSID, wifiPassword):
    print(f"SSID: {ssid}, Password: {password}")

# gen qr
print("\nGenerating random WiFi QR codes...")
path :str = pathAdmin.get_script_path()

for ssid, password in zip(wifiSSID, wifiPassword):
    qr_wifi : QrWiFi = QrWiFi(ssid, password)
    qr_wifi.set_icon(myvars.my_wifi_icon)

    img = qr_wifi.get_qr_code()

    card : WiFiCard = WiFiCard(qr_wifi)
    card.set_bottom_logo(myvars.my_logo)
    card.set_font(myvars.my_font)
    card.draw().save(f"{path}/out/{ssid}.png")

    
