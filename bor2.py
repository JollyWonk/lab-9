K = set([i for i in range(-34, 45) if abs(i) % 10 == 4])

K = {i for i in K if i % 4 != 0}

print("Множина K після видалення чисел, що діляться на 4:", K)
