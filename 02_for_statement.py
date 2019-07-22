words = ['cat', 'windows', 'defenestrace']
for w in words:
   print (w, ', len:',  len(w))
for r in range(5):
   print(r)

a = ['Mary', 'Had', 'a', 'little', 'lamb']

# rangee
for l in range(len(a)):
  print(l, a[l])

print(range(10))
#range, break
for n in range (2, 10):
  for x in range (2, n):
   if n % x == 0:
        print(n, 'equals', x, '*', n // x)
        break
   else:
        print(n, 'is a prime number')


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number ", num)
        continue
    print("Found a numnber:", num)
