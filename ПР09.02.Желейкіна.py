A = set(range(1, 251))

number = int(input("Введіть число для видалення його дільників з множини A: "))

divisors = {x for x in A if x % number == 0}

A.difference_update(divisors)

print(A)