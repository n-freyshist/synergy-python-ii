# На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег.
# Одна лодка может выдержать не более m килограмм, при этом в лодку помещается не более 2 человек.
# Определите, какое минимальное число лодок нужно, чтобы перевезти на другой берег всех рыбаков.
# В первую строку вводится число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может выдержать одна лодка.
# Во вторую строку вводится число n (1 ≤ n ≤ 100) - количество рыбаков.
# В следующие N строк вводится по одному числу Ai (1 ≤ Ai ≤ m) - вес каждого путешественника.
# Программа должна вывести одно число - минимальное количество лодок, необходимое для переправки всех рыбаков на противоположный берег.


print("Введите грузоподъемность лодки (кг):")
capacity_kg = int(input())

print("Введите количество рыбаков:")
len_fishers = int(input())

fishers_weights = []
for i in range(len_fishers):
    print("Сколько весит рыбак #%d?" % i)
    w = int(input())
    if w > capacity_kg:
        raise ValueError("Рыбак весит слишком много, не получится перевезти его на другой берег.")
    fishers_weights.append(w)

fishers_weights.sort()
fishers_weights.reverse()

boats_counter = 0

while True:
    if len(fishers_weights) == 0:
        break

    if len(fishers_weights) == 1:
        boats_counter += 1
        break

    max_weight_for_second_fisher = capacity_kg - fishers_weights[0]
    for i in range(1, len(fishers_weights)):
        if fishers_weights[i] <= max_weight_for_second_fisher:
            fishers_weights.pop(i)
            break
    fishers_weights.pop(0)
    boats_counter += 1

print(boats_counter)

