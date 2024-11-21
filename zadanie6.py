# Pętla for jest używana, gdy wiemy, ile razy chcemy wykonać jakąś operację,
# na przykład gdy iterujemy po zbiorze, liście, zakresie itp. Pętla ta jest
# wygodna, gdy mamy określony zestaw danych lub liczbę powtórzeń.
for i in range(5):
    print(i)

# Pętla while jest używana, gdy chcemy, aby operacja była powtarzana dopóki
# nie spełni się jakiś warunek. Pętla ta jest bardziej elastyczna, bo możemy
# zatrzymać ją w dowolnym momencie, w zależności od wyniku warunku.
count = 0
while count < 5:
    print(count)
    count += 1
