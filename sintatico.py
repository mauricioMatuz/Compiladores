import ply.yacc as yacc
import os
import codecs
import re
from lexico import tokens
from sys import stdin

resultado_gramatica = []
VERBOSE = 1



def p_declaration(p):
    """declaration : HASH INCLUDE LESS STD ID POINT ID GREATER"""
    print("p_declaration")


def p_var_declaration_1(p):
    """var_declaration : type_specifier ID SEMICOLON
    | type_specifier ID COMMA ID SEMICOLON
    | type_specifier ID EQUAL NUMBER SEMICOLON
    | type_specifier ID EQUAL var SEMICOLON
    """
    print("p_var_declaration_1")


def p_var_declaration_2(p):
    """var_declaration : type_specifier ID LBRACKET NUMBER RBRACKET SEMICOLON"""
    print("p_var_declaration_2")


def p_type_specifier_1(p):
    """type_specifier : INT"""
    print("p_type_specifier_1")


def p_type_specifier_2(p):
    """type_specifier : VOID"""
    print("p_type_specifier_2")


def p_type_specifier_(p):
    """type_specifier : STRING"""
    print("p_type_specifier_")

def p_type_specifier_(p):
    """type_specifier : CHAR"""
    print("p_type_specifier_")


def p_fun_declaration(p):
    """fun_declaration : type_specifier ID LPAREN  RPAREN LBLOCK RBLOCK"""
    print("p_fun_declaration")


def p_params_1(p):
    "params : param_list"
    print("p_params_1")


def p_params_2(p):
    "params : VOID"
    print("")


def p_param_list_1(p):
    "param_list : param_list COMMA param"
    print("p_params_2")


def p_param_list_2(p):
    "param_list : param"
    print("p_param_list_2")


def p_param_list_3(p):
    "param_list : empty"
    print("p_param_list_3")


def p_param_1(p):
    "param : type_specifier ID"
    print("p_param_1")


def p_param_2(p):
    "param : type_specifier ID LBRACKET RBRACKET"
    print("p_param_2")


def p_compount_stmt(p):
    "compount_stmt : LBLOCK local_declarations statement_list RBLOCK"
    print("p_compount_stmt")


def p_local_declarations_1(p):
    "local_declarations : local_declarations var_declaration"
    print("p_local_declarations_1")


def p_local_declarations_2(p):
    "local_declarations : empty"
    print("p_local_declarations_2")


def p_statement_list_1(p):
    "statement_list : statement_list statement"
    print("p_statement_list_1")


def p_statement_list_2(p):
    "statement_list : empty"
    print("p_statement_list_2")


def p_statement(p):
    """statement : expression_stmt
    | compount_stmt
    | selection_stmt
    | iteration_stmt
    | return_stmt
    """
    print("p_statement")


def p_expression_stmt_1(p):
    """expression_stmt : expression SEMICOLON"""
    print("p_expression_stmt_1")


def p_expression_stmt_2(p):
    "expression_stmt : SEMICOLON"
    print("p_expression_stmt_2")


def p_expression_stmt_3(p):
    """expression_stmt : PRINTF LGREATER QUOTES ID QUOTES SEMICOLON
    | PRINTF LGREATER QUOTES ID QUOTES LGREATER ENDL SEMICOLON
    | PRINTF LGREATER STRING  SEMICOLON
    | PRINTF LGREATER STRING  LGREATER ENDL SEMICOLON
    | PRINTF LGREATER var SEMICOLON
    | PRINTF LGREATER var LGREATER   ENDL SEMICOLON
    | PRINTF LGREATER var  LGREATER var SEMICOLON
    | PRINTF LGREATER var LGREATER  var LGREATER ENDL SEMICOLON
    """
    print("p_expression_stmt_3")


def p_expression_stmt_4(p):
    """expression_stmt : CIN RGREATER var SEMICOLON
    | CIN RGREATER var  RGREATER var SEMICOLON
    | CIN POINT GET LPAREN RPAREN SEMICOLON
    """
    print("p_expression_stmt_4")


