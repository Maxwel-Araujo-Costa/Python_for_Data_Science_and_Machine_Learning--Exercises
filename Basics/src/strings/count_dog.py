#Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.

def countDog (text) :
    words = text.lower().split()
    dogCount = 0
    for word in words :
        if word == 'dog':
            dogCount += 1
    return dogCount

print(countDog('This dog runs faster than the other dog dude!'))