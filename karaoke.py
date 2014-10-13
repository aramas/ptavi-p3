#!/usr/b in/python

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler
import sys
import os


class KaraokeLocal (SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        kHandler = SmallSMILHandler()
        parser.setContentHandler(kHandler)
        parser.parse(open(fichero))
        self.taglist = kHandler.get_tags()

    def __str__(self):
        self.linea = ""
        self.lista = ""
        for elemento in self.taglist:
            self.linea = elemento[0]
            for atributo in elemento[1].keys():
                if elemento[1][atributo] != "":
                    self.linea = self.linea + ('\t')
                    self.linea += atributo + ("=")
                    self.linea += (elemento[1][atributo])
            self.lista = self.lista + self.linea + ('\n')
        return self.lista

    def do_local(self):
        self.linea = ""
        for elemento in self.taglist:
            self.linea = elemento[0]
            for atributo in elemento[1].keys():
                if atributo == "src":
                    os.system(
                    "wget -q " + elemento[1][atributo])
                    direcciontroz = elemento[1][atributo].split("/")
                    elemento[1][atributo] = direcciontroz[-1]
                if elemento[1][atributo] != "":
                    self.linea = self.linea + ('\t')
                    self.linea += atributo + ("=")
                    self.linea += (elemento[1][atributo])

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print ("Usage: python karaoke.py file.smil")
        raise SystemExit
    karaoke = KaraokeLocal(sys.argv[1])
    print karaoke.__str__()
    karaoke.do_local()
    print karaoke.__str__()
