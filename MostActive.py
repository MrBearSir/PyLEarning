name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
emailers = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != "From":
        continue
    email = wds[1]
    emailers[email] = emailers.get(email, 0) + 1
topCommiter = None
topCommits = None
for email, count in emailers.items():
    if topCommits is None or count > topCommits:
        topCommits = count
        topCommiter = email
print(topCommiter, topCommits)