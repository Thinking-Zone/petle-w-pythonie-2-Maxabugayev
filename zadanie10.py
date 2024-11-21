# Zadanie:
# Napisz program, który wypisze wszystkie liczby od 1 do 50, ale:
# - jeśli liczba jest podzielna przez 3, wypisz "Fizz" zamiast liczby
# - jeśli liczba jest podzielna przez 5, wypisz "Buzz" zamiast liczby
# - jeśli liczba jest podzielna zarówno przez 3, jak i przez 5, wypisz "FizzBuzz"

print("A pod spodem rozwiązanie tego zadanka, napisane w Pythonie :)")

# Rozwiązanie:

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
