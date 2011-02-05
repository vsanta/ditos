#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from optparse import OptionParser
class Runner(object):
    
    def __init__(self):
        self.parser = OptionParser()
        self._configura_opcoes()
        self._extrai_opcoes()
    
    def main(self):
        raise NotImplementedError("Voce deve implementar como rodar seu ditado")
        
    def testes(self):
        raise NotImplementedError("Voce deve implementar como rodar seus testes")
    
    def roda(self):
        if self._opcaoes.teste:
            self.testes()
        else:
            self.main()
        
    def _extrai_opcoes(self):    
        (self._opcaoes, self._argumentos) = self.parser.parse_args()
        self._teste = self._opcaoes.teste
        
    def _valida_opcoes(self, opcoes):
        raise NotImplementedError("Voce deve implementar a validacao dos seus parametros")

    def _configura_opcoes(self):
        self.parser.add_option("-t", "--teste",action="store_true",
                          dest="teste", default=False,
                          help="roda os testes")


import unittest
class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.runner = Runner()
        
    def test_runner_pede_implementacao_de_validacao(self):
        try:
            self.runner._valida_opcoes(None)
            self.assertFalse(False)
        except NotImplementedError:
            self.assertTrue(True)
            
    def test_runner_pede_implementacao_de_testes(self):
        try:
            self.runner.testes()
            self.assertFalse(False)
        except NotImplementedError:
            self.assertTrue(True)

    def test_runner_pede_implementacao_de_main(self):
        try:
            self.runner.main()
            self.assertFalse(False)
        except NotImplementedError:
            self.assertTrue(True)

from mae import TesteMae, Mae
class MaeRunner(Runner):

    def main(self):
        uma_mae = Mae(self._opcaoes.uma)
        outra_mae = Mae( self._opcaoes.outra)
        sao_iguais = "Sim"  if uma_mae == outra_mae else "Nao"
        print "%s é igual a %s? %s" % (uma_mae.nome, outra_mae.nome, sao_iguais)
        print "So que %s mora em %s e %s na %s" % (uma_mae.nome, uma_mae.endereco, outra_mae.nome, outra_mae.endereco)

    def testes(self):
        suite = unittest.TestLoader().loadTestsFromTestCase(TesteMae)
        unittest.TextTestRunner(verbosity=2).run(suite)

    def _extrai_opcoes(self):    
        super(MaeRunner, self)._extrai_opcoes()
        if self._valida_opcoes() or self._teste:
            return ( self._opcaoes.uma, self._opcaoes.outra)

    def _valida_opcoes(self):
        if not (self._opcaoes.uma and self._opcaoes.outra) and not self._teste:
            raise ValueError("Voce deve passar --uma mae e --outra mae ou usar --teste")
        return True

    def _configura_opcoes(self):
        super(MaeRunner, self)._configura_opcoes()
        self.parser.add_option("-u", "--uma", dest="uma",
                          help="nome de uma mae")
        self.parser.add_option("-o", "--outra",
                          dest="outra", 
                          help="nome de outra mae")

if __name__ == '__main__':
   runner = MaeRunner()
   runner.roda()                             


# if __name__ == '__main__':
#     unittest.main()
