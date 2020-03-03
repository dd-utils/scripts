#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time : 2020-03-03
# @Author : Deming

from PyPDF2 import PdfFileReader, PdfFileWriter

remove_page_list = (0, )
readfile = r"xxxxx.pdf"
outfile = r"xxxxx_new.pdf"


def remove_page():
    print("read file: " + readfile)
    with open(readfile, "rb") as f:
        pdfFileWriter = PdfFileWriter()
        pdfReader = PdfFileReader(f)
        numPages = pdfReader.getNumPages()
        for index in range(0, numPages):
            if index not in remove_page_list:
                pageObj = pdfReader.getPage(index)
                pdfFileWriter.addPage(pageObj)

        print("save file: " + outfile)
        with open(outfile, "wb") as out_f:
            pdfFileWriter.write(out_f)
    print("end")


if __name__ == "__main__":
    remove_page()
