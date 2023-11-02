#This function it was copied from the course.
def make_hashtable_whileloop(nbuckets):#It outputs a list of lists, where each list is a bucket.
    i = 0
    table = []
    while i < nbuckets:
        table.append([])
        i += 1
    return table
print(make_hashtable_whileloop(12))

#This function it was created by me.
def makehashtabale_forloop(nbuckets):#Has the same functionality that the last function, but it in fewer lines.
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table
print(makehashtabale_forloop(12))

def make_hashtable_NOT(nbuckets):#This function was copied from the course.
    result = [[]] * nbuckets
    return result
print(make_hashtable_NOT(12))

#The evidence of the uselessness of "make_hashtable_NOT()".
table0 = make_hashtable_whileloop(12)
table1 = makehashtabale_forloop(12)
table2 = make_hashtable_NOT(12)

table0[0].append(1)
table1[0].append(1)
table2[0].append(1)

print('\n')
print(table0)
print(table1)
print(table2)
