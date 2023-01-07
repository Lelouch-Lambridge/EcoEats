keywords, results = input("Keywords, Max 5: ").split()[:5], []

data = ['a']
for x in data:
 recipies = {data.name: [data.ingrediants]}

for r,ing in recipies.items():
 check = 0
 for x in r:
  if x in keywords: check += 1
 if check == len(keywords):results += r

print(results)

