import re
from pathlib import Path
from collections import defaultdict
import sys

'''
Runtime complexity of tokenize should be O(n), linear time based on length (# of characters) of my file.
I go through the text file once line by line, convert to lowercase which is O(n) and do regex matching for each line once.
Can see re's documentation here https://docs.python.org/2/library/re.html
I could have used isalnum() instead of regex instead, probably would have been easier.
The regex is O(n) because it processes the string in a single pass.
The [a-z0-9]+ checks the characters once to see if it matches this pattern (alphanumerical), which is O(1) for each character.
The (?=[\s_]|$) and (?<=_) parts checks if the alphanumerical stuff is surrounded by either a word boundary or underscore.
These are look forward and look backwards which make sure the matched word has this condition so it's also O(n).

CURRENTLY MY CODE SAVES WORDS SUCH autodafés as autodaf and s. Because the assignment wasn't clear, I'm keeping it like this.
I could just throw out the whole word as well if that's not right.

I also add these extracted tokens to the list once based on the original text file, O(n).
'''
def tokenize(file_path):
    path = Path(file_path) #using pathlib cuz my friend told me a few months ago it's better than os.path in general
    
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
            line = line.lower() #a bit less efficient maybe to lowercase first
            line_tokens = re.findall(r'\b[a-z0-9]+(?=\b|_)|(?<=_)[a-z0-9]+', line) #extract words using regex, splits by non alphanumerical including underscore (the underscore stuff complicates it a lot)
            if line_tokens: #makes sure my newly processed line actually had at least one token in it
                tokens.extend(line_tokens) #add the found tokens to my result list

    return tokens
    
'''
Runtime complexity of computeWordFrequencies probably O(n) as well.
I go through all the tokens from my list (n tokens) and do stuff (accessing, adding) with a hashmap, which is usually O(1).
'''
def computeWordFrequencies(tokens):
    freq = defaultdict(int) #using default dict so I don't have to check if I have the token already in my hashmap (not that it really matters, I can do an if else)
    for token in tokens:
        freq[token] += 1  #much count very wow, goes through my list and ups the count in my dict
    return dict(freq)  #returning a regular dictionary instead of defaultdict just in case, I saw someone on eddiscussion say something about that
    
'''
Runtime complexity of printFreq probably O(n log n).
Converting from a dictionary to a list of tuples is O(n).
Sorting is going to be O(n log n) cuz I'd assume python has a good default sort.
Printing the sorted items is O(n).
'''
def printFreq(frequencies):
    sorted_tokens = sorted(frequencies.items(), key=lambda x: (-x[1], x[0])) #dictionary is converted into a list then sorted by frequency first in descending order then by ascending alphabetical order if they have the same frequency
    for token, freq in sorted_tokens:
        print(f"{token} {freq}")

if __name__ == "__main__": #runs if script is run as the main code, so in partA not partB
    if len(sys.argv) < 2: #making sure that I have enough command line arguments
        print("Needs the path to a file as an argument")
        sys.exit()

    file_path = sys.argv[1]
    tokens = tokenize(file_path)
    freq = computeWordFrequencies(tokens)
    printFreq(freq)