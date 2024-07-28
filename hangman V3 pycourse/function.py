def cdict(my_dict):
    newd={}
    index=0
    dict_keys=list(my_dict.keys())
    dict_values=list(my_dict.values())
    for values in dict_values:
        newd[values]=[]
    for values in dict_values:
        newd[values].append(dict_keys[index])
        newd[values].sort()
        index+=1
    return newd

course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
ans=cdict(course_dict)
print(ans)