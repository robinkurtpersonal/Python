print("Make a string with me :>")
text = ""


enter_char = input('Enter character: ')
while enter_char != "0":
    text = text + enter_char
    enter_char = input('Enter character: ')
    
    
print(text)
