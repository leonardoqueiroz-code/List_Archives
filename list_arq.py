import os
pasta = 'D:/'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        print(os.path.join(os.path.realpath(diretorio), arquivo))