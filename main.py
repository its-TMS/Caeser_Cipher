from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(start_text,plain_text, shift_amount):
  caeser_text = ""
  if start_text == 'decode':
    shift_amount *= -1
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      if new_position >= 26:
        new_position = new_position % 26
      new_letter = alphabet[new_position]
      caeser_text += new_letter
    else:
      caeser_text += letter
              
  print(f"Here's the {start_text}d text: {caeser_text}\n")

print(logo)

status = True
while status:
  direction = input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caeser(start_text=direction, plain_text=text, shift_amount=shift)

  try_again = input(f"Type 'yes' if you'd like to start again, otherwise 'no' to stop:\n").lower()

  if try_again == 'no':
    status = False
    print(f"Good Bye! See Yaa...")
  
  