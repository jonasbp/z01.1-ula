import sys
from random import randrange

from ula import compute_ula


class UlaTerminal:
    ula_fields = ['x', 'y', 'zx', 'nx', 'zy', 'ny', 'f', 'no']

    def __init__(self):
        self.data = {}
        for k in UlaTerminal.ula_fields:
            self.data[k] = randrange(0, 2)
        self.data['x'] = randrange(0, 2**16)
        self.data['y'] = randrange(0, 2**16)

    def print_ula_vals(self):
        print('======-- ULA --======')
        for k in UlaTerminal.ula_fields:
            print('{}: {}'.format(k, self.data[k]))
        print('\n')
        result = compute_ula(**self.data)
        print('======-- Output --======')
        print('zr: {}  ng: {}  out (signed): {}'.format(result[0], result[1], result[2]))
        print('')

    def ask(self):
        campo = ''
        valor = None

        while campo not in UlaTerminal.ula_fields:
            campo = input('Digite nome do campo para alterar valor ou S para sair: ')
            if campo.strip() == 'S':
                sys.exit(0)

        while valor is None:
            try:
                valor = int(input('Digite um valor para o campo: '))
                if campo not in ['x', 'y'] and (valor < 0 or valor > 1):
                    valor = None
                    raise Exception
                elif campo in ['x', 'y'] and (valor > 2**15 or valor < 2**15):
                    raise Exception
            except:
                print('Valor inválido para o campo')

        self.data[campo] = valor

if __name__ == '__main__':
    ula = UlaTerminal()
    while True:
        ula.print_ula_vals()
        ula.ask()

