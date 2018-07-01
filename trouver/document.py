from elasticsearch_dsl import DocType as ESDoc, Text as ESText, Date as ESDate
from .indexer import get_index_data
import os


class Document(ESDoc):
    class Meta:
        index = 'trouver-documents'
    content = ESText(analyzer='snowball')
    title = ESText()
    content_type = ESText()
    file_path = ESText()
    status = ESText()
    last_scanned = ESDate()

    @classmethod
    def create_from_file_path(cls, file_path):
        scanned = get_index_data(file_path)
        result = cls()
        result.content = scanned['content']
        result.title = get_title(scanned)
        result.content_type = scanned['metadata']['Content-Type']
        result.file_path = scanned['file_path']
        result.status = scanned['status']
        result.last_scaned = scanned['last_scanned']
        result.meta.id = file_path
        result.save()
        return result


TITLE_KEYS = ['title', 'dc:title', 'resourceName']


def get_title(scanned):
    candidates = {k: v
                  for k, v in scanned['metadata'].items()
                  if k in TITLE_KEYS}
    return next((candidates[k]
                 for k in TITLE_KEYS
                 if k in candidates and candidates[k]),
                os.path.basename(scanned['file_path']))