def p_expression_stmt_5(p):
    """expression_stmt : ID PLUSPLUS
    | PLUSPLUS ID
    | ID MINUSMINUS
    | MINUSMINUS ID
    """
    print("p_expression_stmt_5")


def p_selection_stmt_1(p):
    "selection_stmt : IF LPAREN expression RPAREN statement"
    print("p_selection_stmt_1")


def p_selection_stmt_2(p):
    "selection_stmt : IF LPAREN expression RPAREN statement ELSE statement"
    print("p_selection_stmt_2")


def p_iteration_stmt(p):
    "iteration_stmt : WHILE LPAREN expression RPAREN statement"
    print("p_iteration_stmt")


def p_iteration_stmt1(p):
    """iteration_stmt :
    | FOR LPAREN var SEMICOLON expression SEMICOLON expression RPAREN statement
    | FOR LPAREN var SEMICOLON expression SEMICOLON var PLUSPLUS RPAREN statement
    | FOR LPAREN var SEMICOLON expression SEMICOLON PLUSPLUS var  RPAREN statement
    | FOR LPAREN var SEMICOLON expression SEMICOLON var MINUSMINUS RPAREN statement
    | FOR LPAREN var SEMICOLON expression SEMICOLON MINUSMINUS var  RPAREN statement
    """
    print("p_iteration_stmt1")


def p_return_stmt_1(p):
    "return_stmt : RETURN SEMICOLON"
    print("p_return_stmt_1")


def p_return_stmt_2(p):
    "return_stmt : RETURN expression SEMICOLON"
    print("p_return_stmt_2")


def p_expression_1(p):
    """expression : var EQUAL expression"""
    print("")


def p_expression_2(p):
    "expression : simple_expression"
    print("")


def sintax(t):
    os.system("g++ -Wall " + t)
    print("")


def p_var_1(p):
    "var : ID"
    print("")


def p_var_2(p):
    "var : ID LBRACKET expression RBRACKET"
    print("")


def p_simple_expression_1(p):
    "simple_expression : additive_expression relop additive_expression"
    print("")


def p_simple_expression_2(p):
    "simple_expression : additive_expression"
    print("")


def p_relop(p):
    """relop : LESS
    | LESSEQUAL
    | GREATER
    | GREATEREQUAL
    | DEQUAL
    | DISTINT
    | QUOTES
    """
    print("")


def p_additive_expression_1(p):
    "additive_expression : additive_expression addop term"
    print("")


def p_additive_expression_2(p):
    "additive_expression : term"
    print("")


def p_addop(p):
    """addop : PLUS
    | MINUS
    """
    print("")


def p_term_1(p):
    "term : term mulop factor"
    print("")


def p_term_2(p):
    "term : factor"
    print("")


def p_mulop(p):
    """mulop : 	TIMES
    | DIVIDE
    """
    print("")


def p_factor_1(p):
    "factor : LPAREN expression RPAREN"
    print("")


def p_factor_2(p):
    "factor : var"
    print("")


def p_factor_3(p):
    "factor : call"
    print("")


def p_factor_4(p):
    "factor : NUMBER"
    print("")


def p_call(p):
    "call : ID LPAREN args RPAREN"
    print("")


def p_args(p):
    """args : args_list
    | empty
    """
    print("")


def p_args_list_1(p):
    "args_list : args_list COMMA expression"
    print("")


def p_args_list_2(p):
    "args_list : expression"
    print("")


def p_empty(p):
    "empty :"
    print("")


# def p_error(p):
#       	print ("Error de sintaxis ", p)
def p_error(p):
    global resultado_gramatica
    if p:
        resultado = "Error sintactico de tipo {} en el valor {}".format(
            str(p.type), str(p.value)
        )
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(p)
        print(resultado)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sistactico


parser = yacc.yacc()


def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica


if __name__ == "__main__":
    while True:
        try:
            s = input(" ingresa dato >>> ")
        except EOFError:
            continue
        if not s:
            continue

        # gram = parser.parse(s)
        # print("Resultado ", gram)

        prueba_sintactica(s)
