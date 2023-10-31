#Find and slice input.
text = "X-DSPAM-Confidence:    0.8475"
d = text.find(" ")
res = text[d:len(text)+1].strip()#[d:] will do the same 
resF = float(res)
print(res)

# Printing text from file
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
   print(line.upper().rstrip())

# Reading file, sarching for specific input and getting avarage from floating values
fname = input("Enter file name: ")
fh = open(fname)
cnt = 0
total = 0
avg = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    scu = line.find(":")
    fp = line[scu+1:]
    fp = fp.strip()
    ffp = float(fp)
    cnt = cnt + 1
    total = float(total) + ffp
avg = total / cnt
print("Average spam confidence: " + str(avg))