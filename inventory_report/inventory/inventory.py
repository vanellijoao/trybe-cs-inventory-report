from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport
import csv
import json
import xml.etree.ElementTree as ElementTree


class Inventory:
    @staticmethod
    def import_csv_file(path):
        with open(path) as file:
            csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
            return [i for i in csv_file]

    @staticmethod
    def import_json_file(path):
        with open(path) as file:
            content = file.read()
            json_file = json.loads(content)
            return json_file

    @staticmethod
    def import_xml_file(path):
        tree = ElementTree.parse(path)
        root = tree.getroot()
        xml_file = []
        for item in root:
            dict_item = {}
            for child in item:
                dict_item[child.tag] = child.text
            xml_file.append(dict_item)
        return xml_file

    def import_data(path, type):
        dict_types = {"simples": SimpleReport, "completo": CompleteReport}
        file = ""

        if path.endswith(".csv"):
            file = Inventory.import_csv_file(path)
            return dict_types[type].generate(file)

        elif path.endswith(".json"):
            file = Inventory.import_json_file(path)
            return dict_types[type].generate(file)

        else:
            file = Inventory.import_xml_file(path)
            return dict_types[type].generate(file)

        return dict_types[type].generate(file)
