q = ['quiz practice code tom is good']
# a = 'good tom practice'

q = "quiz practice code tom is good"

# Split the input string into words
words = q.split()

# Rearrange the words and join them into a string
a = ' '.join([words[-1], words[words.index("tom")], words[words.index("practice")]])

print(a)
