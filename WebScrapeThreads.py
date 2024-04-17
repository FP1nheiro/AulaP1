# Importa a biblioteca requests para fazer solicitações HTTP
import requests

# Importa a classe BeautifulSoup do módulo bs4 para analisar HTML
from bs4 import BeautifulSoup

# Importa o módulo time para medir o tempo de execução
import time

# Importa o módulo threading para trabalhar com threads
import threading

# Importa o módulo multiprocessing para trabalhar com processos
import multiprocessing

# Importa o módulo matplotlib.pyplot para criar gráficos
import matplotlib.pyplot as plt

# Lista de URLs para fazer o scraping
urls = [
    "https://en.wikipedia.org/wiki/Python_(programming_language)",
    "https://en.wikipedia.org/wiki/Java_(programming_language)",
    "https://en.wikipedia.org/wiki/JavaScript",
    "https://en.wikipedia.org/wiki/Ruby_(programming_language)",
    "https://en.wikipedia.org/wiki/Go_(programming_language)"
]

# Função para raspar o título da página
def scrape_title(url):
    print(f"Scraping {url}")  # Imprime a URL que está sendo raspada
    response = requests.get(url)  # Faz a solicitação HTTP para obter a página
    soup = BeautifulSoup(response.content, 'html.parser')  # Analisa o conteúdo HTML da página
    title = soup.find('title').get_text()  # Extrai o título da página
    print(title)  # Imprime o título da página

# Função para executar o scraping usando threads
def scrape_with_threads(urls):
    threads = []  # Lista para armazenar as threads
    start_time = time.time()  # Marca o tempo de início
    for url in urls:
        thread = threading.Thread(target=scrape_title, args=(url,))  # Cria uma nova thread
        threads.append(thread)  # Adiciona a thread à lista
        thread.start()  # Inicia a thread
    for thread in threads:
        thread.join()  # Aguarda todas as threads terminarem
    end_time = time.time()  # Marca o tempo de término
    resultTime = end_time - start_time
    print("{:.2f}".format(resultTime))
    return resultTime # Retorna o tempo total de execução

# Função para executar o scraping usando processos
def scrape_with_processes(urls):
    processes = []  # Lista para armazenar os processos
    start_time = time.time()  # Marca o tempo de início
    for url in urls:
        process = multiprocessing.Process(target=scrape_title, args=(url,))  # Cria um novo processo
        processes.append(process)  # Adiciona o processo à lista
        process.start()  # Inicia o processo
    for process in processes:
        process.join()  # Aguarda todos os processos terminarem
    end_time = time.time()  # Marca o tempo de término
    resultTime = end_time - start_time
    print("{:.2f}".format(resultTime))
    return resultTime # Retorna o tempo total de execução

# Função para plotar os resultados
def plot_results(thread_time, process_time):
    # Cria um gráfico de barras com os tempos de execução
    plt.bar(['Threads', 'Processes'], [thread_time, process_time], color=['blue', 'red'])
    plt.ylabel('Tempo de execução (s)')  # Adiciona rótulo ao eixo y
    plt.title('Comparação de Tempo de Execução: Threads vs. Processes')  # Adiciona título ao gráfico
    plt.show()  # Exibe o gráfico

# Ponto de entrada do programa
if __name__ == "__main__":
    # Executa o scraping com threads e processos
    thread_time = scrape_with_threads(urls)  # Tempo de execução com threads
    process_time = scrape_with_processes(urls)  # Tempo de execução com processos
    # Plota os resultados em um gráfico de barras
    plot_results(thread_time, process_time)
    # Imprime o tempo total de execução no console
    print("Tempo total com threads:", thread_time, "segundos")
    print("Tempo total com processos:", process_time, "segundos")
