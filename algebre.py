
def factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

resultat = factors(10)
print(resultat)


def pgdc(num1, num2): # Plus grand dénominateur commun entre deux nombres
    factors1 = factors(num1)
    factors2 = factors(num2)
    common_factors = set(factors1).intersection(factors2)
    return max(common_factors)

num1 = 150
num2 = 138

resultat = pgdc(num1, num2)

print(f"Le PGDC de {num1} et {num2} est {resultat}")

