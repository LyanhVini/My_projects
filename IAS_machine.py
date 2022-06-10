'''
- MÁQUINA IAS --> PC, IR, MBR, MAR, MQ, AC, IBR
'''

import math
import numpy as np

PC = [0, 1, 2, 3]
MAR = 0
MBR = 0
AC = 0
MQ = 0
IBR = 0
IR = 0
i = 0

#Criando a memória:
memória = {
            0: {'LOAD MQ, M(x)': hex(9)[2:]},
            1: {'LOAD MQ': hex(10)[2:]},
            2: {'MUL M(X)': hex(11)[2:]},
            3: {'STOR M(X)': hex(33)[2:]},
            4: {'LOAD -M(X)': hex(2)[2:]},
            5: {'LOAD |M(X)|': hex(3)[2:]},
            6: {'LOAD -|M(X)|': hex(4)[2:]},
            7: {'JUMP M(X,0:19)': hex(13)[2:]},
            8: {'JUMP M(X,20:39)': hex(14)[2:]},
            9: {'JUMP + M(X,0:19)': hex(15)[2:]},
            10: {'JUMP + M(X,20:39)': hex(16)[2:]},
            11: {'ADD M(X)': hex(5)[2:]},
            12: {'ADD |M(X)|': hex(7)[2:]},
            13: {'SUB M(X)': hex(6)[2:]},
            14: {'SUB |M(X)|': hex(8)[2:]},
            15: {'LOAD M(X)': hex(1)[2:]},
            16: {'DIV M(X)': hex(12)[2:]},
            17: {'LSH': hex(40)[2:]},
            18: {'RSH': hex(21)[2:]},
            19: {'STOR M(X,8:19)': hex(18)[2:]},
            20: {'STOR M(X,28:39)': hex(19)[2:]},
            21: {'v1': [1, 2, 3]},
            22: {'v2': [5, 6, 7]},
            23: {'prodinterno': []}
}

for numero in PC:
    if PC == 0:

        # Acessa a memória em -> memória[0]['LOAD MQ, M(x)']
        MAR = PC + list(memória[21].values())
        MBR = list(memória[21])
        IR = list(memória[21].keys())
        MQ = list(memória[21].values())
        # Exibindo os valores:
        print(PC)
        print(MAR)
        print(MBR)
        print(IR)
        print(MQ)

    elif PC == 1:

        # Acessa a memória em -> memória[1]['LOAD MQ']
        MAR = PC + list(memória[1].values())
        MBR = list(memória[1])
        IR = list(memória[1].keys())
        AC = [AC == MQ for item in AC]

        # Exibindo os valores:

        print(PC)
        print(MAR)
        print(MBR)
        print(IR)
        print(AC)

    elif PC == 2:

        # Acessa a memória em -> memória[2]['MUL M(X)']
        MAR = PC + list(memória[2].values())
        MBR = list(memória[2])
        IR = list(memória[2].keys())

        # Fazendo a operação do produto interno

        valor1 = list(memória[21].values())
        valor2 = list(memória[22].values())

        r = (np.cross(valor1, valor2))

        AC = r

        # Exibindo os valores

        print(PC)
        print(MAR)
        print(MBR)
        print(IR)
        print(AC)
        print(r) #Valor do produto interno

    elif PC == 3:

        # Acessando a memória em -> memória[3]['STOR M(X)']
        MAR = PC + list(memória[3].values())
        MBR = list(memória[3])
        IR = list(memória[3].keys())

        memória['prodinterno'] = AC

        # Exibindo os valores

        print(PC)
        print(MAR)
        print(MBR)
        print(IR)
        print(memória['prodinterno'])

    elif PC == 4:

        # Acessando a memória em -> memória [4]['LOAD -M(X)']
        MAR = PC + list(memória[4].values())
        MBR = list(memória[4])
        IR = list(memória[4].keys())
        AC = -(memória[i].values())

    elif PC == 5:

        # Acessando a memória em -> memória [5]['LOAD |M(X)|']
        MAR = PC + list(memória[5].values())
        MBR = list(memória[5])
        IR = list(memória[5].keys())
        AC = abs(memória[i].values())

    elif PC == 6:

        # Acessando a memória em memória [6]['LOAD -|M(X)|']
        MAR = PC + list(memória[6].values())
        MBR = list(memória[6])
        IR = list(memória[6].keys())
        AC = -abs(memória[i].values())

    # elif PC == 7:

    # Acessando a memória em memória [7]['JUMP M(X,0:19)']

    # elif PC == 8:
    #
    # Acessando a memória em memória [8]['JUMP M(X,20:39)']
    # ???

    # elif PC == 9:

    # Acessando a memória em memória [9] ['JUMP + M(X,0:19)']
    # ???

    # elif PC == 10:
    #
    # memória [10] ['JUMP + M(X,20:39)']
    # ????

    elif PC == 11:

        # Acessando a memória em memória [11] ['ADD M(X)']
        MAR = PC + list(memória[11].values())
        MBR = list(memória[11])
        IR = list(memória[11].keys())
        AC = AC + (memória[i].values())

    elif PC == 12:

        # Acessando a memória em memória[12]['ADD |M(X)|']
        MAR = PC + list(memória[11].values())
        MBR = list(memória[11])
        IR = list(memória[11].keys())
        AC = AC + abs(memória[i].values())

    elif PC == 13:

        # Acessando a memória em memória [13] ['SUB M(X)']
        MAR = PC + list(memória[13].values())
        MBR = list(memória[13])
        IR = list(memória[13].keys())
        AC = AC - (memória[i].values())

    elif PC == 14:

        # Acessando a memória em memória [14] ['SUB |M(X)|']
        MAR = PC + list(memória[14].values())
        MBR = list(memória[14])
        IR = list(memória[14].keys())
        AC = AC - abs(memória[i].values())

    elif PC == 15:

        # Acessando a memória em memória [15] ['LOAD M(X)']
        MAR = PC + list(memória[14].values())
        MBR = list(memória[14])
        IR = list(memória[14].keys())
        AC = memória[i].values()

    elif PC == 16:

        # Acessando a memória em memória [16] ['DIV M(X)']
        MAR = PC + list(memória[16].values())
        MBR = list(memória[16])
        IR = list(memória[16].keys())
        AC = AC / int(memória[i].values())

    elif PC == 17:

        # Acessando a memória em memória [17] ['LSH']
        MAR = PC + list(memória[17].values())
        MBR = list(memória[17])
        IR = list(memória[17].keys())
        AC = 2 * AC

    elif PC == 18:

        # Acessando a memória em memória [18] ['RSH']
        MAR = PC + list(memória[18].values())
        MBR = list(memória[18])
        IR = list(memória[18].keys())
        AC = AC / 2

    # elif PC == 19:

    # Acessando a memória em memória [19] ['STOR M(X,8:19)']
    # ???

    # elif PC == 20:

    # Acessando a memória em -> memória [20] ['STOR M(X,28:39)']
    # ???

