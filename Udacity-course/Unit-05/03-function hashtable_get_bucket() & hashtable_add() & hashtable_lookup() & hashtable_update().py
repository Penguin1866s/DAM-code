#In this archive, isn't anythig new, or it was copied from the courseor it was copied from other archive in this path.
def makehashtabale_forloop(nbuckets):#copied archive path.
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table

def hash_string(keyword, buckets):#copied archive path.
    val_ascid = []
    for char in keyword:
        val_ascid.append(ord(char))
    val_ascid = sum(val_ascid)
    num_bucket = val_ascid % buckets
    assert (num_bucket >= 0) and (num_bucket <= buckets -1) , "The number of the bucket result, isn't in the range between 0 and buckets -1"
    return num_bucket

def hashtable_get_bucket(htable, key):#copied course.
    return htable[hash_string(key, len(htable))]

def hashtable_add(htable, key, value):#copied course.
    bucket = hashtable_get_bucket(htable, key)
    bucket.append([key, value])

table = makehashtabale_forloop(3)
hashtable_add(table, 'udacity', 23)
hashtable_add(table, 'audacity', 17)
hashtable_add(table, 'bodacity', 19)
hashtable_add(table, 'wodacity', 28)
print(table)


def hashtable_lookup(htable, key):#copied course.
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None
print(hashtable_lookup(table, 'udacity'))

hashtable_add(table, 'udacity', 27)
print(hashtable_lookup(table, 'udacity'))
print(table)

def hashtable_update(htable, key, value):#copied course.
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return
    bucket.append([key, value])

print('\nNow, with the function hashtable_update() instead of hashtable_add():')
table = makehashtabale_forloop(3)
hashtable_update(table, 'udacity', 23)
hashtable_update(table, 'audacity', 17)
hashtable_update(table, 'bodacity', 19)
hashtable_update(table, 'wodacity', 28)
print(table)

print(hashtable_lookup(table, 'udacity'))
hashtable_update(table, 'udacity', 27)

print(hashtable_lookup(table, 'udacity'))
print(table)
