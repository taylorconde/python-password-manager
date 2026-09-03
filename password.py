import random
import string

def strong_password():
  characters = string.ascii_letters + string.digits + string.punctuation
  pass_len = random.randint(14,18)
  new_pass = random.sample(characters, k=pass_len)
  password = "".join(new_pass)
  return password