class Solution(object):
    def sortSentence(self, s):
        arr=s.split(" ")
        mystr=''
        dic={}
        for i in arr:
            for j in range(len(arr)+1):
                if(i[-1]==str(j)):
                    dic[j-1]=i.replace(str(j),' ')
        for j in range(len(dic)):
            mystr+=dic[j]
        mystr=mystr.strip()
        return mystr
        