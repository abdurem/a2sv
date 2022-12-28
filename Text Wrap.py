import textwrap

def wrap(string, max_width):
    ans=[]
    i=0
    while i < len(string):
        ans.append(string[i:i+max_width])
        i+=max_width  
    return '\n'.join(ans)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
