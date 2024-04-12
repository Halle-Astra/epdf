from paddleocr import PaddleOCR


class Image:
    def __init__(self,image):
        self.image = image
        self.machine = self.init_machine()

    def init_machine(self, lang='zh'):
        lang_dict = {'zh':'ch'}
        lang = lang_dict[lang]
        machine = PaddleOCR(use_angle_cls=True, lang=lang)
        return machine


    def set_header_tailer_boxes(self, auto=False, boxes=None):
        if not auto:
            self.header_tailer_boxes = boxes
        else:
            self.header_tailer_boxes = self.detect_header_tailer_boxes(self.image)
            # boxes_num = len(boxes)
            # for box in boxes:
            #     x,y,w,h = box

    def detect_header_tailer_boxes(self):
        pass

    def basic_ocr(self, image=None, lang=None):
        """
        最基础的ocr识别接口
        :param image:
        :param lang: 用于后续的多语言选择，待实现
        :return:
        """
        if image is None:
            image = self.image
        res = self.machine.ocr(image)
        return res




