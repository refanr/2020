# Keep these 2 lines
text_to_translate = input("Text to translate: ")
VOWELS = "aeiouyAEIOUY"

translation = ''
length = len(text_to_translate.split())
consonants = ''



# ...add your code here
for i in range(0,length):
    for char in VOWELS:
        if text_to_translate.split()[i][0] != char:
            for ch in text_to_translate.split()[i]:
                if text_to_translate.split()[i][:]:
                    consonants += 
        


    print(translation)
    
    

# Keep this line
print("Translation:", translation)
