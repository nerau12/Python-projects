# created by Jeremy Jersin

class Code:

    def __init__(self):
        self.jump_codes = {
            'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100',
            'JNE': '101', 'JLE': '110', 'JMP': '111'
        }

        self.destination_codes = {
            'null': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100',
            'AM': '101', 'AD': '110', 'AMD': '111'
        }

        self.comp_codes = {
            '0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100', 'A': '0110000',
            '!D': '0001101', '!A': '0110001', '-D': '0001111', '-A': '0110011', 'D+1': '0011111',
            'A+1': '0110111', 'D-1': '0001110', 'A-1': '0110010', 'D+A': '0000010', 'D-A': '0010011',
            'A-D': '0000111', 'D&A': '0000000', 'D|A': '0010101',  'M': '1110000', '!M': '1110001',
            '-M': '1110011', 'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010','D-M': '1010011',
            'M-D': '1000111', 'D&M': '1000000', 'D|M': '1010101', '!(!D&!A)': '0010101', '!D|!A': '0000001',
            '!D&A': '0010000', 'D&!A': '0000100', '!D&!A': '0010100', '!(D&A)': '0000001', '!(D&!A)': '0010001',
            '!(!D&A)': '0000101', 'D|!A': '0000101', '!D|A': '0010001', '!(D|A)': '0010100', '!(D|!A)': '0010000',
            '!(!D|A)': '0000100', '!(!D|!A)': '0000000', 'D&!M': '1000100', '!D&M': '1010000', '!D&!M': '1010100',
            '!(D&M)': '1000001', '!(!D|!M)': '1000000', '!(D&!M)': '1001001', '!(!D&M)': '1010001',
            '!(!D&!M)': '1010101', 'D|!M': '1010001', '!D|M': '1010001', '!D|!M': '1000001', '!(D|M)': '1010100',
            '!(D|!M)': '1010000', '!(!D|M)': '1000100'
        }

    # converts numbers to bits
    @staticmethod
    def to_bits(number):
        return bin(int(number))[2:]

    # converts Xnn instructions to hex strings
    @staticmethod
    def change_special_comp(comp):
        return str(bin(int(comp.lower().strip('x'), 16)))[2:].zfill(7)

    # creates a type instruction
    def create_a_type_instruction(self, address):
        return '0' + self.to_bits(address).zfill(15)

    # creates c type instructions
    def create_c_type_instruction(self, comp, destination, jump):
        if comp.startswith('X') or comp.startswith('x'):
            return '111' + self.change_special_comp(comp) + self.destination(destination) + self.jump(jump)
        else:
            return '111' + self.comp(comp) + self.destination(destination) + self.jump(jump)

    # get jump code
    def jump(self, jump):
        return self.jump_codes[jump]

    # get destination code
    def destination(self, destination):
        return self.destination_codes[destination]

    # get comp code
    def comp(self,comp):
        return self.comp_codes[comp]

