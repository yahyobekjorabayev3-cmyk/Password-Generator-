import secrets
import string

def generate_password(length=16):
    letters = string.ascii_lowercase
    all_characters = letters + string.ascii_uppercase + string.digits + string.punctuation

    # Ensure the password has at least one of each character type
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
        
    # Fill the rest of the password length
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(secrets.choice(all_characters))
        
    # Shuffle to prevent predictable patterns
    secrets.SystemRandom().shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    print("--- Secure Password Generator ---")
    try:
        user_input = input("Enter password length (minimum 8) [Default: 16]: ")
        length = int(user_input) if user_input else 16
        if length < 8:
            print("[!] Length too short. Setting to minimum 8 characters.")
            length = 8
    except ValueError:
        print("[!] Invalid input. Setting to default 16 characters.")
        length = 16

    new_password = generate_password(length=length)
    print(f"\nYour secure password is:\n👉 {new_password} 👈\n")

