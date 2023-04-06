from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list_of_products):
        report = super().generate(list_of_products)
        report += "\nProdutos estocados por empresa:\n"

        empresas = []
        for product in list_of_products:
            empresas.append(product["nome_da_empresa"])

        estoque = Counter(empresas).most_common()
        for empresa, quantidade in estoque:
            report += f"- {empresa}: {quantidade}\n"

        return report
