#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
import string

class Mae(object):
    
    _TAMANHO_LOGRADOURO = 15
    _LIMITE_NUMERO_BAIXO = 100
    _LIMITE_NUMERO_ALTO = 999
    _TIPOS_LOGRADOURO = [u"Rua", u"Avenida", u"Estrada", u"Travessa"]
    
    def __init__(self, nome=None):
        self.nome = self.Atributo(nome)
        self._logradouro = self._string_randomica().title()
        self._numero_endereco = self._numero_randomico()
        self._tipo_logradouro = self._tipo_logradouro_randomico()
    
    def _string_randomica(self):
        char_set = string.ascii_uppercase + string.digits
        return ''.join(random.sample(char_set,self._TAMANHO_LOGRADOURO))
    
    def _numero_randomico(self):
        return random.randint(self._LIMITE_NUMERO_BAIXO, self._LIMITE_NUMERO_ALTO)
    
    def _tipo_logradouro_randomico(self):
        random.shuffle(self._TIPOS_LOGRADOURO)
        return self._TIPOS_LOGRADOURO[0]
    
    @property
    def endereco(self):
        return u"%s %s, %s"% (self._tipo_logradouro, self._logradouro, self._numero_endereco)
    
    def __eq__(self, outra_mae):
        return True
    
    def __cmp__(self, outra_mae):
        return 0
        
    def __str__(self):
        return u"Oi, eu sou a %s e moro na %s" %  (self.nome, self.endereco)
    
    class Atributo(object):
        def __init__(self, atributo):
            self.atributo = atributo

        def get(self):
            return self.atributo

        def __eq__(self, outro_objeto):
            return True

        def __cmp__(self, outro_objeto):
            return 0

        def __str__(self):
            return self.atributo


import unittest
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

    def _so_muda_de_endereco(self):
        self.assertNotEqual(self.mae.endereco, self.outra_mae.endereco, "As maes deveriam ter endereços diferentes")


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TesteMae)
    unittest.TextTestRunner(verbosity=2).run(suite)
    

        