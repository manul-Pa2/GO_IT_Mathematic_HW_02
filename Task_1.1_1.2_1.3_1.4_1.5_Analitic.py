import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# 1) Данні
rock_fans = {101, 102, 103, 105, 107, 109, 110, 112, 115, 118}
pop_fans  = {102, 104, 105, 106, 108, 110, 111, 113, 115, 117}
jazz_fans = {103, 105, 108, 110, 112, 114, 115, 116, 119, 120}

# 1) Загальне охоплення
all_unique = rock_fans | pop_fans | jazz_fans

# 2) Слухали всі три жанри
melomani_all3 = rock_fans & pop_fans & jazz_fans

# 3) Рокери
pure_rockers = rock_fans - (pop_fans | jazz_fans)

# 4) Рівно два жанри (але не всі три)
exactly_two = (
    ((rock_fans & pop_fans) - jazz_fans) |
    ((rock_fans & jazz_fans) - pop_fans) |
    ((pop_fans & jazz_fans) - rock_fans)
)

print("1) Загальне охоплення:", len(all_unique), sorted(all_unique))
print("2) Всі три жанри:", len(melomani_all3), sorted(melomani_all3))
print("3) Чисті рокери:", len(pure_rockers), sorted(pure_rockers))
print("4) Рівно два жанри:", len(exactly_two), sorted(exactly_two))

# Візуал (діаграмма Венна)
plt.figure(figsize=(7, 5))
venn3([rock_fans, pop_fans, jazz_fans], set_labels=("Rock", "Pop", "Jazz"))
plt.title("Перетини аудиторій за жанрами")
plt.tight_layout()
plt.show()

#__________ Results __________
# 1) Загальних кристувачів - 20 (ID: [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120])
# 2) Слухали всі 3 жанри - 3  (ID: [105, 110, 115])
# 3) Рокери - 4  (ID: [101, 107, 109, 118])
# 4) Слухали 2 жанри (будб-які) - 4  (ID: [102, 103, 108, 112])
# Діаграма з перетином аудиторії у доп .jpg з назвою "Task_1"!
