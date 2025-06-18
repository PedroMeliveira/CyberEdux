import requests
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap

class Pokemon(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaces_graficas/aula_06-11/pokemon.ui", self)
        self.pokemons = []

        self.carregar_lista_pokemon()

        self.lista_pokemon.itemClicked.connect(self.carregar_detalhes_pokemon)

    def carregar_lista_pokemon(self):
        url = "https://pokeapi.co/api/v2/pokemon?limit=500"
        response = requests.get(url)
        data = response.json()
        # print(data)
        self.pokemons = data["results"]
        # print(pokemons)
        self.lista_pokemon.clear()
        for pokemon in self.pokemons:
            self.lista_pokemon.addItem(pokemon["name"].capitalize())


    def carregar_detalhes_pokemon(self, item):
        name = item.text().lower()
        url = next((p["url"] for p in self.pokemons if p["name"] == name), None)
        print(url)
        response = requests.get(url)
        data = response.json()

        print(data["sprites"]["front_default"])

        img_url = data["sprites"]["front_default"]
        if img_url:
            img_data = requests.get(img_url).content
            pixmap = QPixmap()
            pixmap.loadFromData(img_data)
            self.label_img.setPixmap(pixmap)
            self.label_img.setScaledContents(True)
        else:
            self.label_img.clear()


        # self.label_img.setPixmap(img)
        self.label_name.setText(data["name"].capitalize())
        self.label_height.setText(f"Altura: {data['height']}")
        self.label_weight.setText(f"Peso: {data['weight']}")



if __name__ == "__main__":
    app = QApplication([])
    janela = Pokemon()
    janela.show()
    app.exec()