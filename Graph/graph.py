from typing import Callable, Dict, List, Optional, Any
from enum import Enum


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    '''
    data: Any
    index: int
    '''
    def __init__(self, data: Any, index: int) -> None:
        self.data = data
        self.index = index
    
    def __repr__(self) -> str:
        return f"{self.index}: {self.data}"


class Edge:
    '''
    source: Vertex
    destination: Vertex
    weight: Optional[float]
    '''

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight
        
    def __repr__(self) -> str:
        return f'{self.destination}'


class Graph:

    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self) -> None:
        self.adjacencies = dict()

    def create_vertex(self, data: Any) -> Vertex:
        new_vertex = Vertex(data, len(self.adjacencies))
        self.adjacencies[new_vertex] = list()
        return new_vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        new_edge = Edge(source, destination, weight)
        self.adjacencies[source].append(new_edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == edge.directed:
            self.add_directed_edge(source, destination, weight)
        if edge == edge.undirected:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        pass

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        pass

    def show(self):
        pass


class GraphPath:
    pass