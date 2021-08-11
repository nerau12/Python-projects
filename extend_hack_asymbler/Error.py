# created by Jeremy Jersin


from Parser import Parser
from Code import Code
import re


class Error:

    def __init__(self, asm_file):
        self.asm_file = asm_file
        self.errors = []
        self.symbol_table = {}
        self.current_address = 16

    # see if not errors for empty list
    def has_no_errors(self):
        return self.errors == []

    # checks for negative values and binary numbers
    def illegal_a_instruction(self, parser, line):
        no_white_space = re.sub(r'\s+', '', parser.current_instruction)
        if '-' in no_white_space and parser.instruction_type == parser.A_INSTRUCTION:
            self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction + ' '
                               + parser.symbol + " Value is not allowed\n")

        elif no_white_space.startswith('@0b') or no_white_space.startswith('@0B'):
            if re.match(r'[^0-1]+', no_white_space[3:]) is not None:
                self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction + ' '
                                   + no_white_space[1:] + " Invalid binary number\n")

    # checks for legal comp codes
    def illegal_comp(self, code, parser, line):
        if parser.comp not in code.comp_codes and parser.comp is not 'null' and not parser.comp.startswith('X') \
                and not parser.current_instruction.startswith('/'):
            self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction +
                               ' ' + parser.comp + ' is not in mnemonics\n')

    # checks for legal jumps
    def illegal_jump(self, code, parser, line):
        if parser.jump not in code.jump_codes and parser.jump is not 'null' \
                and not parser.current_instruction.startswith('/'):
            self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction +
                               ' ' + parser.jump + " is not in mnemonics\n")

    # checks for legal destinations
    def illegal_destination(self, code, parser, line):
        if parser.destination not in code.destination_codes and parser.destination is not 'null' \
                and not parser.current_instruction.startswith('/'):
            self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction +
                               ' ' + parser.destination + " is not in mnemonics\n")

    # checks for legal c instructions
    def illegal_c_instruction(self, parser, line):
        code = Code()
        self.illegal_comp(code, parser, line)
        self.illegal_jump(code, parser, line)
        self.illegal_destination(code, parser, line)

    # checks for illegal lables and see if in use already
    def illegal_label(self, parser, line):
        if parser.instruction_type == parser.L_INSTRUCTION and parser.symbol not in self.symbol_table:
            self.symbol_table[parser.symbol] = self.current_address

        elif parser.instruction_type == parser.L_INSTRUCTION and parser.symbol in self.symbol_table:
            self.errors.append('test\n')

        elif ' ' in parser.current_instruction and parser.instruction_type == parser.L_INSTRUCTION:
            self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction +
                               ' is not valid label\n')

    # checks for illegal equs
    def illegal_equ(self, parser, line):
        if parser.instruction_type == parser.EQU_INSTRUCTION and parser.symbol in self.symbol_table:
            self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction +
                               ' ' + parser.symbol + " has already been declared\n")

        elif parser.instruction_type == parser.EQU_INSTRUCTION and parser.symbol not in self.symbol_table:
            self.symbol_table[parser.symbol] = parser.value

    # checks for illegal comments
    def illegal_comment(self, parser, line):
        if '/' in parser.current_instruction:
            if parser.current_instruction.startswith('@'):
                self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction +
                                   ' is not valid A instruction\n')
            elif parser.current_instruction.startswith('.'):
                self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction +
                                   ' is not valid EQU statement\n')
            else:
                self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction +
                                   ' is not valid comment\n')

    # checks for values are legal for regular numbers for equ and a type
    def illegal_value(self, parser, line):
        if parser.instruction_type == parser.A_INSTRUCTION:
            if parser.symbol.isdigit():
                if 0 < int(parser.symbol) > 32768:
                    self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction +
                                       ' ' + parser.symbol + " Value is not allowed\n")

        elif parser.instruction_type == parser.EQU_INSTRUCTION:
            if parser.value is not 'null' and '/' not in parser.current_instruction:
                if 0 < int(parser.value, 0) > 32768:
                    self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction +
                                       ' ' + parser.value + " Value is not allowed\n")

    # handles hex numbers conversion and see if hex number is legal
    def illegal_hex_number(self, parser, line):
        no_white_space = re.sub(r'\s+', '', parser.current_instruction)
        if no_white_space.startswith('@0x') or no_white_space.startswith('@0X'):
            if re.search(r'[^a-fA-F\d]+', no_white_space[3:]) is not None:
                self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction + ' '
                                   + no_white_space[1:] + " Invalid hex number\n")
            else:
                if 0 < int(no_white_space[1:], 0) > 32768:
                    self.errors.append('on line number: ' + str(line) + ' Instruction: ' + parser.current_instruction +
                                       ' ' + no_white_space[1:] + " Value is not allowed\n")

    def print_out_errors(self):
        with open('./hack/' + self.asm_file + "-error.txt", 'w') as error_file:
            error_file.writelines(self.errors)

    def check_for_errors(self):
        parser = Parser(self.asm_file)
        line = 1
        while parser.has_more_instructions():
            parser.advance()
            if parser.current_instruction == '':
                continue
            else:
                self.illegal_a_instruction(parser, line)
                self.illegal_c_instruction(parser, line)
                self.illegal_label(parser, line)
                self.illegal_equ(parser, line)
                self.illegal_comment(parser, line)
                self.illegal_value(parser, line)
                self.illegal_hex_number(parser, line)
                line += 1

        if not self.has_no_errors():
            self.print_out_errors()

        return self.has_no_errors()
