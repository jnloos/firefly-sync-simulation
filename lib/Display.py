from abc import abstractmethod
from tkinter import Place

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import time


class Display:
    graph = None
    topo = None

    def __init__(self, topology):
        self.topo = topology
        self.graph = nx.Graph()

    def insert(self, node):
        self.topo.insert(graph=self.graph, node_id=node)

    def recolor(self, node_id, color):
        if node_id in self.graph.nodes:
            nx.set_node_attributes(self.graph, {node_id: color}, 'color')

    def show(self):
        matplotlib.use('TkAgg')
        nx.draw(self.graph)
        plt.show()


class Bulb:
    ref = None
    display = None

    def __init__(self, ref):
        if Bulb.display is None:
            Bulb.display = Display(topology=Plane())
        Bulb.display.insert(ref)
        self.ref = ref

    def turn_on(self, sec=None):
        Bulb.display.recolor(node_id=self.ref, color='tab:yellow')
        if sec is not None:
            time.sleep(sec)
            Bulb.display.recolor(node_id=self.ref, color='tab:black')

    def turn_off(self, sec=None):
        Bulb.display.recolor(node_id=self.ref, color='tab:black')
        if sec is not None:
            time.sleep(sec)
            Bulb.display.recolor(node_id=self.ref, color='tab:yellow')


class Topology:
    @abstractmethod
    def insert(self, display, node_id):
        pass


class Plane(Topology):
    def insert(self, graph, node_id):
        graph.add_node(node_id)


class Torus(Topology):
    def insert(self, display, node_id):
        # TODO: implement insertion logics
        pass

bulbs = {}
for i in range(1):
    bulbs[i] = Bulb(i)
Bulb.display.show()