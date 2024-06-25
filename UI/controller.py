import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        distanza=self._view.txt_distanza.value
        if distanza=="":
            self._view.create_alert("Inserire un distanza")
            return
        provider=self._view.dd_provider.value
        if provider is None:
            self._view.create_alert("Selezionare un provider")
            return
        grafo = self._model.creaGrafo(float(distanza), provider)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        self._view.update_page()

    def handle_analisi(self, e):
        ritorno=self._model.analisi()
        self._view.txt_result.controls.append(ft.Text("VERTICI CON PIU' VICINI"))
        for (nodo,vicini) in ritorno:
            self._view.txt_result.controls.append(ft.Text(f"{nodo},#vicini={vicini}"))
        self._view.update_page()
    def fillDD(self):
        provider=self._model.getProvider
        for prov in provider:
            self._view.dd_provider.options.append(ft.dropdown.Option(
                text=prov))
