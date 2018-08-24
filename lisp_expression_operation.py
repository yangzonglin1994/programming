"""
(* (+ 2 3) (^ 4))
"""


def calcu(lisp_expression):
    nums_stack = list()
    ops_stack = list()
    for char in lisp_expression:
        if char == '(':
            pass
        elif char in ['*', '+', '-', '^']:
            ops_stack.append(char)
        elif char.isdigit():
            nums_stack.append(float(char))
        elif char == ')':
            num = nums_stack.pop()
            op = ops_stack.pop()
            if op == '*':
                num = nums_stack.pop() * num
            elif op == '+':
                num = nums_stack.pop() + num
            elif op == '-':
                num = nums_stack.pop() - num
            elif op == '^':
                num += 1
            nums_stack.append(num)
    return nums_stack.pop()

if __name__ == '__main__':
    lisp_str = '(* (+ 2 6) (^ 3))'
    res = calcu(lisp_str)
    print('result:', res)
