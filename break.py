#!/usr/bin/env python3
import sys

# DO NOT ADD ANY import STATEMENTS

# DO NOT CHANGE THIS LINE NOR ANYTHING ABOVE THIS LINE

# You can add functions here to support your implementation below

#Reverses permatution
def reverse_permute(block):
    result = [block[3], block[1], block[0], block[2]]
    return result
    
#Handles subtraction and the reverse truncation where needed    
def subtraction_of(block, key):
    result = [(block[i] - key[i]) % 10 for i in range(4)] 
    return result  
    
#Decrypts the ciphertext    
def decrypt_block(block, key):
    second_half_of_key=[key[i+4] for i in range(4)]
    first = subtraction_of(block, second_half_of_key)
    second = reverse_permute(first)
    first_half_of_key=[key[i] for i in range(4)]
    third = subtraction_of(second, first_half_of_key)
    plaintext = reverse_permute(third)
    
    return plaintext

     
def breakcipher(block): # This function must return a string of 4 decimal digits
    plaintext = "0000" 

    # YOUR IMPLEMENTATION HERE
    
    known_plaintext = [0,1,2,3]
    known_ciphertext = [7,4,6,8]
    
    #Ensures all block data is in the form of integer
    block = [int(digit) for digit in block]
    
    #Brute forces possible keys and stops at the first.
    #My logic is that due to modulo equivalence checking
    # one key is enough.
    for candidate_key in range(10**8):
        key = [int(d) for d in f"{candidate_key:08d}"]
        
        if decrypt_block(known_ciphertext, key) == known_plaintext:
            plaintext = decrypt_block(block, key)
            break
            
    plaintext=''.join(map(str, plaintext))
    return plaintext

# DO NOT CHANGE THIS LINE NOR ANYTHING BELOW THIS LINE

def non_digits(s):
    return len(s.strip("0123456789")) > 0

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print('''Usage: break.py

        Call this program without any command line arguments. Then enter
        blocks of 4 decimal digits to be decrypted by (your) implementation.
        ''')
        sys.exit(1)

    print("Go ahead, type in your ciphertext consisting of blocks of 4 decimal digits.")
    print("Do NOT input any brackets [ ] or commas")
    for line in sys.stdin:
        line = line.strip().replace(" ","")
        if non_digits(line):
            print("Error: Input contains non-decimal digit characters.")
            sys.exit(1)
        if len(line) % 4 != 0:
            print("Error: The length of your input should be, but is not, a multiple of\n      the cipher's block size (which is 4).")
            sys.exit(1)
        while line!="":
            print(breakcipher(line[0:4]))
            line=line[4:]
