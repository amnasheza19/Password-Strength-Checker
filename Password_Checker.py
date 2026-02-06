import math
import string

def calculate_entropy(password):
    charset = 0
    
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def check_strength(password):
    entropy = calculate_entropy(password)
    suggestions = []

    if len(password) < 8:
        suggestions.append("Use at least 8–12 characters")
    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letters")
    if not any(c.islower() for c in password):
        suggestions.append("Add lowercase letters")
    if not any(c.isdigit() for c in password):
        suggestions.append("Include numbers")
    if not any(c in string.punctuation for c in password):
        suggestions.append("Add special symbols (!@#$ etc)")

    if entropy < 40:
        strength = "Weak 🔴"
    elif entropy < 70:
        strength = "Medium 🟡"
    else:
        strength = "Strong 🟢"

    return entropy, strength, suggestions

def main():
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")

    entropy, strength, suggestions = check_strength(password)

    print("\n--- Result ---")
    print(f"Entropy Score: {entropy}")
    print(f"Strength: {strength}")

    if suggestions:
        print("\nSuggestions to improve:")
        for s in suggestions:
            print(f"- {s}")
    else:
        print("\nExcellent password! 💪")

if __name__ == "__main__":
    main()
