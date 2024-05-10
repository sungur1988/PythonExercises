def flatten(elList,res):
    for i in elList:
        if type(i)==list:
            flatten(i,res)
        else:
            res.append(i)

    return res

listt = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

flist = flatten(listt,[])

print(flist)