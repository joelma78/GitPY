class Inventario:
    def __init__(self):
        self.itens = []
    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item} adicionando ao inventario")
    def listar_itens(self):
        print("Itens do inventario")

        if not self.itens:
            print("O inventário está vazio")
        else:
         for i, item in enumerate(self.itens):
                    print(f"{i + 1}. {item}")


meu_inventario = Inventario()

meu_inventario.adicionar_item ("espada longa")
meu_inventario.adicionar_item ("escudo de madeira")
meu_inventario.adicionar_item ("poção de cura")
meu_inventario.adicionar_item ("flecha  (x20)")

meu_inventario.listar_itens()