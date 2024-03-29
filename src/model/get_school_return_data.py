from math import floor, ceil
import pandas as pd


def get_school_return_projections(
    number_alunos,
    number_alunos_naovoltando,
    number_professores,
    number_professores_naovoltando,
    number_salas,
    maxalunossalas,
    hours_classpresencial,
    hours_classpremoto,
    turnos,
    professorday,
    horaaula,
):
    """
    Calcula o número projetado de alunos e professores que retornam à escola.

    Parameters
    ----------
        number_alunos: int 
            Número de alunos autorizados a retornar à escola.
        number_alunos_naovoltando: int 
            Número de alunos não autorizados a retornar à escola.
        number_professores: int
            Número de professores autorizados a voltar à escola.
        number_professores_naovoltando: int
            Número de professores não autorizados a voltar à escola.
        number_salas: int
            Número de salas de aula disponíveis.
        maxalunossalas: int
            Máximo de aulos por sala.
        hours_classpresencial: int
            Duração do tempo em aula por dia (definido por modelo ou usuário).
        hours_classpremoto:
            Duração do tempo em aula remota por dia (definido por modelo ou usuário), hoje colocada automáticamanete em 0.
        maxalunossalas: int
            Número máximo de alunos por turma.
        turnos: int
            Total de Turnos dados em um dia.
        professorday:
            Máximo de horas de aula que o professor da em um dia.
        horaaula: int
            Duracao de uma aula.

    Returns
    -------
        number_alunos_retornantes : int
            Número projetado de alunos voltando à escola.
        number_professores_retornantes : int
            Número projetado  de professores que retornam à escola.
        limite_turmas;
            Número de turmas voltando.
        salasocupadas:
            Salas ocupadas por turno.
        salaslivres:
            Salas Livres por turno.
        diasletivos;
            Dias letivos necessários para atingit 800 hroas obrigatórias anuais.
        professoreslivres:
            Professores não retornantes do modelo.
        alunoslivres:
            Alunos não retornantes do modelo.
    """
    # Maximo de turmas por limitacao dos alunos
    number_alunos = number_alunos-number_alunos_naovoltando
    max_alunos = int(number_alunos/maxalunossalas)
    
    # Maximo de turmas por limitacao de salas
    max_salas = number_salas*turnos
    
    # Maximo de turmas por limitacao por professores
    number_professores = number_professores-number_professores_naovoltando
    max_professores = int(number_professores*((horaaula*professorday/60)/hours_classpresencial))
    
    # Identifica o gargalo
    limite_turmas = min(max_alunos, max_salas, max_professores)
    # Dado o gargalo, identificar as condições reais do retorno
    max_professores_por_turma = (horaaula*professorday/60)/hours_classpresencial
    number_professores_retornantes = ceil(limite_turmas/max_professores_por_turma)
    number_alunos_retornantes = ceil(limite_turmas*maxalunossalas)
    salasocupadas = ceil(limite_turmas/turnos)
    salaslivres = int(number_salas-salasocupadas)
    alunoslivres = int(number_alunos-number_alunos_retornantes)
    professoreslivres = int(number_professores-number_professores_retornantes)

    # Dias letivos

    # Dias letivos
    diasletivos = ceil(800/(hours_classpresencial+hours_classpremoto))

    return number_alunos_retornantes, number_professores_retornantes, limite_turmas, salasocupadas, salaslivres, diasletivos, alunoslivres, professoreslivres

