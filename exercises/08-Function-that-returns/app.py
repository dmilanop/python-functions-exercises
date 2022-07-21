def dollar_to_euro(dollar_value):
	return dollar_value * 0.89

def euro_to_yen(euro_value):
	return euro_value * 124.15

####### ↓ YOUR CODE BELOW ↓ #######
transformar_dollar_to_euro = dollar_to_euro(137)
transformar_euro_to_yen = euro_to_yen(transformar_dollar_to_euro)

print(transformar_euro_to_yen)