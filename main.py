from flask import Flask, jsonify

from vendedor import Vendedor

api = Flask(__name__)

if __name__ == "__main__":
    api.run(debug=True)

@api.route('/api')
def ola_mundo():
    return jsonify({'text':'Olá Mundo'})

@api.route('/api/hello_word')
def hello_word():
    return "Hello Word"

@api.route('/cpi/calcular_valor_receber/<nome>/<meses_contrato>/<valor_venda>', methods=['GET'])
def calcular_valor_receber(nome, meses_contrato, valor_venda):
    vendedor = Vendedor(nome, int(meses_contrato), float(valor_venda))
    perc_comissao = Vendedor.calcular_comissao()
    salario_base = Vendedor.calcular_salario_base()
    valor_receber = Vendedor.calcular_valor_receber()

    return jsonify({'perc_comissao': perc_comissao, 'salario_base': salario_base, 'valor_receber': valor_receber})