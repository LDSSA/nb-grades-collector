import nbformat
from nbgrader import utils
"""
Grade function from here: 
https://github.com/LDSSA/ldsagrader/blob/0244c08c742815867cb7921b6845a6dd8f4b5e84/ldsagrader/utils.py#L52
"""
def grade(notebook_path):
    nb = nbformat.read(notebook_path, as_version=nbformat.NO_CONVERT)
    total_score = 0
    max_total_score = 0
    for cell in nb.cells:
        if utils.is_grade(cell):
            score, max_score = utils.determine_grade(cell)
            total_score += score
            max_total_score += max_score
    return total_score, max_total_score

email = input("Type your email:")
print(email)
total_score, max_total_score = grade("test_gradding_process_teacher_version.ipynb")
print(f"Your grade is {total_score} out of {max_total_score}!")

