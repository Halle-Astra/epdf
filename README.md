# pppdf

pppdf(PaddlePaddlePDF)项目是一个为了实现pdf内容提取的项目

阶段目标

1. 实现文字提取，实现pdf2txt;
2. 实现章节信息提取，转换为markdown格式;
3. 实现图片信息提取，转换为markdown格式;
4. 实现ipad笔记的提取(GoodNotes5)

## Requirements 

    fitz                               0.0.1.dev2
    PyMuPDF                            1.23.22
    PyMuPDFb                           1.23.22

<del>
## PyPDF

似乎这个库仅仅提供了对pdf的文本、图像、pdf本身，三个事物的解析，pdf本身的解析是指，依据pdf规范所允许的交叉引用与对象信息的解读，如果不是文本和标准图像，那么这样子的对象，PyPDF
只提供该对象的索引或box信息，而不帮你做该对象的读取与解析，而需要你自行去二进制读取处理。

为了更好的理解pdf中的非文本和非图像的对象，需要下载[pdftk工具](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/). **感觉这个工具似乎也没啥用**
</del>
