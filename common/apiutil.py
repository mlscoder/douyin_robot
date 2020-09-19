# -*- coding: UTF-8 -*-
import base64
import requests


def setParams(array, key, value):
    array[key] = value


class AiPlatImage(object):
    def __init__(self, ak, sk):
        self.ak = ak
        self.sk = sk
        self.data = {}
        self.url_data = ''

    def getAccessToken(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + self.ak + '&client_secret=' + self.sk
        response = requests.get(host)
        if response:
            return response.json()['access_token']

    def invoke(self, params):
        request_url_pre = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
        token = self.getAccessToken()
        request_url = request_url_pre + "?access_token=" + token
        headers = {'content-type': 'application/json'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            print(response.json())
            return response.json()

    def face_detectface(self, image):
        setParams(self.data, 'image_type', 'BASE64')
        setParams(self.data, 'face_field', 'age,gender,beauty,expression')
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data.decode("utf-8"))

        return self.invoke(self.data)


class AiPlatWord(object):
    def __init__(self, ak, sk):
        self.ak = ak
        self.sk = sk
        self.data = {}
        self.url_data = ''

    def getAccessToken(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + self.ak + '&client_secret=' + self.sk
        response = requests.get(host)
        if response:
            return response.json()['access_token']

    def invoke(self, params):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
        # 二进制方式打开图片文件

        access_token = self.getAccessToken()
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            if "广告" in response.text:
                return True
            else:
                return False

    def ad_detectface(self, image):
        image_data = base64.b64encode(image)
        setParams(self.data, 'image', image_data.decode("utf-8"))
        return self.invoke(self.data)
