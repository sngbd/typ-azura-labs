def kalkulator(inp):
    op1, opr, op2 = inp.split()
    op1 = int(op1)
    op2 = int(op2)
    if opr == '+':
        return op1 + op2
    elif opr == '-':
        return op1 - op2
    elif opr == '*':
        return op1 * op2
    elif opr == '/':
        if op1 % op2 == 0:
            return op1 // op2
        else:
            return op1 / op2
