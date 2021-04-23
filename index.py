# Belajar Cesting ,Cesting Merupakan mengubah tipe data

print("============INTEGER=================")

data_int = 10;
print("data : ",data_int,", Type = ",type(data_int))

data_float=float(data_int)
data_string=str(data_int)
data_bool=bool(data_int) #benilai FALSE jika nilai tersebut 0 dan selai 0 maka TRUE
print("data : ",data_int,", Type = ",type(data_float))
print("data : ",data_int,", Type = ",type(data_string))
print("data : ",data_int,", Type = ",type(data_bool))

print("============FLOAT=================")

data_float = 10.9;
print("data : ",data_float,", Type = ",type(data_float))

data_int=int(data_float)
data_string=str(data_float)
data_bool=bool(data_float)
print("data : ",data_int,", Type = ",type(data_int))
print("data : ",data_string,", Type = ",type(data_string))
print("data : ",data_bool,", Type = ",type(data_bool))


print("============BOOLEAN=================")

data_bool = True;
print("data : ",data_bool,", Type = ",type(data_bool))

data_int=int(data_bool)
data_string=str(data_bool)
data_float=float(data_bool)
print("data : ",data_int,", Type = ",type(data_int))
print("data : ",data_string,", Type = ",type(data_string))
print("data : ",data_float,", Type = ",type(data_float))


print("============STRING=================")

data_string = "10";
print("data : ",data_string,", Type = ",type(data_string))

data_int=int(data_string) #string harus angka
data_bool=bool(data_string) #string harus angka
data_float=float(data_string) #nilai string bila terisi bernilai true dan bila tak terisi maka false
print("data : ",data_int,", Type = ",type(data_int))
print("data : ",data_bool,", Type = ",type(data_bool))
print("data : ",data_float,", Type = ",type(data_float))
