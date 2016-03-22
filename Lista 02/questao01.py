def converteParaCelsius(fahrenheit):
	return (float(fahrenheit) - 32)/1.8


def converteParaFahrenheit(celsius):
	return (float(celsius) * 1.8) + 32

celsius = converteParaCelsius(input("Digite uma temperatura em Fahrenheit \n"))
fahrenheit = converteParaFahrenheit(input("Digite uma temperatura em Celsius \n"))


print("Celsius Para Fahrenheit " + str(fahrenheit))
print("Fahrenheit Para Celsius " + str(celsius))
