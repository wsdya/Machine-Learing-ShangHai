import base64

import requests


def get_code(img_data):
    url = 'http://api2.sz789.net:88/RecvByte.ashx'
    data = {
        'username': "y1317407749",
        "password": "12345678",
        "softId": '73522',
        "imgdata": img_data
    }
    response = requests.post(url, data=data)
    print(response.text)


if __name__ == '__main__':
    with open('D:/1.jpg', 'rb') as a:
        data = a.read()
        print(data)
        data = base64.b64decode(data)
        print(data)

        get_code(data)
