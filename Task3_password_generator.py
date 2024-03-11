import random

def generate_password(length):
  """
  Generates a random password of the specified length.

  Args:
    length: The desired length of the password.

  Returns:
    A random password string.
  """

  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

  password = ""
  for i in range(length):
    password += random.choice(characters)

  return password

length = int(input("Enter the desired password length: "))

password = generate_password(length)


print("Your random password is:", password)
