import requests
import os
import random
import string
import json
import time

# COMPONENTS
import creditCardGenerator

def firstnameGenerator(names):
  """
  @params:    names     list of string
  @return:    string    Random firstname from list
  """
  return random.choice(names).lower()

def lastnameGenerator(names):
  """
  @params:    names     list of string
  @return:    string    Random lastname from concatenation of two names from list
  """
  return random.choice(names)[0:3].lower() + random.choice(names)[3:].lower()

def emailAddressGenerator(firstname, lastname, domain):
  """
  @params:    firstname     string
  @params:    lastname      string
  @params:    domain        list of string
  @return:    string        email address made from firstname, lastname and domain
  """

  key = random.choice([0, 1, 2, 3])
  if key == 0:
    # x-last@domaim.xyz
    return firstname[0] + "-" + lastname[0:3] + random.choice(domain)
  elif key == 1:
    # firstname.lastname@domaim.xyz
    return firstname + "." + lastname + random.choice(domain)
  elif key == 2:
    # x.lastname@domaim.xyz
    return firstname[0] + "." + lastname + random.choice(domain)
  elif key == 3:
    # firstnameH4E@domain.xyz
    name_extra = "".join(random.choice(string.digits))
    return firstname + name_extra + random.choice(domain)
  
def passwordGenerator(length=10):
  """
  @params:    length    int, optional
  @return:    string    Random password of size = length
  """
  chars = string.ascii_letters+ string.digits + "!@#$%^&*()"
  random.seed = os.urandom(1024)
  return "".join(random.choice(chars) for i in range(length))

def creditCard():
  """
  @return:    string    Random credit card number
  """
  return creditCardGenerator.generate_card(random.choice(["visa16", "mastercard", "discover"]))

def expirationDateGenerator():
  """
  @return:    string    Random expiration date
  """
  return str(random.randrange(1, 13)) + "/" + str(random.randrange(20, 23))

def cvvGenerator():
  """
  @return:    string    Random cvv number
  """
  return str(random.randrange(100, 1000))

def dobGenerator():
  """
  @return:    string    Random date of birth
  """
  return str(random.randrange(1, 30)) + "/" + str(random.randrange(1, 13)) + "/" + str(random.randrange(1970, 2010))

def addressGenerator(names):
  """
  @params:    names     list of string
  @return:    string    Random city name from concatenation of two names from list
  """
  streetName = lastnameGenerator(names)
  return random.choice(["Rue", "Cours", "Boulevard", "Avenue", "Impasse", "Chemin"]) + " " + streetName


 # Names list (1000)
names = json.loads(open("names.json").read())
# Emails domain
domainList = ["@gmail.com", "@gmail.fr", "@outlook.com", "@outlook.fr", "@laposte.net", "@wanadoo.fr", "@live.fr"]

def completeUserGenerator():
  """
  @return:    object    False user created from names list with following fields:
    {"user"
    "pass"
    "prenom"
    "nom"
    "carte"
    "exp"
    "cvv"
    "dob"
    "address"
    "city"
    "zip"}
  """

  firstname = firstnameGenerator(names)
  lastname = lastnameGenerator(names)

  return {
    "user": emailAddressGenerator(firstname, lastname, domainList),
    "pass": passwordGenerator(),
    "prenom": firstname,
    "nom": lastname,
    "carte": creditCard(),
    "exp": expirationDateGenerator(),
    "cvv": cvvGenerator(),
    "dob": dobGenerator(),
    "address": addressGenerator(names),
    "city": lastnameGenerator(names),
    "zip": round(random.randrange(10000, 99000), -2)
  }


def sendFalseUser(urls):
  """
  @params:    urls      list of string
  """

  falseUser = completeUserGenerator()

  # Send fake user to the fuckers
  requests.post(urls[0], allow_redirects=False, data={
    "user": falseUser["user"],
    "pass": falseUser["pass"]
  })

  requests.post(urls[1], allow_redirects=False, data={
    "prenom": falseUser["prenom"],
    "nom": falseUser["nom"],
    "carte": falseUser["carte"],
    "exp": falseUser["exp"],
    "cvv": falseUser["cvv"]
  })

  requests.post(urls[2], allow_redirects=False, data={
    "prenom": falseUser["prenom"],
    "nom": falseUser["nom"],
    "dob": falseUser["dob"],
    "address": falseUser["address"],
    "city": falseUser["city"],
    "zip": falseUser["zip"]
  })

  print("User {user} sent...".format(user=falseUser["user"]))




urls = [
  "https://bnp-paribas.wpmudev.host/wp-content/connexion-netf.php",
  "https://bnp-paribas.wpmudev.host/wp-content/carte-netf.php",
  "https://bnp-paribas.wpmudev.host/wp-content/bill-netf.php"
]


for n in range(1000):
  if n % 100 == 0:
    print()
    print("===== {n} =====".format(n=n))

  sendFalseUser(urls)





