# -*- coding: utf-8 -*-

from lxml import etree
from pykml import parser
from pykml.factory import KML_ElementMaker as KML
import re, sys, os

no_code = open("no_code.txt", "a")
files = sys.argv[1:]
for file in files:
    print "processing %s" % file
    open(file,'r')
    doc = parser.parse(file)
    root = doc.getroot()

    for element in root.Document.Placemark:
        desc = element.description.text
        r = re.compile("<TR>\s*<TD>\s*School code\s*</TD>\s*<TD>\s*<B>\s*(\d+)\s*</B>", re.IGNORECASE|re.MULTILINE)
        code = r.findall(desc)
        name = element.name.text
        element.remove(element.description)
        try:
            d = KML.description(code[0])
            # code_object = KML.code(code[0])
        except:
            no_code.write(name+"\n")

        if d is not None:
            element.append(d)

    filename = "clean/"+file.split('.')[0]+"c.kml"
    dir = os.path.dirname(filename)
    if not os.path.exists(dir):
        os.mkdir(dir)

    outfile = open(filename,'w')
    outfile.write(etree.tostring(doc, pretty_print=True))
