import numpy as np
import fitz
from PIL import Image
# import bocr
# from utils import import_bocr

# import_bocr(vars())
if __name__ == "__main__":
    import sys
    sys.path.append('..')
    import bocr


class Page:
    def __init__(self, content):
        self.content = content

    def to_pil(self, zoom=1, rotate=0):
        trans = fitz.Matrix(zoom, zoom).prerotate(rotate)
        pix = self.content.get_pixmap(matrix=trans, alpha=False)
        height, width = pix.height, pix.width
        img = Image.frombytes('RGB', (width, height), pix.samples)
        return img

    @property
    def pil_image(self):
        return self.to_pil()

    def extract_original_text(self):
        return self.content.get_text()

    def extract_text(self, roi=None):
        """

        :param roi: 用于后续根据不同区域进行ocr，待实现
        :return:
        """
        image = np.asarray(self.pil_image)
        image_bocr = bocr.Image(image)
        ocr_result = image_bocr.basic_ocr()
        # print(ocr_result)

        t_ls = []
        if ocr_result.__len__() == 1:
            ocr_result = ocr_result[0]
        for text_candidate in ocr_result:
            points, (t, prob) = text_candidate
            p1, p2, p3, p4 = points
            x1, y1 = p1
            x2, y2 = p3
            t_ls.append(t)
        t_ls = '\n'.join(t_ls)
        return t_ls









class PDFReader:
    def __init__(self, filepath):
        self.file = fitz.open(filepath)
        self.page_count = self.file.page_count
        self.pages = [Page(self.file[i]) for i in range(self.page_count)]

    # @property
    # def pages(self):
    # return self.file


if __name__ == "__main__":
    import sys
    # sys.path.append('..')
    # import bocr

    # self test 1
    def self_test1():
        filepath = r'C:\Users\meiyan\Documents\ArUco与PnP问题解的可解性(R,t).pdf'
        reader = PDFReader(filepath)
        print(reader.pages[0])  # 证明用property+索引中括号的方法是可行的, 但是最终还是改了

    # self test 2
    def self_test2():
        filepath = '../data/古書堂事件手帖：扉子與不可思議的訪客 (三上延) (Z-Library).pdf'
        reader = PDFReader(filepath)
        for i in range(reader.page_count):
            page = reader.pages[i]
            text = page.extract_original_text()
            if text:
                print("第{}/{}页\n".format(i + 1, reader.page_count), text)
                break

    def self_test3():
        filepath = '../data/23唐迟-阅读方法论笔记.pdf'
        reader = PDFReader(filepath)
        for i in range(reader.page_count):
            page = reader.pages[i]
            text = page.extract_text()
            if text:
                print("第{}/{}页\n".format(i + 1, reader.page_count), text)
                break
    self_test3()
