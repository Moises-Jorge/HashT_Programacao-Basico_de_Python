# Projecto: Criador de Backups - Cria backup dos arquivos ou diretorios selecionado

# Parte 1: Janela para selecionar a pasta do nosso computador
    # Biblioteca para listar os arquivos que estao dentro da pasta que a gente quer fazer backup
import os
    # Biblioteca que nos permite criar uma janela (personalizada ou uma ja existente no sistema)
from tkinter.filedialog import askdirectory # askdiretory: funcao que permite abrir/selecionar uma pasta do computador
    # Biblioteca que nos permite copiar arquivos/directorios de um lugar para o outro
import shutil # Da para fazer essa copia com a bblioteca "os", mas a "shutil" possui muitas vantagens
    # Biblioteca para pegar e manipular data e tempo
import datetime

    # Armazenando o nome da pasta selecionada para se fazer o backup
nome_pasta_selecionada = askdirectory()

    # Listando todos os arquivos que estao dentro do directorio selecionado e armazenando eles numa lista
lista_arquivos = os.listdir(nome_pasta_selecionada)

# Parte 2: Fazer o backup dos arquivos que estao nessa pasta
    # Criando a pasta de backups:
nome_pasta_backup = "backup" # Esse eh o nome da pasta onde vao constar todos os backups
nome_completo_pasta_backup = f"{nome_pasta_selecionada}/{nome_pasta_backup}" # Esse vai ser o caminho onde a pasta se encontra
if not os.path.exists(nome_completo_pasta_backup): # Para nao criar a pasta backup sempre que rodar o codigo, vericamos se ela ainda nao existe.
    os.mkdir(nome_completo_pasta_backup)
    
    # Criando um directorio com a data e hora actualizada para armazenar cada backup
data_atual = datetime.datetime.today().strftime("%Y-%m-%d %H%M%S")

    # Passo 1: Percorrer toda lista de arquivos para poder fazer o backup
for arquivo in lista_arquivos:
        nome_completo_arquivo = f"{nome_pasta_selecionada}/{arquivo}" # Isso me da o caminho onde o arquivo se encontra
        nome_final_arquivo = f"{nome_completo_pasta_backup}/{data_atual}/{arquivo}" # Destino final da copia do arquivo (dentro de uma pasta com a "data e hora" do backup)
        
        if not os.path.exists(f"{nome_completo_pasta_backup}/{data_atual}"): # Para nao criar a pasta com a "data e hora" do backup, dentro da pasta backups sempre que rodar o codigo, vericamos se ela ainda nao existe.
            os.mkdir(f"{nome_completo_pasta_backup}/{data_atual}")
        
        if "." in arquivo: # Se for um ficheiro (soh ficheiro possuem pontos para determinar a extensao)
            shutil.copy2(nome_completo_arquivo, nome_final_arquivo) # o Copy2 soh copia ficheiros, por isso a verificacao antes da copia
        elif "backup" != arquivo: # Se nao for um ficheiro, entao eh uma pasta, e se for uma pasta, nao pode ser a propria pasta de "backups". 
            shutil.copytree(nome_completo_arquivo, nome_final_arquivo) # copytree copia a arvore toda (desde a pasta raiz ate as subpastar e seus conteudos)