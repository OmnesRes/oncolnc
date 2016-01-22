import re

##def myloop(list1,list2):

def mysort(first,second):
    global i
    global j
    for i,j in zip(first,second):
        if i==j:
            if len(first)==1 or len(second)==1:
                if len(first)<len(second):
                    return -1
                else:
                    return 1
            else: 
                return mysort(first[1:],second[1:])
        if re.search('[0-9]',i) and not re.search('[0-9]',j):
            return -1
        elif re.search('[0-9]',j) and not re.search('[0-9]',i):
            return 1
        else:
            if i<j:
                return -1
            else:
                return 1

f=open('every_gene_id_upper.txt')
data=eval(f.read())
data.sort(cmp=mysort)
