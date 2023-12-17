from collections import Counter

a = [1, 2, 1, 3, 1, 4, 1, 0, 2, 5]
b = Counter(a)
print(b)

string = 'java python php c++ c c#'
ans = list(dict(Counter(string)).items())
print(ans)