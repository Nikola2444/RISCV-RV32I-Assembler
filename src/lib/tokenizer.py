#
# @author:Don Dennis
# tokenizer.py
#
# A simple assembler for RISCV RV32I supporting a definable subset of
# instructions.
#
# The assembler is build around `ply` and you can refer to
# http://www.dabeaz.com/ply/ply.html
# for its documentation.
import ply.lex as lex


# List of token names. This is always required
tokens = (
    'OPCODE',
    'REGISTER',
    'COMMA',
    'IMMEDIATE',
    'NEWLINE'
)

'''
Regex patters for token names are specified as t_TOKENNAME
in ply.Tthe TOKENNAME should match one of the specified tokesn.
'''
t_OPCODE = r'[a-z]+'
t_COMMA = r','
# For immediates, we currently only support decimal base
# which is converted to its equivalent two's complement method.
t_IMMEDIATE = r'[+-]?[0-9]+'
'''
Simar to the definition of token regex, rules associated with
tokens are specified as t_TOKENNAME(t). The tokens returned by
lexer.token() are instances of LexToken. This object has attributes
tok.type, tok.value, tok.lineno, and tok.lexpos.
'''


def t_REGISTER(t):
    r'\$[0-9][0-9]?'
    return t


# Define a rule so we can track line numbers
# This is a special rule in pyl
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


# A string containing ignored characters (spaces and tabs)
# Special rule
t_ignore = ' \t\r'

# Error handling rule


def t_COMMENT(t):
    r'\#.*'
    pass


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

if __name__ == '__main__':
    lex.runmain()

'''
REGARDING REQUIRED SPACE
Think of what will happen if the opcode portion is not followed
by a space before the register is specified. Let the opcode be
`add`. Lex now matches addr instead of arr, taking the r to be
a part of the opcode causing an error.
'''
