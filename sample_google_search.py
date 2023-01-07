try:
    from googlesearch import search
except ImportError:
    print(" 'google' not found")

query = "low fat burritos" # we would need to concatentate user key words here

url_list = []

while len(url_list) <= 10:
    for j in search(query, tld="com", num=20, stop=20, pause=0):
        if 'youtube' in j or 'tiktok' in j:
            pass
        else:
            url_list.append(j)
            if len(url_list) >= 10:
                break
url_list.pop()
print(url_list[0])

