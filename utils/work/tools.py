import os.path

from utils import constants


def get_file_type(file_name):
    result =  constants.File_TYPE_UNKNOWN
    if os.path.isfile(file_name):
        return result
    path_name,ext = os.path.splitext(file_name)
    ext = ext.lower()
    if ext in ('.png', '.jpg', '.gif', '.bmp'):
        result = constants.File_TYPE_IMG
    elif ext in ('.doc', '.docx'):
        result = constants.File_TYPE_DOC
    elif ext in ('.xls','.xlsx'):
        result = constants.File_TYPE_EXCEL
    elif ext in ('.ppt', '.pptx'):
        result = constants.File_TYPE_PPT
    return result