#!/usr/bin/env python3
import cgi
import cgitb
from http.cookies import SimpleCookie
import secret
import templates
import os

cgitb.enable()

s = cgi.FieldStorage()
username = s.getfirst("username")
password = s.getfirst("password")

form_credentials_match_secret = username == secret.username and password == secret.password

cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = cookie_password = None
client_cookie_username = cookie.get("username")
client_cookie_password = cookie.get("password")
if client_cookie_username:
    cookie_username = client_cookie_username.value
if client_cookie_password:
    cookie_password = client_cookie_password.value

cookie_credentials_match_secret = cookie_username == secret.username and cookie_password == secret.password

# override form credentials if cookie values are okay
if cookie_credentials_match_secret:
    username = cookie_username
    password = cookie_password

print("Content-Type: text/html")
if form_credentials_match_secret:
    # update client cookie in case it was stale
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

print()

# render appropriate page
if not (username and password):
    print(templates.login_page())
elif username == secret.username and password == secret.password:
    print(templates.secret_page(username, password))
else:
    print(templates.after_login_incorrect())
