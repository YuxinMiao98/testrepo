name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if line.startswith('From '):
        word = line.split()
        ps = word[1]
        counts[ps] = counts.get(ps, 0) + 1
    else:
        continue

bigcount = None
bigname = None
for ps, count in counts.items():
    if bigcount is None or count > bigcount:
        bigname = ps
        bigcount = count

print(bigname,bigcount)