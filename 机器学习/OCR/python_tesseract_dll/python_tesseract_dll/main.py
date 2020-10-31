import ctypes

class OCR():

    def __init__(self, DLL_PATH, TESSDATA_PREFIX, lang):
        self.DLL_PATH = DLL_PATH
        self.TESSDATA_PREFIX = TESSDATA_PREFIX
        self.lang = lang
        self.ready = False
        if self.do_init():
            self.ready = True


    def do_init(self):
        self.tesseract = ctypes.cdll.LoadLibrary(self.DLL_PATH) #  DLL_PATH = 'libtesseract304.dll'
        self.tesseract.TessBaseAPICreate.restype = ctypes.c_uint64
        self.api = self.tesseract.TessBaseAPICreate()                    # TESSDATA_PREFIX = b'./tessdata'
        rc = self.tesseract.TessBaseAPIInit3(ctypes.c_uint64(self.api), self.TESSDATA_PREFIX, self.lang)
        if rc:
            self.tesseract.TessBaseAPIDelete(ctypes.c_uint64(self.api))
            print('Could not initialize tesseract.\n')
            return False
        return True

    def get_text(self, path):
        if not self.ready:
            return False
        self.tesseract.TessBaseAPIProcessPages(ctypes.c_uint64(self.api), path, None, 0, None)
        self.tesseract.TessBaseAPIGetUTF8Text.restype = ctypes.c_uint64
        text_out = self.tesseract.TessBaseAPIGetUTF8Text(ctypes.c_uint64(self.api))
        return bytes.decode(ctypes.string_at(text_out)).strip()


if __name__ == '__main__':
    DLL_PATH = 'libtesseract304.dll'
    TESSDATA_PREFIX = b'./tessdata'
    lang = b'eng'
    ocr = OCR(DLL_PATH, TESSDATA_PREFIX, lang)
    image_file_path = b'test.png'
    result = ocr.get_text(image_file_path)
    print(" --- > ",result)