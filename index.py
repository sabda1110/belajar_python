# Latihan Suhu 


#Fahrenheit
print("============Fahrenheit=============")

fahrenheit = float(input("Masukan Suhu dalam Fahrenheit : "))

#Fahrenheit ke Celcius
celcius = (5/9)*(fahrenheit-32)
#Fahrenheit ke reamur
reamur = (4/9)*(fahrenheit-32)
#Fahrenheit ke Kelvin
kelvin = ((5/9)*(fahrenheit-32))+273

print("Suhu Dalam Celcius : ",celcius," Celcius")
print("Suhu Dalam reamur : ",reamur," Reamur")
print("Suhu Dalam Kelvin : ",kelvin," kelvin")


#Kelvin
print("============Kelvin=============")

kelvin = float(input("Masukan Suhu dalam Kelvin : "))

#Kelvin ke Celcius
celcius = kelvin-273
#Kelvin ke reamur
reamur = (4/5)*(kelvin-273)
#Kelvin ke fahrenheit
fahrenheit = ((9/5)*(kelvin-273))+32

print("Suhu Dalam Celcius : ",celcius," Celcius")
print("Suhu Dalam reamur : ",reamur," Reamur")
print("Suhu Dalam Fahrenheit : ",fahrenheit," Fahrenheit")

