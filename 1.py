
# Do zrobienia jest funkcja flatten która będzie wypłaszczać zagnieżdżone listy, czyli przykładowo,
# dostajemy listę
# [1, 2, [3, 4, [5, [6]], 7], 8, 9, 10],
# a w wyniku powinniśmy dostać
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# oczywiście liczba zagnieżdżeń
# może być dowolna i zakładamy, że elementem listy jest albo kolejna lista albo integer


def fun(x, y):
    return x + y

print(fun(2, 4))