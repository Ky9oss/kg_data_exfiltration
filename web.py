import requests
import sys


USERNAME = ""
PASSWORD = ""
API_KEY = ""


def send_to_pastebin(title, contents):
    login_url = "https://pastebin.com/api/api_login.php"
    login_data = {
            'api_dev_key': API_KEY,
            'api_user_name': USERNAME,
            'api_user_password': PASSWORD
            }
    r = requests.post(login_url, data=login_data)
    api_user_key = r.text
    print(f'Get api_user_key: {api_user_key}')

    post_url = "https://pastebin.com/api/api_post.php"
    paste_data = {
            'api_paste_name': title,
            'api_paste_code': contents.decode(),
            'api_dev_key': API_KEY,
            'api_user_key': api_user_key,
            'api_option': 'paste',
            'api_paste_private': 0,
            }
    r = requests.post(post_url, data=paste_data)
    print(r.status_code)
    print(r.text)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python web.py [username] [password] [api_key]")
        sys.exit()
    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    API_KEY = sys.argv[3]
    title = 'TITLE1'
    contents = b"lalalallalallalall"
    send_to_pastebin(title, contents)
