from tree import LinkedBinaryTree
import re


class ArithmeticExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """Create an expression tree.
    
        In a single parameter form, token should be a leaf value (e.g., '42'),
        and the expression tree will have that value at an isolated node.
    
        In a three-parameter version, token should be an operator,
        and left and right should be existing ArithmeticExpressionTree instances
        that become the operands for the binary operator.
        """
        super().__init__()                        # LinkedBinaryTree initialization
        if not isinstance(token, str):
            raise TypeError('Token must be a string')
        self._add_root(token)                     # use inherited, nonpublic method
        if left is not None:                      # presumably three-parameter form
            if token not in '+-*x/,^':
                raise ValueError('token must be valid operator')
            self._attach(self.root(), left, right)  # use inherited, nonpublic method

    def __str__(self):
        """Return string representation of the expression."""
        pieces = []                 # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element()))                    # leaf value as a string
        else:
            result.append('(')                                 # opening parenthesis
            self._parenthesize_recur(self.left(p), result)     # left subtree
            result.append(p.element())                         # operator
            self._parenthesize_recur(self.right(p), result)    # right subtree
            result.append(')')                                 # closing parenthesis

    def evaluate(self):
        """Return the numeric result of the expression."""
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        """Return the numeric result of subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())      # we assume element is numeric
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            elif op == ',':
                return '{},{}'.format(left_val, right_val)
            elif op == '*':                          # treat 'x' or '*' as multiplication
                return left_val * right_val
            elif op == '^':
                return left_val ** right_val


def tokenize(raw):
    """Produces list of tokens indicated by a raw expression string.

    For example the string '(43-(3*10))' results in the list
    ['(', '43', '-', '(', '3', '*', '10', ')', ')']
    """
    SYMBOLS = set('+-x*/^(), ')    # allow for '*' or 'x' for multiplication

    mark = 0
    tokens = []
    n = len(raw)
    for j in range(n):
        if raw[j] in SYMBOLS:
            if mark != j:
                tokens.append(raw[mark:j])  # complete preceding token
            if raw[j] != ' ':
                tokens.append(raw[j])       # include this token
            mark = j+1                    # update mark to being at next index
    if mark != n:
        tokens.append(raw[mark:n])      # complete preceding token
    return tokens


def build_expression_tree(tokens):
    """Returns an ArithmeticExpressionTree based upon by a tokenized expression.

    tokens must be an iterable of strings representing a fully parenthesized
    binary expression, such as ['(', '43', '-', '(', '3', '*', '10', ')', ')']
    """
    S = []                                            # we use Python list as stack
    for t in tokens:
        if t in '+-x*/^':                              # t is an operator symbol
            S.append(t)                               # push the operator symbol
        elif t not in '()':                           # consider t to be a literal
            S.append(ArithmeticExpressionTree(t))     # push trivial tree storing value
        elif t == ')':                                # compose a new tree from three constituent parts
            right = S.pop()                           # right subtree as per LIFO
            op = S.pop()                              # operator symbol
            left = S.pop()                            # left subtree
            S.append(ArithmeticExpressionTree(op, left, right))  # repush tree
        # we ignore a left parenthesis
    return S.pop()


def build_algebraic_tree(tokens):
    S = []
    for t in tokens:
        if t in ',':
            S.append(t)
        elif t not in '()':
            S.append(ArithmeticExpressionTree(t))
        elif t == ')':
            right = S.pop()
            op = S.pop()
            left = S.pop()
            assert isinstance(op, str)
            S.append(ArithmeticExpressionTree(op, left, right))
    return S.pop()


def convert_expression(exp):
    """
    This function simply takes an expression and replaces the functions in it by their
    names. It then stores the replacements done in a dictionary.
    It finally returns the replacements dictionary and the new expression.
    """
    # This is to match a pattern like x1, y3
    patt1 = re.compile('([x y]\d*,*)', re.IGNORECASE)

    # This is to match a function e.g f(x1,x2)
    patt2 = re.compile('((\w+\(([x y]\d*,*)+\))*,*)')

    # This is to match patterns like g(f(x1,x2),y2)
    regex1 = re.compile('\w+\(({}|{})+\)'.format(patt1.pattern, patt2.pattern))

    # This is to match the power operator **
    regex2 = re.compile(r'\*\*')

    new_exp = exp      # Keep a copy of exp for processing
    replacements = dict()   # A dictionary containing the replacements done

    # This fragment locate function pattern in an expression and replaces them with
    # function's name
    # It also stores the replacements done in the replacements dictionary
    for match in re.finditer(regex1, exp):
        s = match.start()
        e = match.end()
        f_name = exp[s:e].split('(')[0]  # splits by '(', the function and takes only its name
        new_exp = new_exp.replace(exp[s:e], f_name)
        replacements[exp[s]] = exp[s:e]

    # This is to handle the power operator
    new_exp2 = new_exp
    for match in re.finditer(regex2, new_exp):
        s = match.start()
        e = match.end()
        new_exp2 = new_exp2.replace(new_exp[s:e], '^')
        replacements['^'] = new_exp[s:e]

    if re.search(regex2, new_exp):
        new_exp = new_exp2

    return new_exp, replacements


def expression_formats(exp, order):
    """
    Takes an expression in an infix order and transform it to another format.
    It first replaces the functions by their name by calling convert_expression function
    which returns new expression and the replacement dictionary.
    It then build the expression tree by calling the build_expression_tree function.
    It further creates a new expression in the desired format.
    All the function names in this new format are replaced by their original function look
    e.g add replaced with add(x1,x2).
    """
    expr, repl = convert_expression(exp)
    new_exp = ''
    exp_tree = build_expression_tree(tokenize(expr))

    # Create new expression in the desired format
    if order == 'inorder':
        for c in exp_tree.inorder():
            new_exp += c.element()
    elif order == 'preorder':
        for c in exp_tree.preorder():
            new_exp += c.element()
    elif order == 'postorder':
        for c in exp_tree.postorder():
            new_exp += c.element()

    # replace the function's name with the function it self
    for k in repl.keys():
        new_exp = new_exp.replace(k, repl[k])

    return new_exp


if __name__ == '__main__':
    """
    big = build_expression_tree(tokenize('((((3+1)x3)/((9-5)+2))-((3x(7-4))+6))'))
    print(big, '=', big.evaluate())
    print('length =', len(big))
    print('Inorder traversal as follows: ')
    for i in big.inorder():
        print(i.element())
    """
    exp = '(f(g(x1,x2),y2)+(a**(a-b)))'
    # print(convert_expression(exp))
    print(expression_formats(exp, 'postorder'))