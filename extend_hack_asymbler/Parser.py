# created by Jeremy Jersin


import re


class Parser:

    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2
    EQU_INSTRUCTION = 3

    def __init__(self, asm_file):
        self.asm_file = asm_file
        self.lines_split = []
        self.get_lines()
        self.current_instruction = 'null'
        self.instruction_type = -1
        self.symbol = 'null'
        self.value = 'null'
        self.comp = 'null'
        self.destination = 'null'
        self.jump = 'null'
        self.value_error_file = self.asm_file[:self.asm_file.index('.')] + '_error.txt'

    # gets lines from the files
    def get_lines(self):
        f = open(self.asm_file, 'r')
        for line in f:
            self.lines_split.append(line)
        f.close()

    # removes comments
    @staticmethod
    def remove_comments(line):
        try:
            return line[:line.index('//')]
        except ValueError:
            return line

    # breaks apart the a instructions
    def a_instruction(self):
        self.instruction_type = self.A_INSTRUCTION
        no_white_space = re.sub(r'\s+', '', self.current_instruction)
        if no_white_space.startswith('@0b') or no_white_space.startswith('@0B'):
            if re.match(r'[^0-1]+', no_white_space[3:]) is None:
                self.symbol = str(int(no_white_space[no_white_space.index('@') + 1:], 0))

        elif no_white_space.startswith('@0x') or no_white_space.startswith('@0X'):
            if re.match(r'[a-fA-F\d]+', no_white_space[3:]) is None:
                self.symbol = str(int(no_white_space[1:], 0))

        else:
            self.symbol = no_white_space[1:]

    # breaks apart the c instructions
    def c_instruction(self):
        self.instruction_type = self.C_INSTRUCTION
        no_white_space = re.sub(r'\s+', '', self.current_instruction)
        if '=' in no_white_space:
            self.destination = no_white_space[:no_white_space.index('=')]
            self.comp = no_white_space[no_white_space.index('=')+1:]
        elif ';' in no_white_space:
            self.comp = no_white_space[:no_white_space.index(';')]
            self.jump = no_white_space[no_white_space.index(';')+1:]
        elif ';' and '=' in no_white_space:
            self.comp = no_white_space[no_white_space.index('=')+1:no_white_space(';')]
            self.destination = no_white_space[:no_white_space.index('=')]
            self.jump = no_white_space[no_white_space.index(';')+1]
        else:
            self.comp = no_white_space

    # gets labels from label instructions
    def l_instruction(self):
        self.instruction_type = self.L_INSTRUCTION
        self.symbol = self.current_instruction[self.current_instruction.index('(')+1:self.current_instruction.index(')')]

    # breaks apart the equ instructions
    def equ_instruction(self):
        self.instruction_type = self.EQU_INSTRUCTION
        symbol_value = self.current_instruction[5:]
        self.symbol = symbol_value[:symbol_value.index(' ')]
        self.value = symbol_value[symbol_value.index(' ')+1:]
        if self.value.startswith('0x') or self.value.startswith('0X') or self.value.startswith('0b') or self.value.startswith('0b'):
            try:
                self.value = str(int(self.value.lower(), 0))
            except ValueError:
                print(ValueError)

    # see if list is empty
    def has_more_instructions(self):
        # see if there are more instructions
        return self.lines_split != []

    # resets instruction information and decides what type the instruction is
    def advance(self):
        # reset instruction information
        self.current_instruction = 'null'
        self.instruction_type = -1
        self.symbol = 'null'
        self.value = 'null'
        self.comp = 'null'
        self.destination = 'null'
        self.jump = 'null'

        # get next instruction
        self.current_instruction = self.lines_split.pop(0)
        self.current_instruction = self.remove_comments(self.current_instruction)
        self.current_instruction = self.current_instruction.strip()

        # figure instruction type
        if self.current_instruction.startswith('@'):
            self.a_instruction()
        elif self.current_instruction.startswith('.'):
            self.equ_instruction()
        elif self.current_instruction.startswith('('):
            self.l_instruction()
        elif self.current_instruction == '' or self.current_instruction == '\n':
            pass
        else:
            self.c_instruction()

