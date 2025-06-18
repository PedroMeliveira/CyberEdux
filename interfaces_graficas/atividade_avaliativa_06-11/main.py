import requests
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap

API_KEY = "live_X0VC8vO09sobCOZ3l9Yf6Z9yiodN6qWVcs3UOFJelKsLemY3wk8XDawezczWhCNb"
BASE_URL = 'https://api.thedogapi.com/v1/breeds'

headers = {
    'x-api-key': API_KEY
}

class Dogs(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("interfaces_graficas/atividade_avaliativa_06-11/pexel_qtdesigner.ui", self)

        self.racas = []

        self.carregar_lista_racas()

        self.lista_racas.itemClicked.connect(self.carregar_detalhes_raca)

    def carregar_lista_racas(self):
        url = BASE_URL
        response = requests.get(url, headers=headers)
        self.racas = response.json()
        
        # print(response.json())
        self.lista_racas.clear()

        for raca in self.racas:
            self.lista_racas.addItem(raca['name'].capitalize())

    def carregar_detalhes_raca(self, item):
        nome = item.text().capitalize()
        url = next((r["url"] for r in self.racas if r["name"] == nome), nome)
        response = requests.get(url)
        data = response.json
        print(data)
        img_url = data

if __name__ == "__main__":
    app = QApplication([])
    janela = Dogs()
    janela.show()
    app.exec()


# dict_keys(['weight', 'height', 'id', 'name', 'country_code', 'bred_for', 'breed_group', 'life_span', 'temperament', 'origin', 'reference_image_id', 'image'])