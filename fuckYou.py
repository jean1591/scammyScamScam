import requests
import os
import random
import string
import json

# Fake password
chars = string.ascii_letters+ string.digits + "!@#$%^&*()"
random.seed = os.urandom(1024)

# Emails domain
emailsDomain = ["@gmail.com", "@gmail.fr", "@outlook.com", "@outlook.fr", "@laposte.net", "@wanadoo.fr"]

# URL of the fuckers
url = "https://utilesupportonline.serveirc.com/connexion/info/serv5201.php?enc=ac888a0be0f73d8fa575424feaca2b4c&p=0&dispatch=796063080bb0c5ec75749ad7b13cfa2744082e49"

# Names list (1000)
names = json.loads(open("names.json").read())

print(len(names), "fake users ready to be send...")

for name in names:
  # Create fake username - format = name + digit + email domain
  name_extra = "".join(random.choice(string.digits))
  username= name.lower() + name_extra + random.choice(emailsDomain)

  # Create fake password
  password = "".join(random.choice(chars) for i in range(10))

  # Send fake user to the fuckers
  requests.post(url, allow_redirects=False, data={
    "mail": username,
    "pass": password

  })

  print(">>> Sending", username, password, "...")

print(len(names), "fake users sent...")