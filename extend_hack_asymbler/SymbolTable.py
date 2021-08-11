# created by Jeremy Jersin


class SymbolTable:

    def __init__(self):
        self.symbol_table = {
            'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4,
            'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5,
            'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11,
            'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15, 'SCREEN': 16384, 'KBD': 24576
        }

        self.symbol_table_export = {}

    # add to symbol table
    def add_entry(self, symbol, address):
        self.symbol_table[symbol] = address

    # get address of symbol in table
    def get_address(self, symbol):
        return self.symbol_table[symbol]

    # see if symbol in symbol table
    def contains(self, symbol):
        return symbol in self.symbol_table

    # export the lists into files
    def export_symbol_table(self, hack_file):
        with open('./hack/' + hack_file[:hack_file.index('.')] + '_ram_table.txt', 'w') as ram_file:
            for key in self.symbol_table_export:
                if self.symbol_table_export[key][2] == 0:
                    ram_file.write('Symbol: ' + key + ' Value:   ' + str(self.symbol_table_export[key][0]) + ' Line added: ' + str(self.symbol_table_export[key][1]) + '\n')
        with open('./hack/' + hack_file[:hack_file.index('.')] + '_rom_table.txt', 'w') as rom_file:
            for key in self.symbol_table_export:
                if self.symbol_table_export[key][2] == 2:
                    rom_file.write('Label Name:  ' + key + ' Value:  ' + str(self.symbol_table_export[key][0]) + ' Line added: ' + str(self.symbol_table_export[key][1]) + '\n')
        with open('./hack/' + hack_file[:hack_file.index('.')] + '_equ_table.txt', 'w') as equ_file:
            for key in self.symbol_table_export:
                if self.symbol_table_export[key][2] == 3:
                    equ_file.write('Symbol: ' + key + ' Value: ' + str(self.symbol_table_export[key][0]) + ' Line added: ' + str(self.symbol_table_export[key][1]) + '\n')



