from itertools import permutations

def perm(x):
    y = permutations(x)
    return y

number = [1,2,3]

print(perm(number))