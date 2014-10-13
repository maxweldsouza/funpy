from bs4 import BeautifulSoup
import urllib
import re

page = urllib.urlopen('file:///home/maxweldsouza/Projects/scantuary/gather/phantom240.html')
page = page.read()

def nzxt_cabinets(page):
    soup = BeautifulSoup(page)
    return soup.select('table[class~=product-spec-table]')

def cm_cabinets(page):
    soup = BeautifulSoup(page)
    return soup.select('.htmlEditorArea > table')

print nzxt_cabinets(page)

