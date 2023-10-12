#MMM MKHABELE
#02/07/23
def main():
    string=(input("Input: "))
    print(shorten(string))
def shorten(n):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for x in n:#ITERATE THROUGH THE STRING
        if x in vowels:#CHECK IF X IS IN LIST OF VOWELS
            n=n.replace(x,'')#REPLACE VOWEL WITH EMPTY STRING
    return n

if __name__=="__main__":
    main()

