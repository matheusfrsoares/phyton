alunos = ('Matheus', 'Lucas', 'Ruan', 'Mellyssa')
print (alunos [2])

#uso de if / while
#uso de for

"""
for x in alunos:
    print(x) 
"""
#atividade - listar todos os itens da lista de frutas abaixo, exceto a uva
frutas = ('Banana', 'Maçã', 'Uva', 'Pera', 'Uva', 'Amora')

"""
for f in frutas:
    if f != 'uva':
        print(f)
"""
for f in frutas:
    if f == 'Uva':
        #continue # apenas mantém o loop - transmitindo a informação
        break # interrompe o loop na hora que ele encontra o 'Uva'
    else:
        print(f)