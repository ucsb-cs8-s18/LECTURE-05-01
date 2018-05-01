# todaysFuncs.py
# Functions from lecture 05/01/2018


# This is called the accumulator pattern
# I start a value at zero (total)
# I go through a list of items
# for each item I add that item into the total
# at the end, I return the total

def addEm(somelist):
    " return sum of numbers in somelist "
    total = 0
    for num in somelist:
        total  = total + num
    return total

# How can this go wrong? Here's one way:\
# This version always returns the first element
# in the list, no matter what .. unless
# ... if the list is empty, it returns None


def badAddEm(somelist):
    """
    try to return sum of numbers in somelist 
    but something goes wrong...
    """
    
    total = 0
    for num in somelist:
        total  = total + num
        return total   # indented ?!?!?!

def sumEvens(somelist):
    " add up only the even numbers "
    total = 0
    for num in somelist:
        if num % 2 == 0:  # if num is even
           total  = total + num
    return total

def brokenSumEvens(somelist):
    " add up only the even numbers (wrong)! "
    total = 0
    for num in somelist:
        if num % 2 == 0:  # if num is even
           total  = total + num
           return total

def kaputSumEvens(somelist):
    " add up only the even numbers (wrong)! "
    total = 0
    for num in somelist:
        if num % 2 == 0:  # if num is even
           total  = total + num
        return total


def firstEven(somelist):
  " first even number, or None if their are none"
  for num in somelist:
    if num % 2 == 0:  # if num is even
      return num



# The actual behaviour of kaputSumEvens is that
# it return 0 if the first element of the list is odd,
# and the first element of the list if it is even.

def findMax(somelist):
    winner = somelist[0]
    for i in range(1,len(someist)):
        if somelist[i] > winner:
            winner = somelist[i]
    return winner
    
def findMin(somelist):
    winner = somelist[0]
    for i in range(1,len(somelist)):
        if somelist[i] < winner:
            winner = somelist[i]
    return winner
    
