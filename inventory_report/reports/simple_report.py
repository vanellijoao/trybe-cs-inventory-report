from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def fab_date(data):
        oldest_fab_list = sorted(data, key=lambda d: d["data_de_fabricacao"])
        oldest_fab = oldest_fab_list[0]["data_de_fabricacao"]
        return f'Data de fabricação mais antiga: {oldest_fab}\n'

    @staticmethod
    def valid_date(data):
        still_valid_list = [
            product["data_de_validade"] for product in data
            if date.today() < date.fromisoformat(product["data_de_validade"])
        ]
        return f'Data de validade mais próxima: {min(still_valid_list)}\n'

    @staticmethod
    def product_by_company(data):
        companies = [
            product["nome_da_empresa"] for product in data
        ]
        sentence = "Empresa com maior quantidade de produtos estocados:"
        return f'{sentence} {max(Counter(companies))}\n'

    @classmethod
    def generate(cls, data):
        valid_date = SimpleReport.valid_date(data)
        fab_date = SimpleReport.fab_date(data)
        company = SimpleReport.product_by_company(data)
        return f'{fab_date}{valid_date}{company}'
