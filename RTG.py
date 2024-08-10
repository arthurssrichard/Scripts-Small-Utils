import random
import pandas


enable_feel = bool(input('Habilitar tríades menores?(T/F)'))
enable_size = bool(input('Habilitar tríades aumentadas e diminutas?(T/F)'))
enable_model = bool(input('Habilitar modelos?(T/F)'))
enable_enc = bool(input('Habilitar encadeamentos diferentes?(T/F)'))

roots = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
feels = ['m',""]
sizes = ['Aug', 'Dim',""]
models = ['C', 'A', 'E']
encs = ['1º','2º','3º','4º']

def random_triad():
    

    root = random.choice(roots)

    if enable_size == True:
        size = random.choice(sizes)
    else:
        size = ""

    if enable_feel == True:
        feel = random.choice(feels)
    else:
        feel = ""

    if enable_model == True:
        model = random.choice(models)
    else:
        model = ""

    if enable_enc == True:
        enc = random.choice(encs)
    else:
        enc = ""


    chord = root + feel + " " + size + " " + ('Modelo de '+ model) + (f', {enc} encadeamento')
    print(chord)

while True:
    input('\nPressione Enter para gerar tríade')
    random_triad()
    
    

