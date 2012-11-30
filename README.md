======
LaundryList
======

LaundryList is a web app to help you keep track of your clothes and 
determine which were worth their cost.

Requirements
------
MongoDB
pymongo
Flask, including WTForms extension

Server
------
To start a server, must have an instance of MongoDB running in the background. Then, 
```
$ python laundry.py
```
Navigate in a browser to localhost:5000/closet to add items to your closet and
begin analyzing your clothes.
