'''
This is the beggining of my VPN project in Python. 
Like I said in the description of the repository, I will be attempting this for the first time.
I want to do this for my own sake as well as anyone who is interested in cyber security.
The fact that many companies, governments, and people with malicious intentions are buying and selling your data scares me.
This should also scare you too.

I am going to learn a lot about cybersecurity and networking along the way and I am 100% extitied for this.
I Hope you enjoy as well!!!
'''

# Authors: Nathan Cheonis

import requests

proxies = {
    'https': 'https://52.183.8.192:3128'
}

response = requests.get("https://ipinfo.io/json", proxies = proxies)
print(response.text)