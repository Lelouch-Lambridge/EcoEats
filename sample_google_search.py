try:
    from googlesearch import search
except ImportError:
    print(" 'google' not found")

while True:
    prompt = input('Enter your search prompt: ').split( )
    if len(prompt) > 5:
        print('Enter a shorter search')
    else:
        break
prompt = str(prompt)
query = prompt + ' recipe'

url_list = []

while len(url_list) <= 10:
    for j in search(query, tld="com", num=20, stop=20, pause=0):
        if 'youtube' in j or 'tiktok' in j or 'pintrest' in j or 'facebook' in j or '.gov' in j:
            pass
        else:
            url_list.append(j)
            if len(url_list) >= 10:
                break
url_list.pop()
for i in url_list:
    print(i)

