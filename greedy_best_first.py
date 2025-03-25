# -*- coding: utf-8 -*-
"""greedy_best_first.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SZEeZtvXgiGDozEBfTzgFVgfdPYHgEgm
"""

from queue import PriorityQueue

# Fungsi untuk algoritma Greedy Search
def greedy_search(graph, start, goal):
    frontier = PriorityQueue()  # Antrian prioritas untuk menyimpan simpul yang akan dieksplorasi
    frontier.put((heuristic[start], start))  # Menambahkan simpul awal ke dalam antrian dengan nilai heuristik
    explored = set()  # Set untuk menyimpan simpul yang sudah dieksplorasi
    path = {}

    while not frontier.empty():
        current_priority, current = frontier.get()  # Ambil simpul dengan prioritas terendah

        if current == goal:
            print("Greedy Best First")
            print("Simpul tujuan sudah ditemukan!")
            route = reconstruct_path(path, start, goal)
            print("Jalur terpendek:", route)
            return True

        explored.add(current)  # Menandai simpul saat ini sebagai sudah dieksplorasi

        for neighbor in graph[current]:
            if neighbor not in explored and neighbor not in path:  # Pastikan neighbor belum dieksplorasi dan belum ada di path
                priority = heuristic[neighbor]  # Menggunakan nilai heuristik untuk menentukan prioritas
                frontier.put((priority, neighbor))  # Menambahkan simpul tetangga ke dalam antrian dengan nilai prioritas heuristik
                path[neighbor] = current

    print("Simpul tujuan tidak ditemukan!")
    return False  # Mengembalikan False jika simpul tujuan tidak ditemukan

def reconstruct_path(path, start, goal):
    current = goal
    route = [current]
    while current != start:
        current = path[current]
        route.append(current)
    route.reverse()
    return route

# Daftar heuristik untuk setiap simpul
heuristic = {
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 1,
    'S': 6,
    'G': 0
}

# Graf (dalam bentuk daftar kejadian)
graph = {
    'S': ['A', 'B'],
    'A': ['B', 'D'],
    'B': ['D','C'],
    'C': ['D','G'],
    'D': ['G']
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi greedy search
greedy_search(graph, start_node, goal_node)