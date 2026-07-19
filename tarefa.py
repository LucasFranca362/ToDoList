from datetime import datetime

class Tarefa:
    def __init__(self, titulo, descricao, data_vencimento, status="Pendente"):
        self.titulo = titulo 
        self.descricao = descricao 
        self.data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
        self.status = status

    def __repr__(self):
        return f"Tarefa(titulo = '{self.titulo}', descricao = '{self.descricao}', data_vencimento = '{self.data_vencimento.strftime('%d/%m/%Y')}', status = '{self.status}')"

    def marcar_concluida(self):
        self.status = "Concluída"

    def esta_atrasada(self):
        return datetime.now() > self.data_vencimento and self.status == "Pendente"
    
    def edit_titulo(self, titulo):
        self.titulo = titulo
    
    def edit_desc(self, descricao):
        self.descricao = descricao
    
    def edit_data(self, data):
        self.data_vencimento = datetime.strptime(data, "%d/%m/%Y")

    def detalhes(self):
        #status = "Atrasada" if self.esta_atrasada() else self.status
        if self.esta_atrasada():
            status = "Atrasada"
        else:
            status = self.status
        return (f"Título: {self.titulo}\nDescrição: {self.descricao}\nVencimento: {self.data_vencimento.strftime('%d/%m/%Y')}\nStatus: {self.status}")
