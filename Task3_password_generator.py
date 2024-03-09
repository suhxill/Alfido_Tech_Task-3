import random

def generate_password(length):
  """
  Generates a random password of the specified length.

  Args:
    length: The desired length of the password.

  Returns:
    A random password string.
  """


  # Define the characters that can be used in the password.
  characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

  # Generate a random password.
  password = ""
  for i in range(length):
    password += random.choice(characters)

  # Return the password.
  return password

# Get the desired password length from the user.
length = int(input("Enter the desired password length: "))

# Generate a random password.
password = generate_password(length)

# Print the password.
print("Your random password is:", password)
