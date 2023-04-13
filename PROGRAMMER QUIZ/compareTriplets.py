# Complete the compareTriplets function below.
def compareTriplets(a, b):
    # totA = 0
    # totB = 0
    # for i in a:
    #     if a < b:
    #         totB = totB + 1
    #     elif a > b:
    #         totA = totA + 1
    # return totA(), totB()
    totA = 0
    totB = 0
    for i in range(len(a)):
        if a[i] < b[i]:
            totB = totB + 1
        elif a[i] > b[i]:
            totA = totA + 1
    return [totA, totB]