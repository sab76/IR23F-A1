import re
from pathlib import Path
from collections import defaultdict
import sys

def tokenize(file_path):
    path = Path(file_path) #using pathlib cuz my friend said it's better than os.path in general
    
    #doing some basic error checking to check if the file given exists and that it's a file
    if not path.exists():
        print(f"File '{file_path}' does not exist.")
        sys.exit()

    if not path.is_file():
        print(f"'{file_path}' is not a file.")
        sys.exit()

    tokens = []
    with open(path, 'r', encoding='utf-8', errors='ignore') as file: #assuming English based text files, I'm just going to ignore errors with non utf-8 characters and skip over them
        for line in file: #assuming my text file doesn't have crazy long lines...
            line = line.lower() #a bit less efficient maybe to lowercase first but seems easier to code
            line_tokens = re.findall(r'\b[a-z0-9]+\b', line)  #extract words using regex, splits by non alphanumerical
            if line_tokens: #makes sure my newly processed line actually had at least one token in it
                tokens.extend(line_tokens) #add the found tokens to my result list

    return tokens

def computeWordFrequencies(tokens):
    freq = defaultdict(int) #using default dict so I don't have to check if I have the token already in my hashmap (not that it really matters, I can do an if else)
    for token in tokens:
        freq[token] += 1  #much count very wow, goes through my list and ups the count in my dict
    return dict(freq)  #returning a regular dictionary instead of defaultdict just in case, I saw someone on eddiscussion say something about that
    
def printFreq(frequencies):
    sorted_tokens = sorted(frequencies.items(), key=lambda x: (-x[1], x[0])) #dictionary is converted into a list then sorted by frequency first in descending order then by ascending alphabetical order if they have the same frequency
    for token, freq in sorted_tokens:
        print(f"{token}\t{freq}")
