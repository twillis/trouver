
from tika import unpack
from tika import config
import datetime
import mimetypes
import json

TIKA_MIME_TYPES = json.loads(config.getMimeTypes()).keys()


def detect_type(file_path):
    return mimetypes.guess_type(file_path)[0]


def is_supported_type(file_path):
    file_type = detect_type(file_path)
    return file_type and file_type.lower() \
        in TIKA_MIME_TYPES


def get_index_data(file_path):
    try:
        result = unpack.from_file(file_path)
        result['status'] = 'succeded'
    except Exception as e:
        print(file_path)
        print(e.__class__)
        result['error'] = str(e)
        result = {'status': 'failed'}
    result['file_path'] = file_path
    result['last_scanned'] = datetime.datetime.now().isoformat()
    if 'attachments' in result and len(result['attachments'].keys()):
        result['attachments'] = {k: v
                                 for k, v in result['attachments'].items()
                                 if v.__class__ is not bytes}
    return result
