import requests
from bs4 import BeautifulSoup
import pylab

r = requests.get('https://tut-cikavo.com/pryroda/tvaryny/ryby/263-chomu-akuli-boyatsya-delfiniv')
page = BeautifulSoup(r.text, 'html.parser')
print(r.status_code)
row1 = page.head.title.text
row2 = page.body.text
names = ['розповідні', 'питальні', 'окличні']
frequency = [0, 0, 0]
frequency[0] = row2.count('. ')
frequency[1] = row2.count('? ')
frequency[2] = row2.count('! ')

xdata = names
ydata = frequency
pylab.bar (xdata, ydata)
pylab.savefig('sentences.png', dpi = 200)
pylab.show()

    