import json

import requests

class NalogRuPython:
    HOST = 'irkkt-mobile.nalog.ru:8888'
    DEVICE_OS = 'iOS'
    CLIENT_VERSION = '2.9.0'
    DEVICE_ID = '7C82010F-16CC-446B-8F66-FC4080C66521'
    ACCEPT = '*/*'
    USER_AGENT = 'billchecker/2.9.0 (iPhone; iOS 13.6; Scale/2.00)'
    ACCEPT_LANGUAGE = 'ru-RU;q=1, en-US;q=0.9'
    CLIENT_SECRET = 'IyvrAbKt9h/8p6a7QPh8gpkXYQ4='
    OS = 'Android'

    def __init__(self):
        self.__session_id = None
        self.set_session_id()

    def set_session_id(self) -> None:
        """
        Authorization using phone and SMS code
        """
        self.__phone = str(input('Input phone in +70000000000 format: '))

        url = f'https://{self.HOST}/v2/auth/phone/request'
        payload = {
            'phone': self.__phone,
            'client_secret': self.CLIENT_SECRET,
            'os': self.OS
        }
        headers = {
            'Host': self.HOST,
            'Accept': self.ACCEPT,
            'Device-OS': self.DEVICE_OS,
            'Device-Id': self.DEVICE_ID,
            'clientVersion': self.CLIENT_VERSION,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'User-Agent': self.USER_AGENT,
        }

        resp = requests.post(url, json=payload, headers=headers)

        self.__code = input('Input code from SMS: ')

        url = f'https://{self.HOST}/v2/auth/phone/verify'
        payload = {
        'phone': self.__phone,
        'client_secret': self.CLIENT_SECRET,
        'code': self.__code,
        "os": self.OS
        }

        resp = requests.post(url, json=payload, headers=headers)

        self.__session_id = resp.json()['sessionId']
        self.__refresh_token = resp.json()['refresh_token']

    def refresh_token_function(self) -> None:
        url = f'https://{self.HOST}/v2/mobile/users/refresh'
        payload = {
            'refresh_token': self.__refresh_token,
            'client_secret': self.CLIENT_SECRET
        }

        headers = {
            'Host': self.HOST,
            'Accept': self.ACCEPT,
            'Device-OS': self.DEVICE_OS,
            'Device-Id': self.DEVICE_ID,
            'clientVersion': self.CLIENT_VERSION,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'User-Agent': self.USER_AGENT,
        }

        resp = requests.post(url, json=payload, headers=headers)

        self.__session_id = resp.json()['sessionId']
        self.__refresh_token = resp.json()['refresh_token']

    def _get_ticket_id(self, qr: str) -> str:
        """
        Get ticker id by info from qr code
        :param qr: text from qr code. Example "t=20200727T174700&s=746.00&fn=9285000100206366&i=34929&fp=3951774668&n=1"
        :return: Ticket id. Example "5f3bc6b953d5cb4f4e43a06c"
        """
        url = f'https://{self.HOST}/v2/ticket'
        payload = {'qr': qr}
        headers = {
            'Host': self.HOST,
            'Accept': self.ACCEPT,
            'Device-OS': self.DEVICE_OS,
            'Device-Id': self.DEVICE_ID,
            'clientVersion': self.CLIENT_VERSION,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'sessionId': self.__session_id,
            'User-Agent': self.USER_AGENT,
        }

        resp = requests.post(url, json=payload, headers=headers)

        return resp.json()["id"]

    def get_ticket(self, qr: str) -> dict:
        """
        Get JSON ticket
        :param qr: text from qr code. Example "t=20200727T174700&s=746.00&fn=9285000100206366&i=34929&fp=3951774668&n=1"
        :return: JSON ticket
        """
        ticket_id = self._get_ticket_id(qr)
        url = f'https://{self.HOST}/v2/tickets/{ticket_id}'
        headers = {
            'Host': self.HOST,
            'sessionId': self.__session_id,
            'Device-OS': self.DEVICE_OS,
            'clientVersion': self.CLIENT_VERSION,
            'Device-Id': self.DEVICE_ID,
            'Accept': self.ACCEPT,
            'User-Agent': self.USER_AGENT,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'Content-Type': 'application/json'
        }

        resp = requests.get(url, headers=headers)

        return resp.json()


if __name__ == '__main__':
    client = NalogRuPython()
    qr_code = "t=20200709T2008&s=7273.00&fn=9282440300688488&i=14186&fp=1460060363&n=1"
    ticket = client.get_ticket(qr_code)
    print(json.dumps(ticket, indent=4, ensure_ascii=False))

    client.refresh_token_function()
    qr_code = "t=20200924T1837&s=349.93&fn=9282440300682838&i=46534&fp=1273019065&n=1"
    ticket = client.get_ticket(qr_code)
    print(json.dumps(ticket, indent=4, ensure_ascii=False))