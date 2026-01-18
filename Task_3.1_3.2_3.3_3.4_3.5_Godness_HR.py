import math

# Кількість кандидатів
backend = 8      # C1
frontend = 6     # C2
designers = 4    # C3

# Скільки треба взяти
need_backend = 2
need_frontend = 2
need_designers = 1

# 1) Способи вибрати Back-end
ways_backend = math.comb(backend, need_backend)

# 2) Способи вибрати Front-end
ways_frontend = math.comb(frontend, need_frontend)

# 3) Способи вибрати дизайнера
ways_designers = math.comb(designers, need_designers)

# 4) Загальна кількість команд (правило множення)
total_teams = ways_backend * ways_frontend * ways_designers

# 5) Вивід результатів
print(f"Back-end: C({backend}, {need_backend}) = {ways_backend}")
print(f"Front-end: C({frontend}, {need_frontend}) = {ways_frontend}")
print(f"Designers: C({designers}, {need_designers}) = {ways_designers}")
print("-" * 40)
print(f"Загальна кількість унікальних команд: {total_teams}")

# Tests: C1(8,2)=28  C2(6,2)=15  C3(4,1)=4

# Загалом: 28*15*4=1680 унікальних складів команди.
