from .importer import Importer
from ..inventory.inventory import Inventory


class XmlImporter(Importer):
    def import_data(path):
        if not path.endswith('xml'):
            raise ValueError('Arquivo inválido')
        return Inventory.import_xml_file(path)
