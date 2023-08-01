def lenguaje_del_hacker(palabra):
    abecedario = {
    'a' : '4', 
    'b' : 'I3', 
    'c' : '[', 
    'd' : ')', 
    'e' : '3', 
    'f' : '|=', 
    'g' : '&', 
    'h' : '#', 
    'i' : '1', 
    'j' : ',_|', 
    'k' : '>|', 
    'l' : '1', 
    'm' : '/\/\\', 
    'n' : '^/', 
    'o' : '0', 
    'p' : '|*', 
    'q' : '(_,)', 
    'r' : 'I2', 
    's' : '5', 
    't' : '7', 
    'u' : '(_)', 
    'v' : '\/', 
    'w' : '\/\/', 
    'x' : '><', 
    'y' : 'j', 
    'z' : '2',
    '1' : 'L',
    '2' : 'R',
    '3' : 'E',
    '4' : 'A',
    '5' : 'S',
    '6' : 'b',
    '7' : 'T',
    '8' : 'B', 
    '9' : 'g',
    '0' : 'o'
    }
    texto_nuevo=""
    for char in palabra:
        if char.lower() in abecedario.keys():
            texto_nuevo+=abecedario[char.lower()]
        else:
            print(f"el caracter no existe en el diccionario")
    print(f"la nueva palabra es: {texto_nuevo}")

lenguaje_del_hacker("hola")