from math import floor, ceil


def get_school_return_projections(
    num_alunos,
    num_professores,
    num_salas,
    horas_de_aula_por_turma,
    max_alunos_por_sala,
    horas_possiveis_sala=10,
    max_professores_por_turma=1,
):
    """
    Calculates projected number of students and teachers returning to school.

    Parameters
    ----------
        num_alunos: int 
            Número de alunos autorizados a retornar à escola.
        num_professores: int
            Número de professores autorizados a voltar à escola.
        num_salas: int
            Número de salas de aula disponíveis.
        horas_de_aula_por_turma: int
            Duração do tempo em aula por dia (definido por modelo ou usuário).
        max_alunos_por_sala: int
            Número máximo de alunos por turma.
        horas_possiveis_sala: int
            Total de horas disponíveis para aulas em um dia. Padrão: 10 = 5 horas x 2 turnos (manhã / tarde)

    Returns
    -------
        num_alunos_retornantes : int
            Número projetado de alunos voltando à escola.
        num_professores_retornantes : int
            Número projetado  de professores que retornam à escola.
    """
    # Maximo de turmas por limitacao dos alunos
    max_alunos = num_alunos/max_alunos_por_sala
    
    # Maximo de turmas por limitacao de salas
    max_salas = horas_possiveis_sala * num_salas / horas_de_aula_por_turma
    
    # Maximo de turmas por limitacao por professores
    max_professores = num_professores*max_professores_por_turma
    
    # Identifica o gargalo
    limite_turmas = min(max_alunos, max_salas, max_professores)
    
    # Dado o gargalo, identificar as condições reais do retorno
    num_professores_retornantes = ceil(limite_turmas*max_professores_por_turma)
    num_alunos_retornantes = ceil(limite_turmas*max_alunos_por_sala)

    return num_alunos_retornantes, num_professores_retornantes, limite_turmas




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
