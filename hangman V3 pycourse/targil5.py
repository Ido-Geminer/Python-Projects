def sort_anagrams(list_of_strings):
    fnl=[]
    agra=[]
    for word in range(len(list_of_strings)):
        for secword in range(len(list_of_strings)):
            temp=sorted(list_of_strings[word])
            temp2=sorted(list_of_strings[secword])
            if temp==temp2:
                agra.append(list_of_strings[secword])
        if agra not in fnl:
            fnl.append(agra)
        agra=[]
    return fnl


list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
print(sort_anagrams(list_of_words))