alphabet = [chr(i) for i in range(97, 123)]

# Caesar Cipher encryption function
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter  # Keep symbols/spaces unchanged
    print(f"✅ Here is the encoded result: {cipher_text}")

# Caesar Cipher decryption function
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
            plain_text += alphabet[shifted_position]
        else:
            plain_text += letter
    print(f"🔓 Here is the decoded result: {plain_text}")

# Main Caesar function to handle both directions
def caesar(start_text, shift_amount, direction):
    if direction == "encode":
        encrypt(start_text, shift_amount)
    elif direction == "decode":
        decrypt(start_text, shift_amount)
    else:
        print("❌ Invalid input. Please type 'encode' or 'decode'.")

# User interaction
print("=== Caesar Cipher Program ===")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Ensure shift value is within alphabet range
shift = shift % 26

caesar(start_text=text, shift_amount=shift, direction=direction)

# Optional: Loop to allow multiple operations
restart = input("Do you want to go again? Type 'yes' or 'no':\n").lower()
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(start_text=text, shift_amount=shift, direction=direction)
    restart = input("Do you want to go again? Type 'yes' or 'no':\n").lower()

print("👋 Goodbye! Thanks for using the Caesar Cipher.")
