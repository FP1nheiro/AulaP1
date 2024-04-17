# Descrição dos Scripts Python

Este repositório contém três scripts Python desenvolvidos para diferentes propósitos: correção de texto, gerenciamento de processos e raspagem de dados da web com múltiplas threads e processos. Cada script demonstra o uso de bibliotecas específicas e técnicas de programação em Python.

## Arquivos

1. **main.py** - Corretor ortográfico multithread
2. **TaskManager.py** - Gerenciador de processos de sistema
3. **WebScrapeThreads.py** - Raspador de dados web com comparação de desempenho entre threads e processos

### 1. main.py

Utiliza um corretor ortográfico para corrigir textos inseridos pelo usuário. O script divide o texto em palavras e cada palavra é corrigida em uma thread separada, demonstrando o uso de programação concorrente.

#### Funcionalidades:
- Correção de texto em português usando `spellchecker`.
- Execução paralela com `ThreadPoolExecutor`.

### 2. TaskManager.py

Interface gráfica para gerenciamento de tarefas do sistema, permitindo ao usuário visualizar e terminar processos. Utiliza `tkinter` para a interface e `psutil` para manipulação de processos.

#### Funcionalidades:
- Listagem e gerenciamento de processos.
- Terminação segura de processos com controle de acesso.

### 3. WebScrapeThreads.py

Raspa títulos de websites comparando o desempenho entre usar threads e processos. O script é útil para entender as diferenças práticas entre concorrência e paralelismo.

#### Funcionalidades:
- Raspagem de dados utilizando `threading` e `multiprocessing`.
- Comparativo de tempo de execução entre threads e processos.
- Visualização de resultados com `matplotlib`.

## Pré-requisitos

Para executar os scripts, você precisará das seguintes bibliotecas:

```bash
pip install -r requirements.txt
