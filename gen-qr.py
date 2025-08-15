from qrWifi import QrWiFi, WiFiCard
import pathAdmin

import argparse

# command sintax
# python genCard.py --ssid Wifi --password 1234 --icon wifi_icon.png --save_as out_dir

if(__name__ == '__main__'):
    # get args
    parser = argparse.ArgumentParser(description='Generate a QR code for WiFi credentials.')
    parser.add_argument('--ssid', type=str, required=True, help='The SSID of the WiFi network.')
    parser.add_argument('--password', type=str, required=True, help='The password of the WiFi network.')
    parser.add_argument('--icon', type=str, required=False, help='The path to the icon image file.')
    parser.add_argument('--save_as', type=str, required=False, help='The directory to save the QR code image.')

    args = parser.parse_args()

    # gen qr code
    qr_wifi = QrWiFi(args.ssid, args.password)

    # load icon
    if(args.icon):
        qr_wifi.set_icon(args.icon)

    qr = qr_wifi.get_qr_code()

    # save
    if args.save_as:
        qr.save(args.save_as)
    else:
        qr.save(f"{pathAdmin.get_script_path()}/out/{args.ssid}.png")