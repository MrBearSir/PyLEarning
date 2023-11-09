fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    lines = line.split()
    for word in lines:
        if word != lst:
            lst.append(word)
lst = list(dict.fromkeys(lst))
lst.sort()
print(lst)