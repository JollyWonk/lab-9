metals = {}
for i in range(9):
    metal = input(f"Введіть назву металу {i+1}: ")
    density = float(input(f"Введіть густину металу {metal}: "))
    metals[metal] = density

sorted_by_name = dict(sorted(metals.items()))

sorted_by_density = dict(sorted(metals.items(), key=lambda x: x[1], reverse=True))

middle_metal = list(sorted_by_density.items())[len(metals) // 2]

print("\nСловник, відсортований за алфавітом:", sorted_by_name)
print("Словник, відсортований за густиною (у порядку зменшення):", sorted_by_density)
print(f"Метал, що знаходиться посередині: {middle_metal[0]}, густина: {middle_metal[1]}")
