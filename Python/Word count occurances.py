
    
def word_count(str):
    frequency = dict()
    words = str.split()

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


print( word_count(input('Enter input string:')))
