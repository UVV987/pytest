import requests

class Form:
    def __init__(self, login, password, email="info@mail.ru", url="https://itproger.com"):
        self.login = login
        self.password = password
        self.email = email
        self.url = url

    def set_web_url(self, url):
        headers = {
            'accpt': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
        }

        session = requests.Session()
        try:
            req = session.get(url, headers=headers)
            if req.status_code == 200:
                return "True"
            else:
                return "False"
        except Exception:
                return "False"

form = Form("Admin", "qwerty")
form2 = Form("Modest", "qwerty123", "info@mail.ru", "https://itproger.com")
print(form.set_web_url("https://itproger.com"))
