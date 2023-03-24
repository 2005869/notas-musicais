from pytest import mark, raises

from notas_musicais.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():
    # Arrange
    tonica = 'c'
    tonalidade = 'maior'

    # Act
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    # Arrange
    tonalidade = 'maior'
    tonica = 'x'

    mensagem_de_erro = f'Esta nota não existe, tente uma destas { NOTAS }'

    # Act
    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    # Assert
    assert mensagem_de_erro == error.value.args[0]


def test_deve_retornar_um_erro_dizendo_que_a_escala_nao_existe():
    # Arrange
    tonica = 'C'
    tonalidade = 'tonalidade'

    mensagem_de_erro = f'Esta escala não existe ou não foi implementada. Tente uma dessas { list(ESCALAS.keys()) }'

    # Act
    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(  # Arrange
    'tonica, tonalidade, esperado',
    [
        ('C', 'maior', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', 'maior', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', 'maior', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
        ('C', 'menor', ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#']),
        ('C#', 'menor', ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']),
        ('F', 'menor', ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#']),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, tonalidade, esperado):
    resultado = escala(tonica, tonalidade)  # Act
    assert resultado['notas'] == esperado  # Assert


def test_deve_retornar_os_sete_graus():
    tonica = 'c'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escala(tonica, tonalidade)
    assert resultado['graus'] == esperado


# AttributeError
def test_deve_retornar_um_erro_dizendo_que_numero_nao_pode_ser_tonica():
    # Arrange
    tonica = 1
    tonalidade = 'maior'

    mensagem_de_erro = f'Números não devem ser usados como tônica. Verifique as notas disponíveis { NOTAS }'

    # Act
    with raises(AttributeError) as error:
        escala(tonica, tonalidade)

    # Assert
    assert mensagem_de_erro == error.value.args[0]
