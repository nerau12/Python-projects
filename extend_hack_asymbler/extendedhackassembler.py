# created by Jeremy Jersin


import sys
from Code import Code
from Parser import Parser
from SymbolTable import SymbolTable
from Error import Error


class ExtendedHackAssembler:

    line_added = 0

    def __init__(self, ext_asm_file):
        self.ext_asm_file = ext_asm_file
        self.ext_hack_file = self.create_hack_file()
        self.symbol_address = 16
        self.symbol_table = SymbolTable()

    # create hack file based on asm file
    def create_hack_file(self):
        if self.ext_asm_file.endswith('.asm'):
            return './hack/' + self.ext_asm_file.replace('.asm', '.hack')

        elif self.ext_asm_file.endswith('.xasm'):
            return './hack/' + self.ext_asm_file.replace('.xasm', '.hack')

        else:
            return './hack/' + self.ext_asm_file + '.hack'

    # get address of symbol based if it exists in table and add to export symbol table for ram
    def get_address(self, symbol, parser):

        if symbol.isdigit():
            return symbol

        else:
            if not self.symbol_table.contains(symbol):
                self.symbol_table.add_entry(symbol, self.symbol_address)
                self.symbol_address += 1
                self.symbol_table.symbol_table_export[symbol] = [self.symbol_address, self.line_added, parser.A_INSTRUCTION]
            return self.symbol_table.get_address(symbol)

    # looks through the file for labels and .equ instructions and adds them to symbol table
    def first_pass(self):
        parser = Parser(self.ext_asm_file)
        current_address = 0
        while parser.has_more_instructions():
            parser.advance()
            instruction_type = parser.instruction_type
            self.line_added += 1
            if instruction_type == parser.A_INSTRUCTION or instruction_type == parser.C_INSTRUCTION:
                current_address += 1
            elif instruction_type == parser.L_INSTRUCTION:
                self.symbol_table.add_entry(parser.symbol, current_address)
                self.symbol_table.symbol_table_export[parser.symbol] = [current_address, self.line_added, parser.L_INSTRUCTION]
            elif instruction_type == parser.EQU_INSTRUCTION:
                self.symbol_table.add_entry(parser.symbol, parser.value)
                self.symbol_table.symbol_table_export[parser.symbol] = [parser.value, self.line_added, parser.EQU_INSTRUCTION]

    # takes each instruction piece given and builds the instructions to be added to hack code
    def second_pass(self):
        self.line_added = 0
        parser = Parser(self.ext_asm_file)
        hack_file = open(self.ext_hack_file, 'w')
        code = Code()
        while parser.has_more_instructions():
            parser.advance()
            self.line_added += 1
            instruction_type = parser.instruction_type
            if instruction_type == parser.A_INSTRUCTION:
                hack_file.write(code.create_a_type_instruction(self.get_address(parser.symbol, parser)) + '\n')
            elif instruction_type == parser.C_INSTRUCTION:
                hack_file.write(code.create_c_type_instruction(parser.comp, parser.destination, parser.jump) + '\n')
        hack_file.close()

    # calls all methods to assemble anc checks for errors
    def assemble(self):
        self.first_pass()
        no_errors = Error(self.ext_asm_file).check_for_errors()
        if no_errors:
            self.second_pass()
            self.symbol_table.export_symbol_table(self.ext_asm_file)

        else:
            print(self.ext_asm_file + " has errors check error.txt")


# driver code for command line
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage python extendedhackassembler.py program.asm or program.xasm")

    else:
        asm_file = sys.argv[1]

extend_hack_assembler = ExtendedHackAssembler(asm_file)
extend_hack_assembler.assemble()
