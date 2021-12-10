from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def get_stocked_products(data):
        list = Counter(p["nome_da_empresa"] for p in data)
        string_list = [
            f'- {company}: {list[company]}'
            for company in list
        ]
        result = 'Produtos estocados por empresa: \n'
        for string in string_list:
            result += f'{string}\n'
        return result

    @classmethod
    def generate(cls, data):
        # first_part = super().generate(data)
        first_part = SimpleReport.generate(data)
        second_part = CompleteReport.get_stocked_products(data)
        return f'{first_part}\n{second_part}'
