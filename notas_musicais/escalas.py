"""
Módulo das escalas musicais.

Attributes:
   ESCALAS: Escalas implementadas usando a notação de inteiros
   NOTAS: Notas musicais

# ESCALAS

A escalas estão implementadas em uma constande chamada `ESCALAS`. Que é um dicionário onde as chaves são as escalas. Se quiser ver todas as escalas implementadas pode usar:

```py title="No seu shell interativo"
>>> from notas_musicais.escalas import ESCALAS
>>> ESCALAS
{'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)...}

```

A notação inteira para as escalas foi retirada da página [List of musical scales and modes](https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes) na wikipedia.

tip: Dica!
    Você pode contribuir com novas escalas usando a notação inteira:
    [Escalas wikipedia](https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes).
    Todos os Pull Requests serão bem vindos! :heart:

# NOTAS

As notas estão sendo definidas em uma contasnte `NOTAS`. Foi optado por menter somente as notas no formato Natural e o Sustenido (#) para a simplificação do fluxo de trabalho. Embora não esteja totalmente correto. Para ver as 12 notas você pode:

```py title="No seu shell interativo"
>>> from notas_musicais.escalas import NOTAS
>>> NOTAS
['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

```
"""
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
