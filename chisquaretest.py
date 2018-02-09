import random

# Text Generator

def generate_random_text(num_chars):
    text = ""

    for i in range(num_chars):
        r = random.randint(32, 126)
        text += chr(r)
    
    return text

bunch_of_text = generate_random_text(1500)

print(bunch_of_text)

# ASCII Array

counts = [0] * 127
for c in bunch_of_text:
    n = ord(c)
    counts[n] += 1

print(counts)

# Mean Function

def mean(counts):

    total = 0
    for c in counts:
        total = total + c
    avg = total / len(counts)

    return avg

avg_counts = mean(counts)

# Chi Square Formula

def chi_square(counts):

    exp = mean(counts)
    sum = 0

    for i in bunch_of_text:
        sum += ((ord(i)+exp))**2/exp

    return sum

chisquare = chi_square(counts)

print(chisquare)
    
    




    



        
    
