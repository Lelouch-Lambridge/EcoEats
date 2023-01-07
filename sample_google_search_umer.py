try:
    from googlesearch import search
except ImportError:
    print(" 'google' not found")

query = "low fat burritos"  # we would need to concatentate user key words here

for j in search(query, tld="com", num=10, stop=10, pause=2):
    print(j)  # need to extract specific lengths

notten = True

listoflinks = []

numberoflinks = 10

while notten:
    for j in search(query, tld="com", num=numberoflinks, stop=numberoflinks, pause=2):
        if "www.youtube.com" in j:
            numberoflinks += 1
        elif "www.tiktok.com" in j:
            numberoflinks += 1
        elif len(listoflinks) == 10:
            notten = False
        else:
            listoflinks.append(j)
