import re
from pathlib import Path
from collections import defaultdict
import sys

def tokenize(file_path):
    path = Path(file_path) #using pathlib cuz my friend said it's better than os.path in general
    
    tokens = []
    with open(path, 'r', encoding='utf-8', errors='ignore') as file: #assuming English based text files, I'm just going to ignore errors with non utf-8 characters and skip over them
        for line in file: #assuming my text file doesn't have crazy long lines...
            line = line.lower() #a bit less efficient maybe to lowercase first but seems easier to code
            line_tokens = re.findall(r'\b[a-z0-9]+\b', line)  #extract words using regex, splits by non alphanumerical
            if line_tokens: #makes sure my newly processed line actually had at least one token in it
                tokens.extend(line_tokens) #add the found tokens to my result list

    return tokens
