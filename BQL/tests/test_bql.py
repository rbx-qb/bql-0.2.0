import unittest
from src.bql_interpreter import BQLInterpreter

class TestBQL(unittest.TestCase):
    def setUp(self):
        self.bql = BQLInterpreter()
    
    def test_create_register(self):
        self.bql.execute("CREATE q1 4")
        self.assertIn("q1", self.bql.registers)
        self.assertEqual(len(self.bql.registers["q1"]["state"]), 4)
    
    def test_entanglement(self):
        self.bql.execute("CREATE q1 4")
        self.bql.execute("CREATE q2 4")
        self.bql.execute("ENTANGLE q1 q2")
        self.assertTrue((self.bql.registers["q1"]["state"] == self.bql.registers["q2"]["state"]).all())

if __name__ == '__main__':
    unittest.main()

