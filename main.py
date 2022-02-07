from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
restart = 'yes'

while restart == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > 26:
            shift = shift % 26

        def caesar(direction,text,shift):
            new_text = ''
            if direction == 'decode':
                shift *= -1
            for letter in text:
                if letter in alphabet:
                    letter = alphabet[alphabet.index(letter)+shift]
                new_text += letter
            print(f"The {direction}d text: {new_text}")
        caesar(direction,text,shift)
    else:
        print("Direction type is not correct!")
    restart = input("Do you want to continue using the cipher program? Type 'yes' if you want to go again. Otherwisw type 'no'\n").lower()
print("Goodbye!")

