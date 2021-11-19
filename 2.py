#варіант 8
import requests
from bs4 import BeautifulSoup
from array import *
import csv
import pylab

r = requests.get('https://travel.24tv.ua/kudi-poyihati-shhob-vidchuti-silu-prirodi-spisok-lokatsiy-harakterom_n1791662')
page = BeautifulSoup(r.text, 'html.parser')
print(r.status_code)
row1 = page.head.title.text
row2 = page.body.text
letters_str = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
letters = list(letters_str)
frequency =[]
L = len(letters)
for i in range(L):
    elem = letters[i]
    fr = row2.count(elem)
    frequency.append(fr)
xdata = letters
ydata = frequency
pylab.bar (xdata, ydata)
pylab.show()
