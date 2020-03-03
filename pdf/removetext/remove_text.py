#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time : 2020-03-04
# @Author : Deming

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.pdf import ContentStream
from PyPDF2.generic import TextStringObject, NameObject
from PyPDF2.utils import b_

def remove_text(texttag, readfile, outfile):
    '''
    删除指定文字
    '''
    print("read file: " + readfile)
    with open(readfile, "rb") as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        num = reader.getNumPages()
        print("total pages:" + str(num)) 

        num = 2
        for index in range(num):
            print(str(index) + ",", end=" ")
            sys.stdout.flush()

            page = reader.getPage(index)
            content_object = page["/Contents"].getObject()
            content = ContentStream(content_object, reader)

            for operands, operator in content.operations:
                if operator == b_("Tj"):
                    text = operands[0]
                    if isinstance(text, str) and text.contains(texttag):
                        operands[0] = TextStringObject('')

            page.__setitem__(NameObject('/Contents'), content)
            writer.addPage(page)

        print("\nsave file: " + outfile)
        with open(outfile, "wb") as out_f:
            writer.write(out_f)
    print("end")


if __name__ == "__main__":
    texttag = "qq.com"
    readfile = r"xxx.pdf"
    outfile = r"xxxx_new.pdf"
    remove_text(texttag, readfile, outfile)
