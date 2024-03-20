#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import ast
import inspect


def AssignCompares(code):
    # Expression régulière pour rechercher une affectation dans une condition avec des parenthèses
    patternParanthese = r'\bif\s*\([^=]+?=\s*(?!=).+?\)\s*:'
    # Expression régulière pour rechercher une affectation dans une condition sans parenthèses
    patternSansParanthese = r'\bif\s+\w+\s*=\s*(?!=).+?\b:'
    if (re.search(patternParanthese, code) or re.search(patternSansParanthese, code)):
        return True
    return False


def has_nested_loops(func):
    """
    Check if a function contains nested loops.

    Parameters:
        func (function): The function to check.

    Returns:
        bool: True if nested loops are found, False otherwise.
    """
    source_lines, _ = inspect.getsourcelines(func)
    source = ''.join(source_lines)
    tree = ast.parse(source)

    def _check_for_nested_loops(node, depth=0):
        if isinstance(node, (ast.While, ast.For)):
            depth += 1
            if depth > 1:
                return True
        for child_node in ast.iter_child_nodes(node):
            if _check_for_nested_loops(child_node, depth):
                return True
        return False

    for node in ast.walk(tree):
        if _check_for_nested_loops(node):
            return True

    return False


def ComparisonWithBoolLiteral(func):
    """
    Detects if a function contains a condition testing if a variable or function result is equal to True.

    Args:
    func (function): The function to analyze.

    Returns:
    bool: True if such a condition is found, False otherwise.
    """
    func_source = inspect.getsource(func)
    tree = ast.parse(func_source)
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare):
            for op in node.ops:
                if isinstance(op, ast.Eq):
                    for value in node.comparators:
                        if isinstance(value, ast.NameConstant) and value.value is True:
                            return True
    return False


def MapToBooleanWithIf(func):
    source = inspect.getsource(func)
    parsed = ast.parse(source)

    for node in ast.walk(parsed):
        if isinstance(node, ast.If):
            if isinstance(node.test, ast.Compare):
                left = node.test.left
                if isinstance(left, ast.Name) and left.id == "num":
                    if len(node.body) == 1 and isinstance(node.body[0], ast.Return):
                        if isinstance(node.body[0].value, ast.NameConstant):
                            if node.body[0].value.value == True:
                                return True
                    if len(node.orelse) == 1 and isinstance(node.orelse[0], ast.Return):
                        if isinstance(node.orelse[0].value, ast.NameConstant):
                            if node.orelse[0].value.value == False:
                                return True
    return False


def ParenthesesOnlyIfArgument(func, suspect_functions):
    """
    Cette fonction détecte si une fonction utilise un appel de fonction
    sans parenthèses, ce qui peut résulter en une référence à la fonction plutôt que
    l'appel de la fonction elle-même.

    @param func: La fonction Python à analyser.
    @param suspect_functions: Une liste de noms de fonctions susceptibles d'être appelées sans parenthèses.
    @pre: func doit être une fonction valide.
    @post: Retourne True si des appels de fonction sans parenthèses sont détectés, False sinon.
    """

    # Obtient le code source de la fonction
    source_lines, _ = inspect.getsourcelines(func)
    source_code = ''.join(source_lines)

    # Parse le code en un arbre de syntaxe abstrait
    tree = ast.parse(source_code)

    # Parcours l'arbre pour rechercher les appels de fonction sans parenthèses
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if node.id in suspect_functions:
                # Vérifie si le nom de la fonction est utilisé comme un appel de fonction
                for parent_node in ast.walk(tree):
                    if isinstance(parent_node, ast.Call):
                        if isinstance(parent_node.func, ast.Name) and parent_node.func.id == node.id:
                            return False  # Une référence à une fonction suspecte est correctement appelée
                        # Vérifie les appels de fonction à l'intérieur des arguments
                        for arg in parent_node.args:
                            if isinstance(arg, ast.Call) and isinstance(arg.func, ast.Name) and arg.func.id == node.id:
                                return False  # Une référence à une fonction suspecte est correctement appelée dans les arguments
                return True  # Une référence directe à une fonction suspecte sans parenthèses
    return False


def detect_recursive_function(function):
    source = inspect.getsource(function)
    tree = ast.parse(source)

    function_name = function.__name__

    # Variable pour indiquer si une récursion est détectée
    recursive_detected = False

    # Fonction récursive interne pour parcourir l'arbre syntaxique
    def traverse(node):
        nonlocal recursive_detected
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                called_function_name = node.func.id
                if called_function_name == function_name:
                    recursive_detected = True
        for child_node in ast.iter_child_nodes(node):
            traverse(child_node)

    # Appeler la fonction récursive interne pour parcourir l'arbre syntaxique
    traverse(tree)

    # Retourner True si une récursion est détectée, sinon False
    return recursive_detected


