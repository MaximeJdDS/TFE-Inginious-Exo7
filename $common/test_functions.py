from Misconceptions import *
import pytest


def test_1():
    assert 1 == 1


def test_AssignCompares():
    # Exemples d'utilisation
    code_exemple1 = """
    if x = 4:
        pass
    """

    code_exemple2 = """
    if (x = 4):
        pass
    """

    code_exemple3 = """
    if (y == 5):
        pass
    """

    code_exemple4 = """
    if x == 4:
        pass
    """

    assert AssignCompares(code_exemple1) == True
    assert AssignCompares(code_exemple2) == True
    assert AssignCompares(code_exemple3) == False
    assert AssignCompares(code_exemple4) == False



    # Testing the function with examples
def example_function():
    for i in range(5):
        print("Outer loop iteration:", i)
        for j in range(3):
            print("Inner loop iteration:", j)

def example_function_without_nested_loops():
    for i in range(5):
        print("Iteration:", i)

def example_function_for_and_while_loops():
    for i in range(4):
        print("Outer loop iteration:", i)
        while (i % 2 == 0):
            print("Inner loop iteration:", i)

def exemple_function_two_loops_not_nested():
    for i in range(4):
        print()
    for i in range(4):
        print()

def test_has_nested_loops():
    assert has_nested_loops(example_function) == True
    assert has_nested_loops(example_function_without_nested_loops) == False
    assert has_nested_loops(example_function_for_and_while_loops) == True
    assert has_nested_loops(exemple_function_two_loops_not_nested) == False



def function_1():
    x = True
    if x == True:
        return True
    return False

def function_2():
    y = False
    if y == True:
        return True
    return False

def function_3():
    def some_function():
        return True

    if some_function() == True:
        return True
    return False

def function_4():
    z = False
    if z == False:
        return True
    return False

def test_ComparisonWithBoolLiteral():
    functions_to_test = [function_1, function_2, function_3, function_4]
    Result = [False, False, False, False]
    for i, func in enumerate(functions_to_test, start=1):
        print(i,func)
        assert ComparisonWithBoolLiteral(func) == Result[i-1]



    # Fonction de test sans bloc else
def function_1():
    if True:
        return "Hello"
    return "Goodbye"

    # Fonction de test avec bloc else
def function_2():
    if True:
        return "Hello"
    else:
        return "Goodbye"

    # Fonction de test avec plusieurs blocs else
def function_3(x):
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"

    # Fonction de test avec "else" dans le nom d'une variable
def function_4(x):
    elsevariable = x * 2
    return elsevariable

def test_detect_else_keyword():
    assert detect_else_keyword(function_1) == False
    assert detect_else_keyword(function_2) == True
    assert detect_else_keyword(function_3) == True
    assert detect_else_keyword(function_4) == False



def function_1():
    if True:
        function_1()
    return "Goodbye"

def recursive_function(n):
    if n <= 0:
        return 1
    return n * recursive_function(n - 1)

def multiple_recursive_calls(n):
    if n <= 0:
        return 1
    return n * multiple_recursive_calls(n - 1) + multiple_recursive_calls(n - 2)

def non_recursive_call_to_recursive_function(n):
    if n <= 0:
        return 1
    return n * recursive_function(n - 1)

def conditional_recursive_call(n):
    if n <= 0:
        return 1
    if n % 2 == 0:
        return n * conditional_recursive_call(n - 1)
    else:
        return n * conditional_recursive_call(n - 2)
def number_of_numbers (n) :
    cnt= 0
    for i in range (len("n")):
        cnt+=1
    return cnt
def chiffres_pairs(n):
    if (number_of_numbers(n))//2 ==0 :
        return True
    else :
        return False


def test_detect_recursive_function():
    assert detect_recursive_function(function_1) == True
    assert detect_recursive_function(recursive_function) == True
    assert detect_recursive_function(multiple_recursive_calls) == True
    assert detect_recursive_function(non_recursive_call_to_recursive_function) == False
    assert detect_recursive_function(conditional_recursive_call) == True
    stringu=inspect.getsource(number_of_numbers)+inspect.getsource(chiffres_pairs)
    assert detect_recursive_function(stringu,function=False) == False


def example_function1(num):
    if num > 0:
        return True
    else:
        return False

def example_function2(num):
    if num > 0:
        return False
    else:
        return True

def example_function3(num):
    return num > 0

def test_MapToBooleanWithIf():
    assert MapToBooleanWithIf(example_function1) == False
    assert MapToBooleanWithIf(example_function2) == False
    assert MapToBooleanWithIf(example_function3) == False



def example_function1():
    return True if x > 0 else False
def example_function2():
    return x > 0
def example_function3():
    return y == 3 if True else False
def example_function4():
    if y > 3:
        return True
    else:
        return False

def test_MapToBooleanWithTernaryOperator():


    assert MapToBooleanWithTernaryOperator(example_function1) == False
    assert MapToBooleanWithTernaryOperator(example_function2) == False
    assert MapToBooleanWithTernaryOperator(example_function3) == True
    assert MapToBooleanWithTernaryOperator(example_function4) == False



    # Fonction de test
def f():
    return 5

def square(x):
    return x ** 2

def function1():
    return square(f)

def function2():
    return f

def function3():
    return add(f)

def test_ParenthesesOnlyIfArgument():
    # Liste des fonctions susceptibles d'être appelées sans parenthèses
    suspect_functions = ['f', 'g', 'h']  # Ajoutez ici les noms de vos fonctions suspectes

    # Exemples de tests
    assert ParenthesesOnlyIfArgument(square,suspect_functions)     == False
    assert ParenthesesOnlyIfArgument(function1, suspect_functions) == True
    assert ParenthesesOnlyIfArgument(function2, suspect_functions) == True
    assert ParenthesesOnlyIfArgument(function3, suspect_functions) == True



def example_function_with_parentheses(x):
    return (x + 5)

def example_function_without_parentheses(x):
    return x + 5

def example_function1(x):
    x = (x * 2)
    returnPrint = print("Pwouet")
    return x + 5

def example_function2(x):
    x = (x * 2)
    returnPrint = print("Pwouet")
    return (x + 5)

def test_ReturnCall():

    assert ReturnCall(example_function_with_parentheses) == True
    assert ReturnCall(example_function_without_parentheses) == False
    assert ReturnCall(example_function1) == False
    assert ReturnCall(example_function2) == True
