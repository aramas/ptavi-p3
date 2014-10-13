#!/usr/b in/python

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

from smallsmilhandler import SmallSMILHandler
import sys

File = sys.argv

parser = make_parser()
kHandler = SmallSMILHandler()
parser.setContentHandler(kHandler)
try:
	parser.parse(open(File[1]))
except:
	print ("Usage: python karaoke.py file.smil")

taglist = kHandler.get_tags()
linea = ""

for elemento in taglist:
	linea = elemento[0]
	for atributo in elemento[1].keys():
		if elemento[1][atributo] != "":
			linea = linea + ('\t') + atributo + ("=") + (elemento[1][atributo])
	print linea
