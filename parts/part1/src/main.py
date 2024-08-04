# main.py
import pygame
from math import sin, cos, pi

class Object3d:
    def __init__(self,
                    vertices: list[list[float]],
                    edges: list[list[int]],
                    faces: list[list[int]],
                    position: list[float]) -> None:
        self.vertices = vertices
        self.edges = edges
        self.faces = faces
        self.position = position
    def draw(self, surface: pygame.Surface) -> None:
        halfWidth = surface.get_width() / 2
        halfHeight = surface.get_height() / 2
        verts = [
            [
                o[u] * 50 + self.position[u] for u in range(3)
            ] for o in self.vertices]
        for edge in self.edges:
            point1Div = verts[edge[0]][2] / 400
            if point1Div == 0:
                continue
            point2Div = verts[edge[1]][2] / 400
            if point2Div == 0:
                continue
            point1 = [
                verts[edge[0]][0] / point1Div + halfWidth,
                verts[edge[0]][1] / point1Div + halfHeight
            ]
            point2 = [
                verts[edge[1]][0] / point2Div + halfWidth,
                verts[edge[1]][1] / point2Div + halfHeight
            ]
            pygame.draw.line(surface, (255, 255, 255), point1, point2)

class Cube(Object3d):
    vertices: list[list[float]] = [
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ]
    edges: list[list[int]] = [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0],
        [4, 5],
        [5, 6],
        [6, 7],
        [7, 4],
        [0, 4],
        [1, 5],
        [2, 6],
        [3, 7]
    ]
    faces: list[list[int]] = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [0, 1, 5, 4],
        [1, 2, 6, 5],
        [2, 3, 7, 6],
        [3, 0, 4, 7]
    ]
    def __init__(self, position: list[float]) -> None:
        super().__init__(Cube.vertices, Cube.edges, Cube.faces, position)

window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("3d Graphics")
done = False

cube = Cube([0, 0, 150])

ticks = 0

while not done:
    pygame.draw.rect(window, (0, 0, 0), (0, 0, 1280, 720))
    cube.position[0] = sin((ticks * pi / 180) / 8) * 50
    cube.position[1] = cos((ticks * pi / 180) / 8) * 50
    cube.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()
    ticks += 1

exit()