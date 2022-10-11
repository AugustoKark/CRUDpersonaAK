import unittest
from persona import Persona
from unittest.mock import patch

class TestPersona(unittest.TestCase):
    def test_constructor(self):
        persona = Persona()
        self.assertEqual(persona.__dict__, {'documento':1,'apellido':'Fernandez', 'nombre':'Anabel'})

   

if __name__ == '__main__':
    unittest.main()    
