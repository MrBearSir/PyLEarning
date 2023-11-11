name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hrCounts = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != "From":
        continue
    time = wds[5].split(":")
    time = time[0]
    hrCounts[time] = hrCounts.get(time, 0) + 1
lst = list()
for k, v in hrCounts.items():
    newtup = (k, v)
    lst.append(newtup)
lst = sorted(lst)
for k, v in lst:
    print(k, v)