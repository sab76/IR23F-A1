from PartA import tokenize
from pathlib import Path
import sys
'''
Runtime complexity is O(n) + O(m).
Tokenize is assumed to be O(n) + O(m).
Making sets is also O(n) + O(m).
Intersection is O(n) with n smallest between n and m.
So it's linear with the size of the inputs (# of characters in the text files).
'''
def tokens_in_common(file1, file2):
    tokens1 = tokenize(file1)
    tokens2 = tokenize(file2)
    common_tokens = list(set(tokens1) & set(tokens2)) #stackoverflow said this is O(n) and implemented in C so I think this would be fast plus it removes the repeated tokens https://stackoverflow.com/questions/3697432/how-to-find-list-intersection
    return common_tokens, len(common_tokens)
    
#not really sure if I'm supposed to make a main to print or have the function print but it's cleaner like this
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Not enough inputs (needs 2 text files)")
        sys.exit()

    file1, file2 = sys.argv[1], sys.argv[2]
    common_tokens, count = tokens_in_common(file1, file2)
    #print(common_tokens)
    print(count)