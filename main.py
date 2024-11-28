# creating a password generator

import string
import random

if __name__== "__main__":
    
    s1 = string.ascii_lowercase
    #print ("Available characters:", s2)
    s2 = string.ascii_uppercase
    #print ("Available characters:", s3)
    s3 = string.digits
    #print ("Available characters:", s4)
    s4 = string.punctuation
    #print ("Available characters:", s5)
    
    plen = int(input("Enter Password Length\n"))
    
    s = []
    s += list(s1) + list(s2) + list(s3) + list(s4)
    
   # print ("\nYour Password is:", s)
   
    random.shuffle(s)
    
    print ("".join(s [0:plen]))
    
    print ("\n\nCode by: [Vaishnavi Singh, 590011338]")
    