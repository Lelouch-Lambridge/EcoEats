try:
    from googlesearch import search
except ImportError:
    print(" 'google' not found")

query = "low fat burritos"  # we would need to concatentate user key words here
searchten = 10

for j in search(query, tld="com", num=searchten, stop=10, pause=2):
    print(j)  # need to extract specific lengths


notten = True
listrecipe = []

while notten:
    for i in search(query, tld="com", num=searchten, stop=None, pause=2):
        if "www.youtube.com" in i:
            searchten += 1
        elif len(listrecipe) == 10:
            notten = False
        else:
            listrecipe.append(i)
