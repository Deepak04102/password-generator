import random
import string

def generate_password(length, complexity):
    characters = string.ascii_letters 
    if complexity > 1:
        characters += string.digits  
    if complexity > 2:
        characters += string.punctuation 

    if length < 1:
        raise ValueError("Password length must be at least 1")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        complexity = int(input("Enter the complexity level (1 for letters, 2 for letters and digits, 3 for letters, digits, and special characters): "))
        
        if complexity < 1 or complexity > 3:
            raise ValueError("Complexity level must be between 1 and 3")
        
        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
