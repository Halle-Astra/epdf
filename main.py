# import PyPDF2
import  fitz
from PIL import Image

filepath = r'data/古書堂事件手帖：扉子與不可思議的訪客 (三上延) (Z-Library).pdf'

# doc = fitz.open(filepath)
# pass
# for page in doc:
#     pm = page.get_pixmap()
#     sample = pm.samples
#     w = pm.xres
#     h = pm.yres
#
# #
#
# import fitz
# from PIL import Image
#
# def convert_img(pdf, jpg):
#     doc = fitz.open(pdf)
#     img_bytes = b''
#     height = 0
#     width = 0
#     samples = b''
#     dpi = ()
#     for pg in range(doc.page_count):
#         page = doc[pg]
#         rotate = 0        #放大分辨率
#         zoom_x = 2.0
#         zoom_y = 2.0
#         # trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
#         pix = page.get_pixmap()#matrix=trans, alpha=False)
#         height += pix.height
#         width = pix.width
#         samples += pix.samples
#         dpi = (pix.xres, pix.yres)
#         img_bytes += pix.tobytes()
#         # break
#     img = Image.frombytes('RGB', (width, height), samples)
#     img.save(jpg, dpi=dpi)
#
#
# if __name__ == '__main__':
#     convert_img(filepath, 'test1.png')
#
# with open(r'C:\Users\meiyan\Documents\ArUco与PnP问题解的可解性(R,t).pdf', 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     num_pages = len(reader.pages)
#     cnt = 0
#     for i in range(num_pages):
#         images = reader.pages[i].images
#         if images:
#             for image in images:
#                 filename = "{}.png".format(cnt)
#                 with open(filename, 'wb') as f:
#                     f.write(image.data)
#                 f.close()
#                 cnt  += 1
