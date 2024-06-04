#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

TAG = re.compile(r"(</?[a-z]+[^>]*?>)")


def main():
    with open("brew/inputdata.xml") as rawxmlfile:
        xmlfile = rawxmlfile.read()
        PIECES = TAG.split(xmlfile)
        for x in [x.strip() for x in PIECES if x.strip() != ""]:
            print(x)


if __name__ == "__main__":
    main()
