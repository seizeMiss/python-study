# /usr/bin/env python
# -*- coding: UTF-8 -*-
from lxml import etree
import tempfile
import shutil

CONFIG = "D://study//pythonStudy//workspace//python-study//configure.xml"

if __name__ == '__main__':
    try:
        parse = etree.XMLParser(remove_comments=False)
        tree = etree.parse(CONFIG, parser=parse)
        node = tree.find("./serviceName")
        print(node.text)
        node.text = "vRAL"

        f = tempfile.NamedTemporaryFile(mode="w", delete=False)
        f.close();
        tree.write(f.name, encoding="utf-8", xml_declaration=True)
        shutil.move(f.name, CONFIG)
    except Exception as e:
        print(e)
