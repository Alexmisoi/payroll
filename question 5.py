# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

tup1 = (1, 2, 3, 4, 5, 6)
divider = int(len(tup1)/2)
tpl1 = tp1[:divider]
tpl2 = tp1[divider:]
tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tp1 = tp[:5]
tp2 = tp[5:]
print(tp1)
print(tp2)

