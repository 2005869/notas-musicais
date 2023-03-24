NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)}


def escala(tonica, tonalidade):
    """
    Gera uma escala apartir de uma tônica e uma tonalidade.
    Args:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonialidade da escala
    Raises:
        ValueError: Caso a tônica não seja uma nota válida.
        KeyError: Caso a escala não exista ou aind não tenha sido implementada.
    Returns:
        Um dicionário com as notas da escala e os graus.
    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
        >>> escala('A', 'menor')
        {'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    try:
        tonica = tonica.upper()
        intervalos = ESCALAS[tonalidade]
        tonica_pos = NOTAS.index(tonica)
    except ValueError:
        raise ValueError(f'Esta nota não existe, tente uma destas { NOTAS }')
    except KeyError:
        raise KeyError(
            'Esta escala não existe ou não foi implementada. '
            f'Tente uma dessas { list(ESCALAS.keys()) }'
        )
    except AttributeError:
        raise AttributeError(
            f'Números não devem ser usados como tônica. Verifique as notas disponíveis { NOTAS }'
        )
    temp = []

    for intervalo in intervalos:
        nota = (tonica_pos + intervalo) % 12
        temp.append(NOTAS[nota])
    return {'notas': temp, 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
