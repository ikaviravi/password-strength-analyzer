# password_tool.py
from zxcvbn import zxcvbn
import itertools
import datetime

# -------------------------------
# Function 1: Analyze password strength
# -------------------------------
def analyze_password_strength(password):
    result = zxcvbn(password)
    print("\n🔒 Password Strength Analysis:")
    print(f"Score (0=weak, 4=strong): {result['score']}")
    print(f"Estimated crack time: {result['crack_times_display']['offline_fast_hashing_1e10_per_second']}")
    print("Feedback:")
    if result["feedback"]["warning"]:
        print(" - Warning:", result["feedback"]["warning"])
    if result["feedback"]["suggestions"]:
        for suggestion in result["feedback"]["suggestions"]:
            print(" - Suggestion:", suggestion)

# -------------------------------
# Function 2: Generate custom wordlist
# -------------------------------
def generate_custom_wordlist(name, dob, pet):
    base_words = [name.lower(), dob.replace("-", ""), pet.lower()]
    leet_subs = {
        'a': ['@', '4'], 'e': ['3'], 'i': ['1'], 'o': ['0'], 's': ['$', '5']
    }

    def leetspeak(word):
        variations = set([word])
        for i, ch in enumerate(word):
            if ch in leet_subs:
                for sub in leet_subs[ch]:
                    new_word = word[:i] + sub + word[i+1:]
                    variations.add(new_word)
        return list(variations)

    words = []
    for word in base_words:
        words += leetspeak(word)

    # Add years and common suffixes
    suffixes = ['123', '2024', '2025', '!', '@']
    full_list = []
    for word in words:
        for suf in suffixes:
            full_list.append(word + suf)
            full_list.append(suf + word)

    full_list = list(set(full_list))  # remove duplicates

    # Save to file
    filename = "custom_wordlist.txt"
    with open(filename, 'w') as f:
        for item in full_list:
            f.write(item + '\n')

    print(f"\n📝 Wordlist generated and saved as '{filename}' with {len(full_list)} entries.")

# -------------------------------
# Main Program
# -------------------------------
def main():
    print("=== 🔐 Password Analyzer & Wordlist Generator ===")
    password = input("\nEnter a password to analyze: ")
    analyze_password_strength(password)

    print("\n💡 Now let's generate a custom wordlist based on personal info.")
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (yyyy-mm-dd): ")
    pet = input("Enter your pet's name (or favorite thing): ")

    generate_custom_wordlist(name, dob, pet)

# Run the program
if __name__ == "__main__":
    main()
