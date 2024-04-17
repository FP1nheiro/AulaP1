import tkinter as tk
from tkinter import ttk, messagebox  # Importa módulos necessários
import psutil  # Importa a biblioteca psutil para obter informações do sistema

# Função para finalizar um processo
def kill_process():
    # Obtém o item selecionado na Treeview
    selected_item = tree.selection()[0]
    # Obtém o PID (identificador de processo) do item selecionado
    pid = tree.item(selected_item)['values'][0]
    # Exibe uma caixa de diálogo de confirmação para finalizar o processo
    if messagebox.askyesno("Finalizar Processo", f"Tem certeza que deseja finalizar o processo {pid}?"):
        try:
            # Tenta obter o processo com base no PID
            p = psutil.Process(pid)
            # Termina o processo
            p.terminate()
            # Exibe uma mensagem informando que o processo foi finalizado com sucesso
            messagebox.showinfo("Processo", f"Processo {pid} foi finalizado.")
        except psutil.NoSuchProcess:
            # Se o processo não existe, exibe um aviso
            messagebox.showwarning("Aviso", "O processo não existe.")
        except psutil.AccessDenied:
            # Se o acesso ao processo for negado, exibe um aviso
            messagebox.showwarning("Aviso", "Acesso negado.")

# Função para obter informações detalhadas dos processos e atualizar a Treeview
def refresh_process_view():
    # Limpa a Treeview para atualização
    for row in tree.get_children():
        tree.delete(row)

    # Itera sobre todos os processos em execução
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'num_threads']):
        try:
            # Obtém informações do processo
            process_info = proc.info
            # Insere as informações do processo na Treeview
            tree.insert('', 'end', values=(
                process_info['pid'],
                process_info['name'],
                f"{process_info['cpu_percent']}%",
                f"{process_info['memory_percent']}%",
                process_info['num_threads']
            ))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Ignora processos que não podem ser acessados
            pass

    # Agenda a próxima atualização após 5 segundos
    root.after(5000, refresh_process_view)

# Função para pesquisar processos pelo nome
def search_process():
    # Obtém o termo de pesquisa inserido pelo usuário
    search_term = search_entry.get().lower()
    # Itera sobre os itens na Treeview para verificar se há correspondência com o termo de pesquisa
    for row in tree.get_children():
        values = tree.item(row)['values']
        # Compara o termo de pesquisa com o nome do processo (segunda coluna na Treeview)
        if search_term in values[1].lower():
            # Se houver correspondência, torna o item visível na Treeview, seleciona e foca nele
            tree.see(row)
            tree.selection_set(row)
            tree.focus(row)
        else:
            # Se não houver correspondência, remove a seleção do item
            tree.selection_remove(row)

# Configuração da GUI
root = tk.Tk()  # Cria a janela principal
root.title("Gerenciador de Tarefas Simplificado")  # Define o título da janela

# Frame principal para organizar os widgets
main_frame = ttk.Frame(root)
main_frame.pack(expand=True, fill=tk.BOTH)

# Configuração da Treeview para listar os processos
columns = ('PID', 'Nome', 'CPU', 'Memória', 'Threads')
tree = ttk.Treeview(main_frame, columns=columns, show='headings')
for col in columns:
    tree.heading(col, text=col)  # Define o texto do cabeçalho de cada coluna
tree.pack(expand=True, fill=tk.BOTH, side='left')  # Expande e preenche a Treeview

# Adiciona uma barra de rolagem à Treeview
scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(fill='y', side='right')
tree.configure(yscroll=scrollbar.set)

# Frame para a entrada de pesquisa
search_frame = ttk.Frame(root)
search_frame.pack(fill='x', padx=10, pady=5)
search_entry = ttk.Entry(search_frame)
search_entry.pack(side='left', expand=True, fill='x')  # Entrada para inserir termo de pesquisa
search_button = ttk.Button(search_frame, text='Pesquisar', command=search_process)
search_button.pack(side='left', padx=5)  # Botão para iniciar a pesquisa

# Botão para finalizar um processo selecionado
kill_button = ttk.Button(root, text='Finalizar Processo', command=kill_process)
kill_button.pack(fill='x', padx=10, pady=5)

# Inicializa a exibição de processos
refresh_process_view()  # Inicia a atualização da lista de processos na Treeview

root.mainloop()  # Inicia o loop principal da interface gráfica
