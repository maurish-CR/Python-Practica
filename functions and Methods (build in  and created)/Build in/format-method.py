texto = "{} es un {} {}"
print(texto.format("Mau", "mal", "estudiante"))

#positional
texto = "{0} es un {2} {1}"
print(texto.format("Mau", "mal", "estudiante"))

#Arguments
texto = "{name} es un {adjective} {noun}"
print(texto.format(name = "Mau", adjective = "mal", noun = "estudiante"))
 