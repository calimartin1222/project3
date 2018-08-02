# Project 3

Web Programming with Python and JavaScript

Description:

This web app is an ordering service for Pinocchio's Pizza & Subs that allows users
to log in or register if they don't have an account, log out, and place orders for
various menu items. Users are also given the ability to customize their order before
they place it, and see the progress of the order (pending or completed) via their
cart after submitting. Restaurant Owners are able to login to the admin page and
change the status of orders and add, delete or change details of menu items.

Note:
This still has some bugs in it. I ran out of time putting the final touches on this.
I also left all the commenting for the end, which I probably shouldn't have done,
because I didn't have the time to comment as thoroughly as I wanted.

File Descriptions:

Account App:

account/static/account/menu.js - javascript that manipulates the elements on and keeps
track of Events on the order.html page

account/static/account/style.css - makes a couple elements more aesthetically pleasing

account/templates/account/index.html - the page the user is brought to when they login;
a simple welcome page

account/templates/account/directions, hours, sicilianVSreg, contact.html - these are
multiple html pages that just extend base.html and display simple information taken
from Pinocchio's website

account/templates/account/login.html - shows user login form

account/templates/account/logout.html - logs the user out and shows user a goodbye message

account/templates/account/registerForm.html - shows user registration form

account/templates/account/base.html - base template all html files extend from;
includes banner, navbar, and basic page body setup

account/admin.py - logs all the models to be accessed via /admin

account/forms.py - pesonalized forms extending django registration and login forms

account/models.py - user database set up

account/urls.py - sets up url paths

account/views.py - defines functions that are called in urls.py when the user visits certain urls

Orders App:

orders/templates/orders/cart.html - shows user's cart

orders/templates/orders/index.html - actual homepage of the web app

orders/templates/orders/order.html - shows user ordering form

orders/admin.py - logs all the models to be accessed via /admin

orders/models.py - Order, toppings and menu_item database set up

orders/urls.py - sets up url paths

orders/views.py - defines functions that are called in urls.py when the user visits certain urls