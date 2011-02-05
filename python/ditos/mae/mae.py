#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random
import string

class Mae(object):
    pass

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
        if(type(outra_mae) == Mae):
            return True
        return False
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