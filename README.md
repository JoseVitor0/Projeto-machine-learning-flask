🚗 Predição de Consumo de Combustível com Machine Learning

Este projeto é uma aplicação web em Flask que utiliza algoritmos de Machine Learning para prever o consumo de combustível (MPG) de carros com base no peso do veículo, usando o famoso dataset Auto MPG.

O usuário pode escolher entre diferentes modelos de regressão e visualizar métricas de desempenho e um gráfico comparando valores reais e preditos.

🧠 Modelos de Machine Learning Utilizados

O sistema permite testar e comparar os seguintes regressores:

🔹 KNN Regressor

🔹 Support Vector Regressor (SVR)

🔹 MLP Regressor (Rede Neural)

🔹 Random Forest Regressor

Cada modelo é treinado no momento da execução, utilizando os mesmos dados para facilitar a comparação.

📊 Dataset

Nome: Auto MPG

Fonte: Dataset clássico de carros

Variáveis utilizadas no projeto:

weight → Peso do carro

mpg → Consumo em milhas por galão

⚠️ Neste projeto, apenas uma variável de entrada (peso) foi usada para simplificar a visualização e o entendimento dos modelos.

⚙️ Tecnologias e Bibliotecas

Python

Flask

Pandas

NumPy

Scikit-learn

Matplotlib

🖥️ Funcionalidades da Aplicação

Seleção do modelo de regressão via interface web

Treinamento automático do modelo escolhido

Cálculo das métricas:

📉 Mean Squared Error (MSE)

📈 R² Score

Geração de gráfico de dispersão:

Valores reais vs valores preditos

Exibição do gráfico diretamente no navegador

📂 Estrutura do Projeto
📁 projeto/
├── main.py
├── auto-mpg.csv
├── 📁 static/
  ├── style.css
  └── plot.png
├── 📁 templates/
│   ├── index.html
│   └── result.html
├── README.md

▶️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

2️⃣ Instale as dependências
pip install pandas flask numpy scikit-learn matplotlib

3️⃣ Execute a aplicação
python app.py

4️⃣ Acesse no navegador
http://127.0.0.1:5000/


🧪 Métricas de Avaliação

MSE (Mean Squared Error): mede o erro médio ao quadrado entre valores reais e preditos.

R² Score: indica o quanto o modelo consegue explicar a variabilidade dos dados.

📈 Visualização

O sistema gera um gráfico de dispersão onde:

⚫ Pontos pretos → valores reais

🔵 Pontos azuis → valores preditos pelo modelo

Isso ajuda a entender visualmente o desempenho de cada regressor.

🚧 Limitações e Possíveis Melhorias

Os hiperparâmetros são fixos (não configuráveis pelo usuário)

Apenas uma variável de entrada é utilizada

Poderia incluir:

Mais atributos do dataset

Ajuste de hiperparâmetros via interface

Comparação entre modelos na mesma tela

Deploy em ambiente cloud (Render, Railway, etc.)

📌 Objetivo do Projeto

Este projeto tem fins educacionais, com foco em:

Aprender regressão com Machine Learning

Integrar modelos ML com aplicações web

Visualizar métricas e resultados de forma simples

Se quiser, no próximo passo eu posso:

Adaptar
