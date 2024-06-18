import random
import string

def generate_password(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Example usage:
password_length = 10
generated_password = generate_password(password_length)
print(f"Generated Password: {generated_password}")
