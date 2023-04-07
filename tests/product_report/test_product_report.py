from inventory_report.inventory.product import Product


def test_relatorio_produto():
    mock_product = {
        "id": 1,
        "nome_do_produto": "Café",
        "nome_da_empresa": "Pilão",
        "data_de_fabricacao": "01-05-2021",
        "data_de_validade":  "01-05-2022",
        "numero_de_serie": "123456789",
        "instrucoes_de_armazenamento": "Em local seco e fresco",
    }

    product = Product(**mock_product)
    product_data = str(product)

    assert (isinstance(product_data, str)) is True
    assert (product_data) == (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )
