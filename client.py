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
    IF_NONE_MATCH = 'W/"39-ecMKyjU/fhuUBv4JoLNnlATwSM0"'

    def __init__(self):
        self.__session_id = '5b1bdc9538ded657352567f1:36d497a9-78ab-4d55-a586-2961aaa169dd'

    def get_ticket_id(self, qr: str) -> str:
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
            'If-None-Match': self.IF_NONE_MATCH,
            'clientVersion': self.CLIENT_VERSION,
            'Accept-Language': self.ACCEPT_LANGUAGE,
            'sessionId': self.__session_id,
            'User-Agent': self.USER_AGENT,
        }

        resp = requests.post(url, json=payload, headers=headers, verify=False)

        return resp.json()["id"]

    def get_ticket(self, ticket_id: str) -> dict:
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
        }

        resp = requests.get(url, headers=headers, verify=False)

        return resp.json()


if __name__ == '__main__':
    client = NalogRuPython()
    qr_code = "t=20200727T1117&s=4850.00&fn=9287440300634471&i=13571&fp=3730902192&n=1"
    ticket_id = client.get_ticket_id(qr_code)
    ticket = client.get_ticket(ticket_id)
    print(json.dumps(ticket, indent=4))
