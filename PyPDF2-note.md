# PyPDF2-note

鉴于PyPDF2的images并不是《ArUco与PnP问题解的可解性(R,t).pdf》直接看到的图片，text里也没有， 因此开始学习[PDF规范](#reference).

pdf文件的文件构成

1. Header
2. Body
3. xref table
4. tailer

## Experiments



### header

    with open(r'C:\Users\meiyan\Documents\ArUco与PnP问题解的可解性(R,t).pdf', 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        print(reader.pdf_header)
    
    Out:
    '%PDF-1.7'

## <span id='reference'>Reference</span> 

1. https://helpx.adobe.com/cn/acrobat/using/pdf-conversion-settings.chromeless.html#about_pdf_x_pdf_e_and_pdf_a_standards
2. https://dhexx.cn/news/show-3268714.html?action=onClick
3. **https://pypdf.readthedocs.io/en/stable/dev/pdf-format.html**
4. [一个python读取pdf的text的示例](https://www.jb51.net/python/298351lkd.htm#_label3)