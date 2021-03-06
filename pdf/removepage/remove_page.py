#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Time : 2020-03-03
# @Author : Deming

from PyPDF2 import PdfFileReader, PdfFileWriter


def remove_page(remove_page_list, readfile, outfile):
    '''
    删除 pdf 指定页
    第一页 index 为 0
    '''
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
    remove_page_list = (0, )
    readfile = r"0_wrapper.pdf"
    outfile = r"0_wrapper_new.pdf"
    remove_page(remove_page_list, readfile, outfile)
