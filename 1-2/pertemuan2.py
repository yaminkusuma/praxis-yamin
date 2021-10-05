#Eksplore type data python

#type data string
x = ("Selamat pagi Indonesia")
print(type(x)) 

#type data float
x = 23.2
print(type(x))

#type data integer
x = 20
print(type(x))

#type data complex
x = 1j
print(type(x))

#type data list
nama_barang=["asus", "lenovo", "acer", "HP"]
print(type(nama_barang))
print(nama_barang)
print(nama_barang[0])

#type data tuple
x = ("asus", "lenovo", "acer", "HP")
print(type(x))

#type data range
x = range(9)
print(type(x))

#type data dict
datadiri= {
    "name" : "yamin kusuma", 
    "age" : 22
     }
print(datadiri)
print(type(datadiri))

#type data set
x = {"mangga", "nanas", "strobery"}
print(type(x))
print(x)

#type data frozenset
x = frozenset({"mangga", "nanas", "strobery"})
print(type(x))
print(x)

#type data boolean
x = True
print(x)

#type data bytes
x = b"selamat pagi indonesia"
print(type(x))
print(x)

#type data bytearray
x = bytearray(10)
print(x)

#type data memoryview
x = memoryview(bytes(5))
print(x)
print(type(x))


