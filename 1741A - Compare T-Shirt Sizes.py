from collections import Counter
n=int(input())
 
sizes={'L':2, 'M':1, 'S':0}
 
for i in range(n):
    l1, l2=input().split()
    size1, size2 = l1[-1], l2[-1]
 
    if sizes[size1] > sizes[size2]:
        print('>')
    elif sizes[size1] < sizes[size2]:
        print('<')
    else:
        if size1 == 'L':
            if len(l1) > len(l2):
                print('>')
            elif len(l1) < len(l2):
                print('<')
            else:
                print('=')
        elif size1 == 'S':
            if len(l1) > len(l2):
                print('<')
            elif len(l1) < len(l2):
                print('>')
            else:
                print('=')
        else:
            print('=')
