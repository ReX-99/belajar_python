from ctypes import c_double
print("halo dunia")
print("apa kabar")

# tipe data tidak perlu dipanggil, bisa langsung menggunakan
# tipe data yang diperlukan

# tipe data: integer (angka)
data_integer = 10
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# tipe data: float (angka dengan koma)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# tipe data: string (karakter (bisa memakai angka))
data_string = "john 100"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# tipe data: boolean (true / false)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

# tipe data khusus

# bilangan kompleks
data_complex = complex(5, 6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# tipe data dari c++
data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
