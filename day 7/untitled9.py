# Create a new Code Challenge to POST data 

# Research the below wesbite and post some data on it

# https://requestbin.com



import requests

Host = "https://enrjgcqhm9yu8.x.pipedream.net"

data = {"firstname":"dev","language":"English"}


def post_method():
    response = requests.post(Host,data)
    return response

print ( post_method().text )

