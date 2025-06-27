import random
import string

length = int(input("Enter password length: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(chars, k=length))
print("Generated Password:", password)

