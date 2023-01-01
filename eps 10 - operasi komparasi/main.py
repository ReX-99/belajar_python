print("halo dunia")
print("apa kabar")

# operasi komparasi

# ada <, >, <=, >=, ==, !=,  is, is not

a = 4
b = 2

# lebih besar dari
print('==== lebih besar dari (>)')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil)

# lebih kecil dari
print('==== lebih kecil dari (<)')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil)

# lebih besar sama dengan dari
print('==== lebih besar sama dengan dari (>=)')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)

# lebih kecil sama dengan dari
print('==== lebih kecil sama dengan dari (<=)')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# sama dengan
print('==== sama dengan(==)')
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

# sama dengan
print('==== tidak sama dengan(!=)')
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)

# 'is' sebagai komparasi objek identitas/object identity
print('==== objek identitas(is)')
x = 5
y = 5
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(x)))
hasil = x is y
print('x is y =', hasil)

x = 5
y = 6
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(x)))
hasil = x is y
print('x is y =', hasil)

# kebalikan dari is
# 'is not' sebagai komparasi objek identitas/object identity
print('==== objek identitas(is not)')
x = 5
y = 5
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(x)))
hasil = x is not y
print('x is y =', hasil)

x = 5
y = 6
print('nilai x =', x, ',id = ', hex(id(x)))
print('nilai y =', y, ',id = ', hex(id(x)))
hasil = x is not y
print('x is y =', hasil)
