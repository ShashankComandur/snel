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

# Attempt at Chi Square 

counts = [0] * 127
for c in bunch_of_text:
    n = ord(c)
    counts[n] += 1

print(counts)

def mean(counts):

    total = 0
    for c in counts:
        total = total + c
    avg = total / len(counts)

    return avg

avg_counts = mean(counts)

print(avg_counts)



    



        
    
