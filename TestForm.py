from form import Form

form = Form('login', 'password')

def test_add():
    assert form.login == 'login'
    assert form.password == 'password'

def test_set_form():
    form = Form('login', 'password', 'email', 'url')
    assert form.login == 'login'
    assert form.password == 'password'
    assert form.email == 'email'
    assert form.url == 'url'

def test_set_web_url():
    result = form.set_web_url("https://itproger.com")
    assert result == 'True'
    result = form.set_web_url("https://itproger.com")
    assert result == 'False'
