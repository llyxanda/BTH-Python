

def zip_2_lists(fill_value, list1, list2):
    '''
    Function to catch all the wrong entered words in the file text vs.
    user input and store it as tuples of form ([file word], [input word])
    '''
    zipped_list = []
    for idx in range(max(len(list1), len(list2))):
        try:
            if list1[idx] != list2[idx]:
                zipped_list.append((list1[idx], list2[idx]))
        except:
            if len(list1) > len(list2):
                zipped_list.append((list1[idx], fill_value))
            else:
                zipped_list.append((fill_value, list2[idx]))
    return zipped_list

l=[('Hello', 'Hellå'), ('my', 'm'), ('is', 'andreas'), 
 ('Andreas', ''), ('name', 'nameaa'), ('', 'ko'), ('My', ''), 
 ('name', ''), ('is', ''), ('Da', '')]
long_l = []
for tup in l:
    long_l += zip_2_lists('', tup[0], tup[1])
print(long_l)
print(len(long_l))
