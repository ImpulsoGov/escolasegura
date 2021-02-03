from math import floor, ceil


def get_school_return_projections(
    num_students,
    num_teachers,
    num_classrooms,
    hours_per_day,
    max_students_per_class,
    hours_day_classes=10,
):
    """
    Calculates projected number of students and teachers returning to school.

    Parameters
    ----------
        num_students : int or float
            Number of students allowed to return to school.
        num_teachers : int or float
            Number of teachers allowed to return to school.
        num_classrooms : int or float
            Number of classrooms available.
        hours_per_day : string
            Duration of time spent in class per day (defined by user/model).
        max_students_per_class : int or float
            Maximum number of students per class.
        hours_day_classes : dict
            Total hours available for classes in a day. Default: 10 = 5 hours x 2 shifts (morning/afternoon)

    Returns
    -------
        num_returning_students : int
            Projected numbers of students returning to school.
        num_returning_teachers : int
            Project number of teachers returning to school.
    """
    # 1. Total hours of classrooms available per day
    max_hours_classroom = hours_day_classes * num_classrooms / hours_per_day

    # 2. Total groups of students per day
    max_groups = min(num_teachers, max_hours_classroom)

    # 3. Total students & teatchers to return
    num_returning_students = max_students_per_class * max_groups
    num_returning_teachers = max_groups

    return num_returning_students, num_returning_teachers, max_groups



def get_school_return_supplies(
    num_returning_students,
    num_returning_teachers,
    hours_per_day,
    max_students_per_class,
    config,
    number_days=7
):
    """
    Calculates number of school supplies given number of return students and faculty.

    Parameters
    ----------
        num_returning_students : int or float
            Number of returning students.
        num_returning_teachers : int or float
            Number of returning teachers.
        hours_per_day : string
            Duration of time spent in class per day (defined by user/model).
        max_students_per_class : int or float
            Maximum number of students per class.
        config : dict
            General school return parameters.
        number_days : int
            Number of days to consider for calculation. Default = 30 days.

    Returns
    -------
        total_masks : int
            Total number of masks required.
        total_sanitizer : int or float
            Total amount of hand sanitizer required.
        total_thermometers : int
            Total amount of thermometers required.
    """

    # Load Fixed Parameters

    # Protection Equipment and Cleaning Supplies
    mask_time_limit = config["br"]["simule"]["supplies"]["mask_time_limit"]
    sanitizer_per_person_per_hour = config["br"]["simule"]["supplies"]["sanitizer_per_person_per_hour"]
    people_per_thermometer = config["br"]["simule"]["supplies"]["people_per_thermometer"]
    
    # Determine Masks and Hand Sanitizer for Students
    hours_per_student = number_days * hours_per_day

    masks_per_student = max(
        number_days, ceil(hours_per_student / mask_time_limit)
    )
    student_masks = num_returning_students * masks_per_student
    student_sanitizer = (
        num_returning_students * hours_per_student * sanitizer_per_person_per_hour
    )

    # Determine Masks and Hand Sanitizer for Teachers
    student_hours = num_returning_students * number_days * hours_per_day
    class_hours = student_hours / max_students_per_class
    try:
        hours_per_teacher = class_hours / num_returning_teachers
    except ZeroDivisionError:
        hours_per_teacher = 0

    masks_per_teacher = ceil(hours_per_teacher / mask_time_limit)
    teacher_masks = num_returning_teachers * masks_per_teacher
    teacher_sanitizer = (
        num_returning_teachers * hours_per_teacher * sanitizer_per_person_per_hour
    )

    # Determine Total Quantities of Masks and Hand Sanitizer
    total_masks = student_masks + teacher_masks
    total_sanitizer = student_sanitizer + teacher_sanitizer

    # Determine Number of Thermometers
    total_thermometers = ceil(num_returning_students / people_per_thermometer)

    return total_masks, total_sanitizer, total_thermometers


def entrypoint(params, config):
    """
    Entrypoint for school return data.

    Parameters
    ----------
        params : dict
            Dictionary with user input from frontend.
        config : dict
            Dictionary with fixed parameters.

    Returns
    -------
        school_return_data : dict
            Dictionary with numbers of returning teachers, students, and
            necessary protective equipment.

    """

    school_return_data = dict()

    # Calculate Number of Returning Students and Teachers
    num_returning_students, num_returning_teachers, max_groups = get_school_return_projections(
        params["number_students"],
        params["number_teachers"],
        params["number_classrooms"],
        params["hours_per_day"],
        params["max_students_per_class"],
    )
    # Calculate Amount of Required Protection Equipment
    total_masks, total_sanitizer, total_thermometers = get_school_return_supplies(
        params["number_students"],
        params["number_teachers"],
        params["hours_per_day"],
        params["max_students_per_class"],
        config,
    )
    # Build School Return Data Dictionary
    return {
        "num_returning_students": num_returning_students,
        "num_returning_teachers": num_returning_teachers,
        "max_groups": max_groups,
        "total_masks": round(total_masks, 0),
        "total_sanitizer": round(total_sanitizer, 0),
        "total_thermometers": round(total_thermometers, 1),
    }
