print("Type 'm' for Morse to Alphanumeric Translation")
MODE = input("or type 'a' for Anphanumeric to Morse Translation ")

#dictioaries 
letters = {
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--..",}
morse = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'}
#function to translate alphanumeric to morse
def A():
    sentence = input("Write a sentence:")
    for word in sentence.split():
        for letter in word.lower(): 
            #check if letter is in alphabet
            if letter.isalpha():  
                if letter in letters:
                    #end = "" stops the output from jumping to a new line every time
                    print(f"{letters[letter]} ", end = " ")
                else:
                    print(f"  {letter} is not in the dictionary")
            else: 
                print("Non-alphabetical input has been ingnored")
        #puts the pipe after each word
        print(end = " | ")
#function to translate morse to alphanumeric
def M():
    code = input("Write your Morse code here (put a space between each letter and use '/' for spaces between words): ").strip()
    #check words as blockes split by /
    words = code.split(" / ")
    decoded_message = []
    #checks each word
    for word in words:
        letters_in_word = word.split()
        #joins the letters back together
        decoded_word = "".join(morse.get(letter, "?") for letter in letters_in_word)
        #adds checked words back into the array
        decoded_message.append(decoded_word)
    #joins words into a sentence
    print("Translated Text:", " ".join(decoded_message))

#if statment that will understand both capital and lowercase inputs
if MODE.lower() == "a":
    A()
elif MODE.lower() == "m":
    M()
else:
    print("Invalid input. Please enter 'm' or 'a'.")