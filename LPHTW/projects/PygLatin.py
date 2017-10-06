pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha(): # Check if its a string
    print original
    word = original.lower() # Convert to lower case
    first = original[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)] # Slicing and removing 0 index
    print new_word
else:
    print 'Word should contain letters(only)'
