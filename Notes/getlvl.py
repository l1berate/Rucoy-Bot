from lxml import etree, html
import requests

page = requests.get('https://www.rucoyonline.com/characters/Ngs%20Anaconda')
tree = html.fromstring(page.content)
result = tree.xpath('/html/body/text()')
print(result[0])
#result = html.tostring(result[0][0])

#print(result)

'''
def findendofstr(strandmore):
	try:
		for x in range(len(strandmore)):
			chartocheck = int(binascii.hexlify(strandmore[x:x+1]), 16)
			if chartocheck < 20:
				return x
		return 0
	except Exception as e:
		return "An unknown error occurred - findendofstr - {}".format(e)
'''