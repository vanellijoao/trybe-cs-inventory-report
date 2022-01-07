from .importer import Importer
from ..inventory.inventory import Inventory


class JsonImporter(Importer):
    def import_data(path):
        if not path.endswith('json'):
            raise ValueError('Arquivo inválido')
        return Inventory.import_json_file(path)
