#importação de todas as bibliotecas necessárias;

import pandas as pd
from flask import Flask, render_template, request
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from io import BytesIO
import base64

#inciando a aplicação flask
app = Flask(__name__)

#fazendo a leitura do dataset: auto-mpg, o qual tem dados de carros, como: peso, potencia, consumo, cilindros, entre outros;
database = pd.read_csv("auto-mpg.csv")

#selecionando as colunas desejadas, "weight" (peso do carro) e "mpg" (consumo do carro em milhas por galão)
X = database["weight"]
y = database["mpg"]

#na hora de compilar estava dando um erro em relação a dimensão do X, estava unidirecional 1D, essa função deixa ele bidimensional 2D
X = np.array(X).reshape(-1, 1)

#dividindo o conjunto de dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#padronizando os dados (média=0 e desvio padrão=1)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#aqui optei por fazer um dicionário com os regressores, pois seria mais facil de usar cada um nas funções posteriormente
#os parametros de cada um foram definidos estaticamente, pois não consegui implementar uma maneira de serem inputados pelo usuário
regressors = {
    'KNN': KNeighborsRegressor(n_neighbors=10),
    'SVR': SVR(kernel='linear'),
    'MLP': MLPRegressor(hidden_layer_sizes=(100, 50, 25), max_iter=800, random_state=42),
    'Random Forest': RandomForestRegressor(n_estimators=1000, random_state=42)
}

#rota principal, a que o usuário é recebido
@app.route('/')
def index():
    return render_template('index.html', regressors=regressors.keys())

#rota onde os resultados serão exibidos
@app.route('/result', methods=['POST'])
def result():
    #pega o regressor que o usuario escolheu
    selected_regressor = request.form.get('regressor')

    #selecionando o regressor escolhido
    regressor = regressors[selected_regressor]

    #treinando o modelo
    regressor.fit(X_train, y_train)

    #fazendo previsões no conjunto de teste
    y_pred = regressor.predict(X_test)

    #métricas
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    #resultados do learning, serão exibidos na página de resultados
    results = {
        'Regressor': selected_regressor,
        'Mean Squared Error (MSE)': f'{mse:.2f}',
        'R-squared (R2)': f'{r2:.2f}'
    }

    #gerando e salvando a imagem do gráfico de dispersão
    fig, ax = plt.subplots()
    ax.scatter(X_test, y_test, color='black', label='Real')
    ax.scatter(X_test, y_pred, color='blue', linewidth=3, label='Predito')
    plt.xlabel('Peso do Carro')
    plt.ylabel('Consumo (MPG)')
    plt.title(f'Regressão - {selected_regressor}')
    plt.legend()

    #convertendo a imagem para base64 para exibir na página HTML
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf8')

    plt.close()

    return render_template('result.html', results=results, scatter_plot=img_base64)

if __name__ == '__main__':
    app.run(debug=True)
