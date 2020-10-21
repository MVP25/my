a=[12,123,12,45,1,23,45,76]
a.append(59)
print(a)

b=a.copy()
print(b)

a.clear()
print(a)


b.insert(1,23)
print(b)

b.remove(1)
print(b)

b.sort()
print(b)

b.sort(reverse=True)
print(b)
