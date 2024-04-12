import argparse
import os
import sys

sys.path.append(os.getcwd())
from ezpdf.pdf import PDFReader
import tqdm

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--pdf", '-i', type=str,
                            help='the input pdf')
    arg_parser.add_argument('--output', '-o', type=str,
                            default='',
                            help='the output folder')
    args = arg_parser.parse_args()
    if not args.output:
        args.output = os.path.join('outputs',
                                   os.path.splitext(os.path.basename(args.pdf))[0]
                                   )

    if not os.path.exists(args.output):
        os.makedirs(args.output, exist_ok=True)

    reader = PDFReader(args.pdf)
    pages = reader.pages

    tqdm_bar = tqdm.tqdm(total=reader.page_count)
    for i in range(reader.page_count):
        png_path = os.path.join(args.output, '{}.png'.format(i))
        page_pil = pages[i].to_pil()
        page_pil.save(png_path)
        tqdm_bar.update()
    tqdm_bar.close()
