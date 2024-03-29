#! /usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import gettext
import shlex
import sys
import os
import re
#from public.Misconceptions import runAllCode
#from public.Misconceptions import feedbackMisconceptions
from Misconceptions import runAllCode
from Misconceptions import feedbackMisconceptions
#import Misconceptions


from inginious import feedback
from inginious import rst
from inginious import input
import inginious_container_api.input as ingi_input
import inginious_container_api.feedback as ingi_feedback


# This runner suits for typical exercises of LSINF1101/FSAB1401
# Should be adapted if used in another occasion
# Structure used:
#  -One folder : src with a proposer answer, the tests and a subdirectory containing the templates
#  -A run file
#  -A task file
# Note that beside this structure we use the global folder common (c) and common/student (cs) containing:
#  -The compiler script         (c)
#  -The tests runner script     (c)
#  -The translations folder     (cs)

def init_translations():
    """
        Move the translations files to student directory
        Initialize gettext and translate to the proper language
    """
    lang = input.get_lang()
    try:
        trad = gettext.GNUTranslations(open("../course/common/student/$i18n/" + lang + ".mo", "rb"))
    except FileNotFoundError:
        trad = gettext.NullTranslations()
    trad.install()
    return lang


def tagAndMisconception(stdout):
    # Parse stdout for tags
    tag_lines = [line for line in stdout.split('\n') if line.startswith('TAG:')]
    tags = {line.split(':')[1].split('=')[0]: line.split('=')[1] == 'True' for line in tag_lines}

    tabMisconception = []
    # Set tags based on parsed output
    for tag, value in tags.items():
        print(f" tag {tag} = {value}")
        tabMisconception.append(tag)
        ingi_feedback.set_tag(tag, value)

    feedbackMisconceptionsString = ""
    for i in feedbackMisconceptions(tabMisconception):
        feedbackMisconceptionsString = feedbackMisconceptionsString + i + "\n"
    feedback.set_global_feedback(feedbackMisconceptionsString, append=True)


def compute_code():
    """
        Fills the template file with the student answer
        Returns the task's number of questions
    """
    for file in os.listdir('./src/Templates'):
        input.parse_template('./src/Templates/' + file, './student/' + file + '.py')
    data = input._load_input()
    return len([k for k in data['input'].keys() if '@' not in k])


def extract_student_code():
    """
    Extracts Python code from student files
    Returns a list of strings containing the code
    """
    student_code = []
    # Parcourir les fichiers dans le répertoire de l'étudiant
    for file in os.listdir('./student'):
        if file.endswith('.py'):  # Assurez-vous que le fichier est un fichier Python
            with open(os.path.join('./student', file), 'r') as f:
                code = f.read()  # Lire le contenu du fichier
                student_code.append(code)  # Ajouter le code à la liste
    return runAllCode(student_code[0])


def compile_code(tagTab):
    """
        Compiles both the student code and the exercise code
        Provides feedback if there is any compilation error
    """
    pyc_cmd = "python3 ../course/common/compiler.py "

    with open('log.out', 'w+', encoding="utf-8") as f:
        subprocess.call(shlex.split(pyc_cmd + './student/'), universal_newlines=True, stderr=f)
        f.seek(0)
        out_student = f.read()

    if out_student != "":
        rawhtml = rst.get_codeblock("", out_student)
        feedback.set_global_result('failed')
        feedbackMisconceptionsString = ""
        # print(feedbackMisconceptions(tagTab))
        for i in feedbackMisconceptions(tagTab):
            feedbackMisconceptionsString = feedbackMisconceptionsString + i + " \n "
        feedback.set_global_feedback(_("Ton programme ne compile pas: \n ") + rawhtml + "\n")
        # print(feedbackMisconceptionsString)
        feedback.set_global_feedback(feedbackMisconceptionsString, append=True)
        for tag in tagTab:
            print(f" tag {tag} = True")
            ingi_feedback.set_tag(tag, True)
        sys.exit(0)

    with open('logTests.out', 'w+', encoding="utf-8") as f:
        subprocess.call(shlex.split(pyc_cmd + './src/'), universal_newlines=True, stderr=f)
        f.seek(0)
        out_tests = f.read()

    if out_tests != "":
        rawhtml = rst.get_codeblock("", out_tests)
        feedback.set_global_result('failed')
        feedback.set_global_feedback(_("Le programme ne compile pas pour des raisons externes,"
                                       "veuillez contacter un administrateur dès que possible: \n ") + rawhtml + "\n")
        sys.exit(0)

    with open('logRunner.out', 'w+', encoding="utf-8") as f:
        subprocess.call(shlex.split(pyc_cmd + '../course/common/'), universal_newlines=True, stderr=f)
        f.seek(0)
        out_runner = f.read()

    if out_runner != "":
        rawhtml = rst.get_codeblock("", out_runner)
        feedback.set_global_result('failed')
        feedback.set_global_feedback(_("Le programme ne compile pas pour des raisons externes,"
                                       "veuillez contacter un administrateur dès que possible: \n ") + rawhtml + "\n")
        sys.exit(0)


