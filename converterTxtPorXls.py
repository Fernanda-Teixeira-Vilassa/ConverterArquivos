import os
import pandas as pd

# Nome do arquivo de entrada e saída
nome_arquivo_txt = 'arquivo.txt'
nome_arquivo_xlsx = 'arquivo.xlsx'  # Corrigido para xlsx se estiver usando o formato .xlsx

# Diretório atual
diretorio_atual = os.getcwd()

# Caminhos completos
caminho_arquivo_txt = os.path.join(diretorio_atual, nome_arquivo_txt)
caminho_arquivo_xlsx = os.path.join(diretorio_atual, nome_arquivo_xlsx)

# Lendo o arquivo txt e convertendo para Excel
dados = pd.read_csv(caminho_arquivo_txt, sep=';', header=None)
dados.to_excel(caminho_arquivo_xlsx, index=False, header=False)

# Mensagem de sucesso
print(f"Arquivo {nome_arquivo_txt} foi convertido para {nome_arquivo_xlsx} na pasta {diretorio_atual}.")


""" # Salvar os dados no arquivo .xls na mesma pasta
dados.to_excel(caminho_arquivo_xlsx, index=False, header=False, engine='xlwt') """

