import string   #the following module is imported to make use of different types of variables to make a password
import random   #the following module is imported to take out random variables out of the list thus maintaining the randomness and secracy of the password

if __name__=="__main__":
    s1 = string.ascii_lowercase     #this commands intialises values abcdefghijklmnopqrstuvwxyz in s1
    s2 = string.ascii_uppercase     #this commands intialises values ABCDEFGHIJKLMNOPQRSTUVWXYZ in s2
    s3 = string.digits              #this commands intialises values 0123456789 in s3
    s4 = string.punctuation         #this commands intialises values !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ in s4

    length = int(input("Please enter the length of the required password: ")) #this is taking input from the user about the length of the password
    s = []                                    #here a empty list is intialised so the others could add up into one 
    s.extend(list(s1))                        #concatinating s1 as a list into s
    s.extend(list(s2))                        #concatinating s2 as a list into s
    s.extend(list(s3))                        #concatinating s3 as a list into s
    s.extend(list(s4))                        #concatinating s4 as a list into s  
    print("".join(random.sample(s,length)))            #printing the sample values randomly 

    
    #random.shuffle(s)                      this method can also be implemented into the program instead of random.sample method
    #print("".join(s[0:length]))
