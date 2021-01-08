"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from unittest.mock import call, patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_9_51(self):
        """Função que testa 9.51."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['9.51']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = [
                'São necessárias:', 'moedas de R$ 1.00: 9',
                'moedas de R$ 0.50: 1', 'moedas de R$ 0.01: 1'
            ]
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)

    def test_5_00(self):
        """Função que testa 5.00."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['5.00']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = ['São necessárias:', 'moedas de R$ 1.00: 5']
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)

    def test_9_99(self):
        """Função que testa 9.99."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['9.99']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = [
                'São necessárias:', 'moedas de R$ 1.00: 9',
                'moedas de R$ 0.50: 1', 'moedas de R$ 0.25: 1',
                'moedas de R$ 0.10: 2', 'moedas de R$ 0.01: 4'
            ]
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)

    def test_0_09(self):
        """Função que testa 0.09."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['0.09']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = [
                'São necessárias:', 'moedas de R$ 0.05: 1',
                'moedas de R$ 0.01: 4'
            ]
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)

    def test_0_37(self):
        """Função que testa 0.37."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['0.37']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 1
            valores = [
                'São necessárias:', 'moedas de R$ 0.25: 1',
                'moedas de R$ 0.10: 1', 'moedas de R$ 0.01: 2'
            ]
            calls = list(map(call, valores))
            mock_print.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
