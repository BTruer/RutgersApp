import json
def parsefood():
	f = open('food1.txt','r')
	d = json.loads(f.read())
	for i in d[0]['meals']:
		print('\n---'+i['meal_name']+'---\n')
		if i['meal_avail'] is True:
			for j in i['genres']:
				print()
				print(j['genre_name'])
				print('-------------')
				for k in j['items']:
					print(k)


'''
	#book = {}
	#book['tom'] = {
			'name': 'tom',
			'address': '1 pway road',
			'phone': 32321155
	#}
	#book['bob'] = {
			'name': 'bob',
			'address': 'here',
			'phone': 5656556
	#}

	#print(book)
	#print(type(book))
	#json.dumps()
	#parsed_json = json.loads(f.readline())
	#print(parsed_json[0]['meals'][''])
'''

parsefood()