def detect_else_keyword(function):
    source = inspect.getsource(function)
    tree = ast.parse(source)

    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            if node.orelse:
                return True
    return False


def RecursiveFunctionNeedsIfElse(func):
    return detect_recursive_function(func) and detect_else_keyword(func)


def ReturnCall(func):
    """
    Detects the presence of parentheses in return statements of a given function.

    @param func: The function to analyze.
    @pre: func must be a Python function.
    @post: Returns True if parentheses are detected in return statements, otherwise False.
    """
    source = inspect.getsource(func)
    for line in source.split('\n'):
        if ' return (' in line:
            if '(' in line or ')' in line:
                return True
    return False

def ReturnCallFile(file_path):
    """
    Detects the presence of parentheses in return statements of a given function.

    @param func: The function to analyze.
    @pre: func must be a Python function.
    @post: Returns True if parentheses are detected in return statements, otherwise False.
    """

    with open(file_path, 'r') as file:
        source = file.read()
    for line in source.split('\n'):
        if ' return (' in line:
            if '(' in line or ')' in line:
                return True
    return False


def MapToBooleanWithTernaryOperator(func):
    return False


#########################################################
#		 RUN ALL FUNCTION			#
#							#
#########################################################


def runAllFunc(func):
    StudentFunction = func

    ApiFunction = [has_nested_loops,  # Function with function parameter
                   ComparisonWithBoolLiteral,
                   RecursiveFunctionNeedsIfElse,
                   MapToBooleanWithIf,
                   MapToBooleanWithTernaryOperator,
                   ReturnCall]

    TagStack = []

    for fonction in ApiFunction:
        if fonction(StudentFunction):
            TagStack.append(fonction.__name__)
    return TagStack


def runAllCode(code):
    TagStack = []
    ApiCodeFunction = [AssignCompares  # Function with code parameter
                       ]

    for fonction in ApiCodeFunction:
        if fonction(code):
            TagStack.append(fonction.__name__)
    return TagStack


dicoFeedback = {
    "AssignCompares": "Nous pensons que tu as fait une erreur au niveau de la condition du if.\nPour rappel, \"=\" c'est pour assigner une valeur à une variable.\nSi tu veux comparer tu dois utiliser \"==\".",
    "ComparisonWithBoolLiteral": "Nous pensons que tu as fait une erreur au niveau de la condition du if. Tu as déjà un boolean, tu n'as pas besoin de le comparer à un autre boolean pour faire ta condition. Tu peux tout simplement écrire \"if nomDeLaVariable : \"",
    "MapToBooleanWithIf": "Nous pensons que ce que tu as écris n'est pas une bonne habitude à prendre : Ce n'est pas nécessaire de faire des if/else pour renvoyer un Boolean, tu peux simplement écrire return CONDITION.",
    "MapToBooleanWithTernaryOperator": "Nous pensons que ce que tu as écris n'est pas une bonne habitude à prendre : tu peux simplement écrire return CONDITION.",
    "ParenthesesOnlyIfArgument": "Attention, Ne pas mettre de paranthèse derrière le nom d'une fonction va donner l'adresse de la fonction. Si tu veux faire appel à une fonction sans paramètre ",
    "RecursiveFunctionNeedsIfElse": "Ce n'est pas obligatoire de faire un cas else. C'est possible d'écrire une fonction récursive sans else avec le cas de base de manière implicite.",
    "ReturnCall": "Nous pensons que tu as fait une erreur au niveau du \"return\".\nLorsque python lit \"return\" il va exécuter tout ce qui suit puis renvoyer le résultat. \nAinsi, les paranthèses ne sont pas nécessaires."}


def feedbackMisconceptions(tabMisconception, verbose=False):
    """
    Return a array with the feedback for each Misconceptions in tabMisconception
    Use verbose = True if you want to print the Misconception who's in tabMisconception but not in dicoFeedback
    Please refer to the variable 'dicoFeedback' to know the list of Misconceptions handled.
    """
    tabOutput = []

    for misc in tabMisconception:
        if misc in dicoFeedback:
            tabOutput.append(dicoFeedback[misc])
        elif (verbose):
            print(misc)
    return tabOutput

def tagTransfer(tagDico):
    for tag in tagDico:
        print(f"TAG:{tag}=True")