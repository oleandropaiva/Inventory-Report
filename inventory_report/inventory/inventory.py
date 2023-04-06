from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        if report_type == "simples":
            return SimpleReport.generate(Inventory.file_read(path))
        elif report_type == "completo":
            return CompleteReport.generate(Inventory.file_read(path))
        else:
            raise ValueError("Tipo de relatório inválido!")

    @staticmethod
    def file_read(path):
        with open(path, "r") as file:
            return list(csv.DictReader(file))
