from wonderwords import RandomSentence
import random
import os

# Define a list of physics-related words or phrases
physics_words = ["gravity", "quantum", "photon", "electron", "quark", "neutrino", "black hole", "dark matter", "cosmos", "universe"]

# Define a function to generate a random sentence
def generate_sentence():
 r = RandomSentence()
 sentence = r.sentence().split()
 random_index = random.randint(0, len(sentence)-1)
 sentence[random_index] = random.choice(physics_words)
 return ' '.join(sentence)

# Define a function to generate a text file with random sentences
def generate_text_file(num_sentences):
    folder_name = "files"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = folder_name + "/ELE302-" + ''.join(random.choice('0123456789') for _ in range(4)) + ".txt"
    with open(filename, 'w') as f:
        for _ in range(num_sentences):
            f.write(generate_sentence() + "\n")

# Generate n text files
n = 10 # Change this to the number of files you want to generate
for _ in range(n):
 generate_text_file(100) # Change 100 to the number of sentences you want in each file

