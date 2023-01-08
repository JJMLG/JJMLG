word = input()
if word.isascii() == True:
    print(ord(word))
elif word.isdigit() == True:
    print(chr(int(word)))