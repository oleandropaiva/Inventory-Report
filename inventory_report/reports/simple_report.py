from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list_of_products):
        datas_de_fabricacao = []
        for product in list_of_products:
            datas_de_fabricacao.append(product["data_de_fabricacao"])
        print(datas_de_fabricacao)

        datas_de_validade = []
        for product in list_of_products:
            datas_de_validade.append(product["data_de_validade"])

        empresas_mais_produtos = []
        for product in list_of_products:
            empresas_mais_produtos.append(product["nome_da_empresa"])

        data_mais_antiga = min(datas_de_fabricacao)
        data_mais_recente = min(datas_de_validade)
        nome_da_empresa = Counter(empresas_mais_produtos).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {data_mais_antiga}\n"
            f"Data de validade mais próxima: {data_mais_recente}\n"
            f"Empresa com mais produtos: {nome_da_empresa}"
        )
