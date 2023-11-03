from flask import Flask, render_template, request
from caxeiroViajante import calcular_rota


# Crie uma instância do aplicativo Flask
app = Flask(__name__,
            static_url_path="/Public",
            static_folder='Public')

# Crie uma rota básica para a página inicial
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    show_response_div = False  # Defina esta variável como True ou False com base na lógica da sua aplicação
    show_Palmeiras =False
    return render_template('index.html', show_response_div=show_response_div , show_Palmeiras=show_Palmeiras)
"""Rota recebe os valores e enviados de index para montar a matriz e calcular a solução inicial
    a calcula a melhor rota para os aeroportos com o custo
"""
"""Retorna das matrizes criadas pelo teste caxeiro viajante """
@app.post('/caxeiroViajante')
def caxeiroViajante():
  total_elementos = int(request.form['total_elementos'])
  min_matriz1 = int(request.form['min_matriz1'])
  max_matriz1 = int(request.form['max_matriz1'])

  _solInicial, _ValorSolInicial, _solucaoAtual, _valorAtual,_solucaoAtualAlterada, _valorAtualAlterada   = calcular_rota(total_elementos,min_matriz1,max_matriz1)

  show_response_div = True

  return render_template('index.html',
                         show_response_div = show_response_div,
                         solInicial = _solInicial,
                         ValorSolInicial = _ValorSolInicial,
                         SolucaoAtual = _solucaoAtual,
                         ValAtual = _valorAtual,
                         solucaoAtualAlterada=_solucaoAtualAlterada,
                         valorAtualAlterada=_valorAtualAlterada
                        )

@app.route('/imagem')
def chamaImagem():
  return render_template('logo.html')

if __name__ == '__main__':
    app.run(debug=True)
