l=input()
n_1 = int(l,2)
n_2 = int(input(),2)
o=format(n_1&n_2,'b').zfill(len(l))
print(o)
