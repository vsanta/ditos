#!/usr/bin/env python
# -*- coding: UTF-8 -*-



import unittest
from ditos.mae.mae import Mae

class TesteMae(unittest.TestCase):

    def setUp(self):
        self.mae = Mae("Maria")
        self.outra_mae = Mae("Augusta")

    def test_tipo_de_logradouro_eh_do_conjunto_predefinidos(self):
        tipo_logradouro = self.mae._tipo_logradouro
        self.assertTrue(tipo_logradouro in self.mae._TIPOS_LOGRADOURO, "O tipo de logradouro %s nao esta na lista" % tipo_logradouro)
        self.assertTrue(tipo_logradouro in self.mae.endereco, "O tipo de logradouro deveria constrar no endereço")

    def test_endereco_de_mae_tem_logradouro(self):
        self.assertTrue(self.mae._logradouro != "", "O logradouro não pode ser vazio")
        self.assertTrue(self.mae._logradouro in self.mae.endereco, "O logradouro deveria constrar no endereço")

    def test_endereco_de_mae_tem_numero(self):
        self.assertEqual(int(self.mae._numero_endereco), self.mae._numero_endereco, "O numero do logradouro deve ser um numero")
        self.assertTrue(str(self.mae._numero_endereco) in self.mae.endereco, "O numero do logradouro deveria constrar no endereço")

    def test_mae_tem_nome(self):
        nome = "Sandra"
        minha_mae = Mae(nome)
        self.assertEqual(minha_mae.nome, nome, "O nome da mae deveria ser %s mas foi %s" % (nome, minha_mae.nome))
        
    def test_comparar_nome_de_mae_eh_sempre_igual(self):
        self.assertEqual(self.mae.nome, self.outra_mae.nome)

    def test_mae_sabe_quem_eh_e_onde_mora(self):
        mensagem_da_mae = "Oi, eu sou a Maria e moro na %s" % self.mae.endereco
        self.assertEqual(mensagem_da_mae, str(self.mae))

    def test_mae_eh_tudo_igual_so_muda_de_endereco(self):
        yield _mae_eh_tudo_igual()
        yield _so_muda_de_endereco()

    def _mae_eh_tudo_igual(self):
        self.assertEqual(self.mae, self.outra_mae, "As maes deveriam ser iguais")
        self.assertNotEqual(self.mae, "outra mae", "As maes deveriam ser iguais à outras maes")

    def _so_muda_de_endereco(self):
        self.assertNotEqual(self.mae.endereco, self.outra_mae.endereco, "As maes deveriam ter endereços diferentes")


if __name__ == '__main__':

    unittest.main()
    

        