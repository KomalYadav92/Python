#working with the strings
a="Komal"
print(a)


b='''Komal is so beautiful!!'''
print(b)

c="""Komal is very hardworking girl"""
print(c)

#Strings are array
a="Komal"
print(a[2])
length=len(a)

print(length)

for x in "banana":
    print(x)


#Concatenating String Literals in Python Using join Method
words = ['welcome', 'to', 'Board Infinity']

joined = ' '.join(words)
print(joined)


#Concatenating Strings in Python Using the format Method
word1 = 'Hey'
word2 = 'there'

words = '{} {}!'.format(word1, word2)

print(words)
#Concatenating Strings in Python Using the % Formatting
word1 = 'Hey'
word2 = 'there'

words = '%s %s!' % (word1, word2)

print(words)

# Joining Strings with String Literals
joined = "hey " "there"

print(joined)