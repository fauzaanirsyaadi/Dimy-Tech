# Complete the staircase function below.
def staircase(n):
    for i in range(1, n+1):
        text = "#"*i
        space = " " * (n-i)
        print(space + text)
    return