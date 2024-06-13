class Album:
    def __init__(self, titulo, ano, lista):
        self.titulo = titulo
        self.ano = ano
        self.lista = lista

    def mostrar_info(self):
        print(f'titulo: {self.titulo} \nano: {self.ano}\nlista: {self.lista}')
