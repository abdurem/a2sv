# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
set1=set(input().split())
input()
set2=set(input().split())

print(len(set1.difference(set2)))
