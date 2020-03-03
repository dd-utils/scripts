#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time : 2020-03-03
# @Author : Deming

from PyPDF2 import PdfFileReader, PdfFileWriter


def add_page(add_page_index, readfile, outfile):
    '''
    添加 pdf 指定页
    第一页 index 为 0
    '''
    print("read file: " + readfile)
    with open(readfile, "rb") as f:
        pdfFileWriter = PdfFileWriter()
        pdfReader = PdfFileReader(f)
        numPages = pdfReader.getNumPages()
        for index in range(0, numPages):
            if index == add_page_index:
                pageObj = pdfReader.getPage(index)
                pdfFileWriter.addPage(pageObj)
            pageObj = pdfReader.getPage(index)
            pdfFileWriter.addPage(pageObj)

        print("save file: " + outfile)
        with open(outfile, "wb") as out_f:
            pdfFileWriter.write(out_f)
    print("end")


if __name__ == "__main__":
    add_page_index = 0
    readfile = r"xxx.pdf"
    outfile = r"xxx_new.pdf"
    add_page(add_page_index, readfile, outfile)
