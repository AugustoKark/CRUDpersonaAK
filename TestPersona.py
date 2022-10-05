import unittest
from persona import Persona
from unittest.mock import patch

class TestPersona(unittest.TestCase):
    def test_constructor(self):
        persona = Persona()
        self.assertEqual(persona.__dict__, {'documento':1,'apellido':'Fernandez', 'nombre':'Anabel'})

    @patch('builtins.input', side_effects=[3, 'Trump', 'Donald'])
    def test_input(self):
        persona = Persona()
        persona.input()
        self.assertEqual(persona.__dict__, {'documento':3,'apellido':'Trump', 'nombre':'Donald'})

if __name__ == '__main__':
    unittest.main()    
