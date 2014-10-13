#!/usr/b in/python

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

from smallsmilhandler import SmallSMILHandler
import sys
import os

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
                if atributo == "src":
                        os.system("wget -q " + elemento[1][atributo])
                        direcciontroz = elemento[1][atributo].split("/")
                        elemento[1][atributo] = direcciontroz[-1]
                if elemento[1][atributo] != "":
                        linea = linea + ('\t')
                        linea += atributo + ("=") + (elemento[1][atributo])
        print linea
