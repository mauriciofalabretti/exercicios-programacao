from Desafio060 import calcular_fatorial, valida_inteiros
import pytest

def test_calculo_fatorial_5():
    assert calcular_fatorial(5) == 120

def test_fatorial_zero():
    assert calcular_fatorial(0) == 1

def test_valida_inteiros_numero_valido(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "5")
    assert valida_inteiros("Mensagem qualquer") == 5

def test_valida_inteiros_rejeita_textos(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    with pytest.raises(ValueError):
        valida_inteiros("Mensagem qualquer")