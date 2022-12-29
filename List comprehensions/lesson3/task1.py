import random

original_price = [random.randint(-100, 100) for _ in range(10)]
new_price = original_price[::]

for i in range(len(original_price)):
    if new_price[i] < 0:
        new_price[i] = 0

print("Мы потеряли:", abs(sum(original_price) - sum(new_price)))
