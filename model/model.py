import networkx as nx

from database.DAO import DAO
import geopy
from geopy.distance import geodesic

class Model:
    def __init__(self):
        self.getProvider=DAO.getProvider()
        self.grafo = nx.Graph()
        self._idMap={}

    def creaGrafo(self, distanza,provider):
        self.nodi = DAO.getNodi(provider)
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges(distanza)
        for v in self.nodi:
            self._idMap[v.location] = v
        return self.grafo

    def addEdges(self, distanza):
        self.grafo.clear_edges()
        for nodo1 in self.grafo:
            for nodo2 in self.grafo:
                if nodo1 != nodo2 and self.grafo.has_edge(nodo1, nodo2) == False:
                    posizione1 = (nodo1.lat, nodo1.lng)
                    posizione2 = (nodo2.lat, nodo2.lng)
                    distanzaCalcolata= geopy.distance.distance(posizione1, posizione2).km
                    if distanzaCalcolata <= distanza:
                        self.grafo.add_edge(nodo1, nodo2, weight=abs(distanzaCalcolata))

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def analisi(self):
        dizio={}
        ritorno=[]
        for nodo in self.grafo.nodes:
            dizio[nodo.location]=self.grafo.degree(nodo)
        dizioOrdinato=list(sorted(dizio.items(), key=lambda item:item[1],reverse=True))
        nmax=dizioOrdinato[0][1]
        for nodo in dizio.keys():
            if dizio[nodo]==nmax:
                ritorno.append((nodo, dizio[nodo]))
        return ritorno