def cleanup_output(error_content):
    """
        Provides a cleaner output from the error trace

        :param error_content: string returned by the unittest failures
    """
    cleaned_lines = []
    indexes = [match.start() for match in re.finditer('AssertionError: ', error_content)]
    for i in indexes:
        cleaned_lines.append(_('Test échoué:\n'))
        cleaned_lines.append(error_content[i + len("AssertionError: "): error_content.find("=" * 70, i)])
    return ''.join(cleaned_lines) if len(indexes) > 0 else error_content


def run_code(n_exercises, lang):
    """
        Runs the student code with the tests
        Provides feedback if it contains errors

        :param n_exercises: the task's number of exercices
        :param lang: the language used by the user
    """
    with open('err.txt', 'w+', encoding="utf-8") as f:
        os.chdir('./student')
        py_cmd = "run_student python3 Runner.pyc " + lang
        try:
            resproc = subprocess.Popen(shlex.split(py_cmd), universal_newlines=True, stderr=f, stdout=subprocess.PIPE)
            stdout, _ = resproc.communicate()
            result = resproc.returncode
        except (IOError, BrokenPipeError):
            result = 252
        f.flush()
        f.seek(0)
        errors = f.read()
        # print(errors)
        outerr = rst.get_codeblock("console", cleanup_output(errors))

    # expected error code: 252=outofmemory, 253=timedout
    # 127 = code returned by our runner
    if result == 127:
        feedback.set_global_result('success')
        # tagAndMisconception(stdout)
    elif result == 252:
        feedback.set_global_result('overflow')
    elif result == 253:
        feedback.set_global_result('timeout')
    else:  # Tests failed
        if n_exercises == 1:
            feedback.set_global_result('failed')
            feedback.set_global_feedback(("Il semble que votre code contienne des erreurs…\n\n") + outerr + "\n")
        else:
            for i in range(0, n_exercises + 1):
                regex = '@' + str(i) + '@: ((.+)(\n|\r){1})+'
                regex_question = re.search(regex, errors)
                if regex_question:
                    outerr_question = re.sub('"', '', regex_question.group(0)[5:])
                else:
                    outerr_question = False

                if i == 0:
                    feedback.set_global_result('failed')
                    if outerr_question:
                        feed = _("Vous avez fait des erreurs: \n\n") + rst.get_codeblock("console",
                                                                                         outerr_question) + "\n"
                        feedback.set_global_feedback(feed)
                else:
                    if outerr_question:
                        feed = _("Vous avez fait des erreurs: \n\n") + rst.get_codeblock("console",
                                                                                         outerr_question) + "\n"
                        feedback.set_problem_feedback(feed, "q" + str(i))
                    else:
                        feedback.set_problem_feedback(_("Vous avez correctement répondu à cette question."),
                                                      "q" + str(i))
                        feedback.set_problem_result('success', "q" + str(i))

    # tagAndMisconception(stdout)
    # ```
    # Parse stdout for tags
    tag_lines = [line for line in stdout.split('\n') if line.startswith('TAG:')]
    tags = {line.split(':')[1].split('=')[0]: line.split('=')[1] == 'True' for line in tag_lines}

    tabMisconception = []
    # Set tags based on parsed output
    for tag, value in tags.items():
        print(f" tag {tag} = {value}")
        tabMisconception.append(tag)
        ingi_feedback.set_tag(tag, value)

    feedbackMisconceptionsString = ""
    for i in feedbackMisconceptions(tabMisconception):
        feedbackMisconceptionsString = " \n" + str(i) + " \n"
        feedback.set_global_feedback(feedbackMisconceptionsString, append=True)
        # feedback.set_global_feedback(feedbackMisconceptionsString,append=True)
    if ((len(tabMisconception) != 0) and (result == 127)):
        feedback.set_global_result('failed')
        feedback.set_grade(95)
        # ```

def common_run():
    language = init_translations()
    num_exercises = compute_code()
    compile_code(extract_student_code())
    run_code(num_exercises, language)

if __name__ == '__main__':
    language = init_translations()
    num_exercises = compute_code()
    compile_code(extract_student_code())
    run_code(num_exercises, language)
