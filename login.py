#!/usr/bin/env python3

import cgi
import cgitb 
cgitb.enable() # for troubleshooting. To send data and receive data. 

from templates import login_page, secret_page, after_login_incorrect
import secret
import os
import http.cookies as SimpleCookie # for cookies

# Create instance of FieldStorage. To get the POSTED data from the form
s = cgi.FieldStorage() #Form's data that we entered
username = s.getfirst("username") #They will look at the form and then see if there is a username and password on the form entered by the user. This form is given in the login_page.
password = s.getfirst("password")

form_ok = username == secret.username and password == secret.password #If the username and password entered by the user is the same as the username and password in the secret.py file (database in future)

#Cookies
cookie = SimpleCookie(os.environ.get("HTTP_COOKIE")) #Get the cookie from the browser
cookie_username = None
cookie_password = None
if cookie.get("username"): #If there is a username in the cookie i.e. if the user has logged in before
    cookie_username = cookie.get("username").value #Get the username from the cookie
if cookie.get("password"): #If there is a password in the cookie i.e. if the user has logged in before
    cookie_password = cookie.get("password").value #Get the password from the cookie

cookie_ok = cookie_username == secret.username and cookie_password == secret.password #If the username and password in the cookie is the same as the username and password in the secret.py file (database in future)
if cookie_ok: #If the cookie is ok, then set the username and password to the cookie's username and password
    username = cookie_username
    password = cookie_password  
  
print("Content-Type: text/html") 
print()
if form_ok: #Shouldnt this be elif (yes because we don't need to check if the form is ok). Can also be done by javascript
    print("Set-Cookie: username={};".format(username)) #Set the cookie's username to the username entered by the user. How does this work?
    print("Set-Cookie: password={};".format(password)) #Set the cookie's password to the password entered by the user

if not username and not password: #If there is anything entered in these fields go to the else clause.
    print(login_page()) # if there is no username or password, then print the login page

elif username == secret.username and password == secret.password: #In our project we will be doing this with a ddatabase entry to validate the entry
    print(secret_page(username, password))

else:
    print(login_page)
    print(f"username: {username}, password: {password}")