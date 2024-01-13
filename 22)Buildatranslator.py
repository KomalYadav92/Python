'''Giraffe Language
in which i want all vowels becomes 'g'
eg
dog:dgg
cat:cgt'''

def  giralang(prase):
    translation=""
    for letter in prase:
        if letter in "aeiouAEIOU":
            translation=translation+"g"
        else:
            translation=translation+letter
    print(translation)


giralang("cat")

giralang(input("Enter a sentence:"))