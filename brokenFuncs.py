# correct versions

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
    
def brokeMax1(somelist):
    winner = somelist[0]
    for i in range(1,len(somelist)):
        if somelist[i] > winner:
            winner = somelist[i]
        return winner

def brokeMax2(somelist):
    winner = somelist[0]
    for i in range(1,len(somelist)):
        if somelist[i] > winner:
            winner = somelist[i]
            return winner

def brokeMax3(somelist):
    winner = somelist[0]
    for i in range(1,len(somelist)):
        if somelist[i] > winner:
            winner = i
    return winner
