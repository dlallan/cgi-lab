# Lab 3 - Common Gateway Interface

## Question 1: How do you inspect all environment variables in Python?
All environment variables are available in Python with `os.environ`. Particular environment variables can be retrieved with `os.getenv()`.

## Question 2: What environment variable contains the query parameter data?
The QUERY_STRING environment variable contains the query parameter data.

## Question 3: What environment variable contains information about the user’s browser?
The HTTP_USER_AGENT environment variable contains information about the user's browser.

## Question 4: How does the POSTed data come to the CGI script?
The POST data is available via `cgi.FieldStorage.getfirst()`.

## Question 5: What is the HTTP header syntax to set a cookie from the server?
The server can set a cookie from the browser via `cookie = SimpleCookie(os.environ["HTTP_COOKIE"])` and using `cookie.get()` to retrive cookies by name.

## Question 6: What is the HTTP header syntax the browser uses to send the cookie back?
From the server, calling `print("Set-Cookie: name=value")` will send a cookie with name `name` and value `value` back to the browser.

## Question 7: In your own words, what are cookies used for?
Cookies are a way to maintain state between a client and a server. Since they persist on disk, a server can keep track of a client over subsequent visits. For example, a browser-based game could store cookies to save the user's progress over time. Deleting the cookies would effectively erase the user's progress.

## Question 8: What is the link to your code on GitHub?
https://github.com/dlallan/cgi-lab
