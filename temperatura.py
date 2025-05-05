def temp():
    temp_celsius = float(input("Digite a tempetarura em celsius:  "))
    calc = (temp_celsius*1.8)+32
    return calc

temp_fah = temp()
print (f"A temperatura em Fahrenheit é {temp_fah}")

   #Convertendo de Fahrenheit para Celsius    
def temp():
    temp_fah = float(input("Digite a tempetarura em Fahrenheit:  "))
    temp_celsius = (temp_fah - 32) /1.8
    return temp_celsius

resultado = temp()
print (f"A temperatura em Celsius é {resultado:.2f} ")
