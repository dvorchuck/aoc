import os
from typing import List, Tuple

DAY = os.path.basename(__file__).replace('.py', '')
input = open(f"input_{DAY}.txt").read()

input_v2 = input.split('\n')
input_size = {
    "rows": len(input_v2),
    "cols": len(input_v2[0])
}

MIN_HEIGHT = ord('a')

visits = [[None for _ in range(input_size['cols'])]
          for _ in range(input_size['rows'])]


def calculate_height(char: str):
    if char == 'S':
        char = 'a'
    elif char == 'E':
        char = 'z'

    return ord(char) - MIN_HEIGHT


def get_start_and_end():
    start = ()
    end = ()

    for row_id, row in enumerate(input_v2):
        for col_id, char in enumerate(row):

            if char == 'S':
                start = (row_id, col_id)
                if len(end) > 0:
                    return [start, end]

            if char == 'E':
                end = (row_id, col_id)
                if len(start) > 0:
                    return [start, end]


[start, end] = get_start_and_end()


class Node():
    children: List['Node']
    depth: int

    def __init__(self, row: int, col: int, parent: 'Node' = None) -> None:
        self.row = row
        self.col = col
        self.parent = parent
        self.height = calculate_height(input_v2[row][col])
        self.children = []
        self.depth = 0

        if parent != None:
            self.depth = self.parent.depth + 1

    def find_elder(self):
        parent: Node = self.parent
        row = self.row
        col = self.col

        while (True):
            if parent == None:
                return None
            if parent.row == row and parent.col == col:
                return parent

            parent = parent.parent

    def get_neighbours(self):

        adjecent_coordinates = [
            (self.row + 1, self.col),  # down
            (self.row - 1, self.col),  # up
            (self.row, self.col + 1),  # right
            (self.row, self.col - 1)  # left
        ]

        # remove out of bound coordinates
        correct_coordinates = []

        for id, coordinate in enumerate(adjecent_coordinates):
            if coordinate[0] < 0 or coordinate[1] < 0:
                continue
            if coordinate[0] >= input_size['rows']:
                continue
            if coordinate[1] >= input_size['cols']:
                continue

            correct_coordinates.append(coordinate)

        return correct_coordinates

    def add_children(self):

        if visits[self.row][self.col] == None:
            visits[self.row][self.col] = self.depth

        elif self.depth >= visits[self.row][self.col]:
            return

        else:
            visits[self.row][self.col] = self.depth

        neighbours = self.get_neighbours()

        for neighbour in neighbours:
            row = neighbour[0]
            col = neighbour[1]
            height = calculate_height(input_v2[row][col])

            if height <= self.height + 1:
                self.children.append(
                    Node(row, col, self)
                )


root = Node(start[0], start[1])


def part1():

    queue = []
    queue.append(root)

    while (len(queue) > 0):
        curr: Node = queue.pop(0)
        curr.add_children()

        # if curr.row == end[0] and curr.col == end[1]:
        #     return curr.depth

        queue.extend(curr.children)


# print(part1())
# print(visits[end[0]][end[1]])


# part 2


class Node_2():
    children: List['Node_2']
    depth: int

    def __init__(self, row: int, col: int, parent: 'Node_2' = None) -> None:
        self.row = row
        self.col = col
        self.parent = parent
        self.height = calculate_height(input_v2[row][col])
        self.children = []
        self.depth = 0

        if parent != None:
            self.depth = self.parent.depth + 1

    def get_neighbours(self):

        adjecent_coordinates = [
            (self.row + 1, self.col),  # down
            (self.row - 1, self.col),  # up
            (self.row, self.col + 1),  # right
            (self.row, self.col - 1)  # left
        ]

        # remove out of bound coordinates
        correct_coordinates = []

        for coordinate in adjecent_coordinates:
            if coordinate[0] < 0 or coordinate[1] < 0:
                continue
            if coordinate[0] >= input_size['rows']:
                continue
            if coordinate[1] >= input_size['cols']:
                continue

            correct_coordinates.append(coordinate)

        return correct_coordinates

    def add_children(self):

        if visits[self.row][self.col] == None:
            visits[self.row][self.col] = self.depth

        elif self.depth >= visits[self.row][self.col]:
            return

        else:
            visits[self.row][self.col] = self.depth

        neighbours = self.get_neighbours()

        for neighbour in neighbours:
            row = neighbour[0]
            col = neighbour[1]
            height = calculate_height(input_v2[row][col])

            if height + 1 >= self.height:
                self.children.append(
                    Node_2(row, col, self)
                )


root_2 = Node_2(end[0], end[1])


def part2():
    queue = []
    queue.append(root_2)

    lowest = None

    while (len(queue) > 0):
        curr: Node_2 = queue.pop(0)
        if curr.height == 0:
            if lowest == None:
                lowest = curr.depth
            if lowest > curr.depth:
                lowest = curr.depth

        curr.add_children()

        # if curr.row == end[0] and curr.col == end[1]:
        #     return curr.depth

        queue.extend(curr.children)

    return lowest

print(part2())
