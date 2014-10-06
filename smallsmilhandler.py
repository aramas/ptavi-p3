#!/usr/bin/python

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

        def __init__(self):

                self.taglist = []
                self.etiquetas = [
                        'root-layout', 'region', 'img', 'audio', 'textstream']
                self.atribs = {
                        'root-layout': ["width", "height", "background-color"],
                        'region': ["id", "top", "bottom", "left", "right"],
                        'img': ["src", "region", "begin", "dur"],
                        'audio': ["src", "begin", "dur"],
                        'textstream': ["src", "region"]}

        def startElement(self, name, attrs):
                self.dict = {}
                if name in self.etiquetas:
                        for atributo in self.atribs[name]:
                                self.dict[atributo] = attrs.get(atributo, "")
                        self.taglist.append([name, self.dict])

        def get_tags(self):
                return self.taglist

if __name__ == "__main__":
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(open('karaoke.smil'))
        print sHandler.get_tags()
