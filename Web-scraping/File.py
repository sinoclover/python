# # 对纯文本进行爬取
# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
#
# try:
#     textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')
#     print(textPage.read())
# except (HTTPError, URLError) as e:
#     print(e)
# except AttributeError:
#     print('There is nothing here')

# # 编码设置
# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
#
# try:
#     textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
#     print(str(textPage.read(), 'utf-8'))  # python默认把文本读为ASCII
# except (HTTPError, URLError) as e:
#     print(e)
# except AttributeError:
#     print('There is nothing here')

# # CSV读取
# from urllib.request import urlopen
# from urllib.error import HTTPError,URLError
# from io import StringIO
# import csv
#
# try:
#     data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
#     dataFile = StringIO(data)
#     csvReader = csv.reader(dataFile)
#
#     for row in csvReader:
#         print(row)
# except (HTTPError, URLError) as e:
#     print(e)
# except AttributeError:
#     print('There is nothing here.')

# # 将读取的CSV转换为字典类型
# from urllib.request import urlopen
# from urllib.error import HTTPError,URLError
# from io import StringIO
# import csv
#
# try:
#     data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
#     dataFile = StringIO(data)
#     dictReader = csv.DictReader(dataFile)
#
#     print(dictReader.fieldnames)
#
#     for row in dictReader:
#         print(row)
# except (HTTPError, URLError) as e:
#     print(e)
# except AttributeError:
#     print('There is nothing here.')

# # 将PDF读取为字符串
# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
# from pdfminer.pdfinterp import PDFResourceManager, process_pdf
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from io import StringIO
# from io import open
#
# def readPDF(pdfFile):
#     rsrcmgr = PDFResourceManager()
#     retstr =  StringIO()
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, laparams=laparams)
#
#     process_pdf(rsrcmgr, device, pdfFile)
#     device.close()
#
#     content = retstr.getvalue()
#     retstr.close()
#     return content
#
# try:
#     # pdfFile = urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
#     pdfFile = open('../Web-scraping/files/chinese.pdf', 'rb')
#     outputString = readPDF(pdfFile)
#     print(outputString)
#     pdfFile.close()
# except (HTTPError, URLError) as e:
#     print(e)
# except AttributeError:
#     print('There is nothing here.')

# 读取word的docx
from zipfile import ZipFile
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from io import BytesIO
from bs4 import BeautifulSoup

try:
    wordFile = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
    # 将word文档读成二进制文件对象
    wordFile = BytesIO(wordFile)
    # 对该文件对象进行解压
    document = ZipFile(wordFile)
    xml_content = document.read('word/document.xml')
    # print(xml_content.decode('utf-8'))
    wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'xml')
    textStrings = wordObj.findAll('w:t')

    for textElem in textStrings:
        closeTag = ''
        try:
            style = textElem.parent.previousSibling.find('w:pstyle')
            if style is not None and style['w:val'] == 'Title':
                print('<h1>')
                closeTag = '</h>'
        except AttributeError:
            pass
        print(textElem.text)
        print(closeTag)
except (HTTPError, URLError) as e:
    print(e)
except AttributeError:
    print('There are nothing here.')