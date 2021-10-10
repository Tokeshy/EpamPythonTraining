### Task 1.3
#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
#Examples:
#Input: ['red', 'white', 'black', 'red', 'green', 'black']
#Output: ['black', 'green', 'red', 'white', 'red']
InpList = str(input()).split(',')
OutList = []
for wrd in InpList: 
    wrd = wrd.replace(' ','')
    wrd.lower     
    if wrd not in OutList:
        OutList.append(wrd)
print(sorted(OutList))

#################################################################
### Task 1.3
#Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
#Examples:
#Input: 60
#Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
import math # unwritten code is the best so i decided do not to "reinvent the wheel"

def divisorGenerator(n): 
    ListOfDivs = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                ListOfDivs.append(int(n / i))
    for divisor in reversed(ListOfDivs):
        yield divisor

NumbToCheck = int(input())
print (list(divisorGenerator(NumbToCheck)))