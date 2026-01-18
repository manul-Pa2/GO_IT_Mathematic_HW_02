# Задача №4 (4.1_4.2_4.3). Аналіз соціальної мережі компанії:

# Вхідні дані
raw_adj = {
    "Анна":   ["Богдан", "Віктор", "Ганна"],
    "Богдан": ["Анна", "Віктор", "Дмитро"],
    "Віктор": ["Анна", "Богдан", "Ганна", "Дмитро"],
    "Ганна":  ["Анна", "Віктор", "Євген"],
    "Дмитро": ["Богдан", "Віктор", "Євген"],
    "Євген":  ["Ганна", "Дмитро"],
}

# 1) Зробимо список вершин у фіксованому порядку
vertices = list(raw_adj.keys())

# 2) Побудуємо МНОЖИНУ ребер (без дублікатів), бо граф неорієнтований:
#    (u, v) і (v, u) — це одне й те саме ребро.
edges_set = set()
for u, nbrs in raw_adj.items():
    for v in nbrs:
        a, b = sorted((u, v))
        edges_set.add((a, b))

# 3) Список ребер (кортежів)
edges_list = sorted(edges_set)

# 4) Список суміжності (гарантуємо симетричність)
adj = {v: set() for v in vertices}
for u, v in edges_list:
    adj[u].add(v)
    adj[v].add(u)

# Перетворимо множини в відсортовані списки
adj_dict = {v: sorted(list(nbrs)) for v, nbrs in adj.items()}

# 5) Матриця суміжності (вкладені списки)
n = len(vertices)
index = {v: i for i, v in enumerate(vertices)}
matrix = [[0] * n for _ in range(n)]
for u, v in edges_list:
    i, j = index[u], index[v]
    matrix[i][j] = 1
    matrix[j][i] = 1      # симетрія для неорієнтованого графа

# ---------- Вивід результатів --------

# 1. Матриця суміжності
print("1) Матриця суміжності (порядок вершин):")
print("   ", vertices)
for i, row in enumerate(matrix):
    print(f"{vertices[i]:>7}:", row)

print("\n2) Список суміжності (словник):")
for v in vertices:
    print(f"{v:>7}: {adj_dict[v]}")

print("\n3) Список ребер (кортежів):")
print(edges_list)

# 2. Степінь кожної вершини
degrees = {v: len(adj[v]) for v in vertices}
print("\n2) Степені вершин:")
for v in vertices:
    print(f"{v:>7}: {degrees[v]}")

max_deg = max(degrees.values())
min_deg = min(degrees.values())
most = [v for v, d in degrees.items() if d == max_deg]
least = [v for v, d in degrees.items() if d == min_deg]

print(f"\nНайбільш комунікабельні (степінь {max_deg}): {', '.join(most)}")
print(f"Найменш комунікабельні (степінь {min_deg}): {', '.join(least)}")

# 3. Перевірка теореми про суму степенів
sum_degrees = sum(degrees.values())
m = len(edges_list)
print("\n3) Перевірка теореми про суму степенів:")
print("Сума степенів усіх вершин:", sum_degrees)
print("Кількість ребер:", m)
print("2 * кількість ребер:", 2 * m)
print("Рівність виконується?" , sum_degrees == 2 * m)