def get_school_return_supplies(
    num_returning_students,
    num_returning_teachers,
    hours_per_day,
    max_students_per_class,
    config,
    number_days=7
):
    """
    Calcula o número de materiais escolares dado o número de alunos e professores que retornam.

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
            Number of days to consider for calculation. Default = 7 days.
            
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
    total_masks = ceil(student_masks + teacher_masks)
    total_sanitizer = ceil(student_sanitizer + teacher_sanitizer)

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
    number_alunos_retornantes, number_professores_retornantes, limite_turmas, salasocupadas, salaslivres, diasletivos, alunoslivres, professoreslivres = get_school_return_projections(
        params["number_alunos"],
        params["number_alunos_naovoltando"],
        params["number_professores"],
        params["number_professores_naovoltando"],
        params["number_salas"],
        params["maxalunossalas"],
        params["hours_classpresencial"],
        params["hours_classpremoto"],
        params["turnos"],
        params["professorday"],
        params["horaaula"],
    )

    # Calculate Amount of Required Protection Equipment
    total_masks, total_sanitizer, total_thermometers = get_school_return_supplies(
        number_alunos_retornantes,
        number_professores_retornantes,
        params["hours_classpresencial"],
        params["maxalunossalas"],
        config,
    )
    # Build School Return Data Dictionary
    return {
        "number_alunos_retornantes": number_alunos_retornantes,
        "number_professores_retornantes": number_professores_retornantes,
        "limite_turmas": limite_turmas,
        "salasocupadas": salasocupadas,
        "salaslivres": salaslivres,
        "alunoslivres": alunoslivres,
        "professoreslivres": professoreslivres,
        "diasletivos": diasletivos,
        "total_masks": total_masks,
        "total_sanitizer": round(total_sanitizer, 2),
        "total_thermometers": total_thermometers,
    }

def entrypoint_municipio(params, config, data):
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
    resultadoporescola = pd.DataFrame(columns=["Escola", "Alunos Retornantes", "Professores Retornantes", "Quantidade de Turmas", "Alunos Não Retornantes", "Professores Não Retornantes", "Salas ocupadas por turno", "Salas Livros por turnos", "Dias Letivos Necessários", "Máscaras (semanal)", "Álcool em gel (Litros - semanal)", "Termômetros (semanal"])
    alunos_retornantes_total = 0
    professores_retornantes_total = 0
    limite_turmas_total = 0
    salasocupadas_total = 0
    salaslivres_total = 0
    alunoslivres_total = 0
    professoreslivres_total = 0
    diasletivos_total = 0
    total_masks_total = 0
    total_sanitizer_total = 0
    total_thermometers_total = 0
    k = 0
    for i in data.index:
        # Calculate Number of Returning Students and Teachers
        alunos_retornantes, professores_retornantes, limite_turmas, salasocupadas, salaslivres, diasletivos, alunoslivres, professoreslivres = get_school_return_projections(
            data.loc[i]['alunos'],
            0,
            data.loc[i]['professores'],
            0,
            data.loc[i]['numsalas'],
            params["maxalunossalas"],
            params["hours_classpresencial"],
            params["hours_classpremoto"],
            params["turnos"],
            params["professorday"],
            params["horaaula"],
        )
        # Calculate Amount of Required Protection Equipment
        total_masks, total_sanitizer, total_thermometers = get_school_return_supplies(
            alunos_retornantes,
            professores_retornantes,
            params["hours_classpresencial"],
            params["maxalunossalas"],
            config,
        )
        alunos_retornantes_total = alunos_retornantes_total+alunos_retornantes
        professores_retornantes_total = professores_retornantes_total+professores_retornantes
        limite_turmas_total = limite_turmas_total+limite_turmas
        salasocupadas_total = salasocupadas_total+salasocupadas
        salaslivres_total = salaslivres_total+salaslivres
        alunoslivres_total = alunoslivres_total+alunoslivres
        professoreslivres_total = professoreslivres_total+professoreslivres
        diasletivos_total = diasletivos
        total_masks_total = total_masks_total+total_masks
        total_sanitizer_total = total_sanitizer_total+total_sanitizer
        total_thermometers_total = total_thermometers_total+total_thermometers
        resultadoporescola.loc[k] = [data.loc[i]['nomedaescola'],alunos_retornantes_total,professores_retornantes_total,limite_turmas_total,alunoslivres_total,professoreslivres_total,salasocupadas_total,salaslivres_total,diasletivos_total,total_masks_total,total_sanitizer_total,total_thermometers_total]
        k = k + 1
    # Build School Return Data Dictionary
    return {
        "number_alunos_retornantes": alunos_retornantes_total,
        "number_professores_retornantes": professores_retornantes_total,
        "limite_turmas": limite_turmas_total,
        "salasocupadas": salasocupadas_total,
        "salaslivres": salaslivres_total,
        "alunoslivres": alunoslivres_total,
        "professoreslivres": professoreslivres_total,
        "diasletivos": diasletivos_total,
        "total_masks": total_masks_total,
        "total_sanitizer": round(total_sanitizer_total, 2),
        "total_thermometers": total_thermometers_total,
    }, resultadoporescola
