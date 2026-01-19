from classes import CaesarCipher, ROT13Cipher, XORCipher, AtbashCipher, Translator
from mappings import t2m, m2t, t2b, b2t, t2bacon, bacon2t

def rules():
    print("""
    *****************  Encryption Software Rules  *****************
    
    Morse Code:
      • Separate letters with a space (" ")
      • Separate words with a slash ("/")

    Binary Code:
      • Separate bytes with a space (" ")

    Bacon Cipher:
      • Each letter represented by 5-character pattern (A/B)
      • Separate words with space (" ")

    Caesar Cipher:
      • Only letters are shifted
      • Choose a positive integer for shift value

    General:
      • Type 'exit!' at any time to quit the program
    """)

def menu():
    print("\nWhat would you like to do?")
    print("1) Text → Morse code")
    print("2) Morse code → Text")
    print("3) Text → Binary")
    print("4) Binary → Text")
    print("5) Text → Bacon Cipher")
    print("6) Bacon Cipher → Text")
    print("7) Caesar Cipher (Encrypt / Decrypt)")
    print("8) ROT13 Cipher")
    print("9) XOR Cipher")
    print("10) Atbash Cipher")
    print("11) Show Rules Again")
    print("Type 'exit!' to quit.")
    return input("\nEnter your choice: ").strip()

def get_text():
    return input("Enter your text: ")

def get_shift():
    while True:
        try:
            return int(input("Enter the shift number: "))
        except ValueError:
            print("❌ Please enter a valid integer.")

def main():

    # Initialize cipher classes
    caesar = CaesarCipher()
    rot13 = ROT13Cipher()
    atbash = AtbashCipher()
    xor_key = "key"  # Default key for XOR Cipher
    xor = XORCipher(xor_key)

    # Translator ciphers
    morse_enc = Translator(t2m, kind="morse")
    morse_dec = Translator(m2t, kind="morse")
    binary_enc = Translator(t2b, kind="binary")
    binary_dec = Translator(b2t, kind="binary")
    bacon_enc = Translator(t2bacon, kind="bacon")
    bacon_dec = Translator(bacon2t, kind="bacon")

    while True:
        choice = menu()

        if choice.lower() == "exit!":
            print("👋 Thank you for using the Encryption Software!")
            break

        elif choice == "11":
            rules()
            continue

        text = get_text()

        if choice == "1":
            print("🔹 Morse Code:", morse_enc.encrypt(text.lower()))
        elif choice == "2":
            print("🔹 Text:", morse_dec.decrypt(text))
        elif choice == "3":
            print("🔹 Binary Code:", binary_enc.encrypt(text.lower()))
        elif choice == "4":
            print("🔹 Text:", binary_dec.decrypt(text))
        elif choice == "5":
            print("🔹 Bacon Cipher:", bacon_enc.encrypt(text.lower()))
        elif choice == "6":
            print("🔹 Text:", bacon_dec.decrypt(text))
        elif choice == "7":
            shift = get_shift()
            caesar.shift = shift
            mode = input("Encrypt or Decrypt? (e/d): ").lower()
            if mode == "e":
                print("🔹 Encrypted:", caesar.encrypt(text))
            elif mode == "d":
                print("🔹 Decrypted:", caesar.decrypt(text))
            else:
                print("❌ Invalid option.")
        elif choice == "8":
            print("🔹 ROT13:", rot13.encrypt(text))
        elif choice == "9":
            key = input(f"Enter XOR key (default='{xor_key}'): ").strip() or xor_key
            xor.key = key
            result = xor.encrypt(text)
            print("🔹 XOR Result:", result)
        elif choice == "10":
            print("🔹 Atbash Cipher:", atbash.encrypt(text))
        else:
            print("❌ Invalid choice. Please try again.")

# start the program
if __name__ == "__main__":
    print("🔐 Welcome to the Cryptography Toolkit!")
    rules()
    main()