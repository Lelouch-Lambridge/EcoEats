try:
    from googlesearch import search
except ImportError:
    print(" 'google' not found")

query = "low fat burritos" # we would need to concatentate user key words here
 
for j in search(query, tld="com", num=10, stop=10, pause=2):
    print(j) #need to extract specific lengths
