import argparse
from gerenciador import GerenciadorDeTarefas

def main():
    parser = argparse.ArgumentParser(description="To Do List em Python")

    subparsers = parser.add_subparsers(dest="comando", help = "Comandos Disponíveis")

    #Add nova tarefa
    parser_add = subparsers.add_parser("adicionar", help = "Adicionar uma nova tarefa")
    parser_add.add_argument("titulo", type = str, help = "Título da tarefa")
    parser_add.add_argument("descricao", type = str, help = "Descrição da tarefa")
    parser_add.add_argument("data_vencimento", type = str, help = "Data de Vencimento(no formato DD/MM/AAAA)")

    #listar Tarefas
    parser_list = subparsers.add_parser("listar", help = "Listar todas as tarefas")
    parser_list.add_argument("--status", choices = ["Pendente", "Concluída", "Vencida"], help = "Filtrar por status da tarefa")

    #Editar nova tarefa
    parser_edit = subparsers.add_parser("editar", help = "Editar uma tarefa")
    parser_edit.add_argument("indice", type = int, help = "Índice da tarefa para edição")
    parser_edit.add_argument("--titulo", type = str, help = "Novo Título da tarefa")
    parser_edit.add_argument("--descricao", type = str, help = "Nova Descrição da tarefa")
    parser_edit.add_argument("--data_vencimento", type = str, help = "Nova Data de Vencimento(no formato DD/MM/AAAA)")

    #Remover nova tarefa
    parser_remove = subparsers.add_parser("remover", help = "Remover uma tarefa")
    parser_remove.add_argument("indice", type = int, help = "Índice da tarefa a ser removida")

    #Marcar como concluída
    parser_conclude = subparsers.add_parser("concluir", help = "Marcar tarefa como concluída")
    parser_conclude.add_argument("indice", type = int, help = "Índice da tarefa que foi concluída")

    args = parser.parse_args()
    gerenciador = GerenciadorDeTarefas()

    if args.comando == "adicionar":
        gerenciador.add_tarefa(args.titulo, args.descricao, args.data_vencimento)
    elif args.comando == "editar":
        gerenciador.edit_tarefa(args.indice - 1, args.titulo, args.descricao, args.data_vencimento)
    elif args.comando == "remover":
        gerenciador.remove_tarefa(args.indice - 1)
    elif args.comando == "concluir":
        gerenciador.marcar_concluida(args.indice - 1)
    elif args.comando == "listar":
        gerenciador.listar_tarefas(args.status)
    else:
        parser.print_help()



if __name__ == "__main__":
    main()