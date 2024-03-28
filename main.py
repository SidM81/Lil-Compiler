from lex import *
from emit import *
from parse import *
import sys

def main():
    print("Lil' Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    lexer = Lexer(source)
    emitter = Emitter(f"{sys.argv[1][:-6]}.c")
    parser = Parser(lexer, emitter)

    parser.program() 
    emitter.writeFile() 
    print("Homie Compiled your code")

main()