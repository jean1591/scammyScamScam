import requests
import os
import random
import string
import json
import time

def createUsername(key, names, domain):
  if key == 0:
    # x-nam@domaim.xyz
    return random.choice(string.ascii_lowercase) + "-" + names[0:3].lower() + random.choice(domain)
  elif key == 1:
    # surname.name@domaim.xyz
    return random.choice(names).lower() + "." + random.choice(names)[0:3].lower() + random.choice(names)[3:].lower() + random.choice(domain)
  elif key == 2:
    # x.name@domaim.xyz
    return random.choice(names)[0].lower() + "." + random.choice(names)[0:3].lower() + random.choice(names)[3:].lower() + random.choice(domain)
  else:
    name_extra = "".join(random.choice(string.digits))
    return random.choice(names).lower() + name_extra + random.choice(domain)
  
def createPassword(length=10):
  chars = string.ascii_letters+ string.digits + "!@#$%^&*()"
  random.seed = os.urandom(1024)
  return "".join(random.choice(chars) for i in range(length))


# Names list (1000)
names = json.loads(open("names.json").read())

# Emails domain
domain = ["@gmail.com", "@gmail.fr", "@outlook.com", "@outlook.fr", "@laposte.net", "@wanadoo.fr", "@live.fr"]

# URL of the fuckers
url = "https://utilesupportonline.serveirc.com/connexion/info/serv5201.php?enc=ac888a0be0f73d8fa575424feaca2b4c&p=0&dispatch=796063080bb0c5ec75749ad7b13cfa2744082e49"

def sendFake(url):
  username = createUsername(2, names, domain)
  password = createPassword()

  # Send fake user to the fuckers
  requests.post(url, allow_redirects=False, data={
    "mail": username,
    "pass": password
  })

  print(">>> Sending", username, password, "...")

for i in range(1000):
  sendFake(url)
  time.sleep(30)

print(len(names), "fake users sent...")