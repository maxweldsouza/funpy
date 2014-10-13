from bs4 import BeautifulSoup
import urllib
import re

page = urllib.urlopen('file:///home/maxweldsouza/Projects/scantuary/gather/phantom240.html')
page = page.read()

soup = BeautifulSoup(page)

print soup.find_all( 'table', class_='product-spec-table')
