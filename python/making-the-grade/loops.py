"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    if not student_scores:
        raise ValueError("Cannot operate with grades of an empty list")

    rounded_grade_list = []
    for grade in student_scores:
        rounded_grade = round(grade)
        rounded_grade_list.append(rounded_grade)
    return rounded_grade_list



def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    count_filed_student = 0
    for garde in student_scores:
        if garde <= 40:
            count_filed_student += 1
    return count_filed_student


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_students_list = []
    for grade in student_scores:
        if grade >= threshold:
            best_students_list.append(grade)
    return best_students_list


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    interval_size = (highest - 40) // 4
    d_grade = 41
    c_grade = 41 + interval_size
    b_grade = 41 + (interval_size * 2)
    a_grade = 41 + (interval_size * 3)
    return [d_grade, c_grade, b_grade, a_grade]




def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    rank_list = []
    for index, name in enumerate(student_names):
        student_info = f"{index + 1}. {name}: {student_scores[index]}"
        rank_list.append(student_info)
    return rank_list





def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for student_data in student_info:
        if isinstance(student_data, list):
            if student_data[1] == 100:
                return student_data
    return []
