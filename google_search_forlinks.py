try:
    from googlesearch import search
except ImportError:
    print(" 'google' not found")

query = "low fat burritos" #sample keywords, would need to use concatentation of user entered keywords

 
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
