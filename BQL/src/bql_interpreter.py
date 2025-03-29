import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute

class BQLInterpreter:
    d   self.registers = {}
    
    def execute(self, command):
        tokens = command.split()
        if not tokens:
            return
        
        action = tokens[0].upper()
        
        if action == "CREATE":
            self.create_register(tokens[1], int(tokens[2]))
        elif action == "ENTANGLE":
            self.entangle(tokens[1], tokens[2])
        elif action == "APPLY_NOISE":
            self.apply_noise(tokens[1], float(tokens[2]))
        elif action == "DISTILL":
            self.distill(tokens[1])
        elif action == "SHOW":
            self.show(tokens[1])
        elif action == "PLOT":
            self.plot_state(tokens[1])
        elif action == "SIMULATE":
            self.simulate_qiskit()
        else:
            print("Unknown command")
    
    def create_register(self, name, levels):
        """Cria um registro bosônico com estados iniciais."""
        self.registers[name] = {"levels": levels, "state": np.zeros(levels)}
        self.registers[name]["state"][0] = 1  # Estado inicial |0⟩
        print(f"Created bosonic register {name} with {levels} levels.")
    
    def entangle(self, reg1, reg2):
        """Cria emaranhamento entre dois registros."""
        if reg1 in self.registers and reg2 in self.registers:
            print(f"Entangled {reg1} and {reg2} using rotation-based encoding.")
            self.registers[reg1]["state"] = (self.registers[reg1]["state"] + self.registers[reg2]["state"]) / np.sqrt(2)
            self.registers[reg2]["state"] = self.registers[reg1]["state"]
        else:
            print("Register not found.")
    
    def apply_noise(self, reg, strength):
        """Aplica ruído gaussiano no registro bosônico."""
        if reg in self.registers:
            noise = np.random.normal(0, strength, size=len(self.registers[reg]["state"]))
            self.registers[reg]["state"] += noise
            self.registers[reg]["state"] /= np.linalg.norm(self.registers[reg]["state"])  # Normaliza
            print(f"Applied noise with strength {strength} to {reg}.")
        else:
            print("Register not found.")
    
    def distill(self, reg):
        """Aplica destilação de emaranhamento."""
        if reg in self.registers:
            self.registers[reg]["state"] = np.abs(self.registers[reg]["state"])  # Remove fase negativa
            self.registers[reg]["state"] /= np.linalg.norm(self.registers[reg]["state"])  # Normaliza
            print(f"Applied entanglement distillation on {reg}.")
        else:
            print("Register not found.")
    
    def show(self, reg):
        """Exibe o estado do registro."""
        if reg in self.registers:
            print(f"State of {reg}: {self.registers[reg]['state']}")
        else:
            print("Register not found.")
    
    def plot_state(self, reg):
        """Gera um gráfico do estado do registro bosônico."""
        if reg in self.registers:
            plt.bar(range(self.registers[reg]["levels"]), self.registers[reg]["state"])
            plt.xlabel("Fock State |n⟩")
            plt.ylabel("Probability Amplitude")
            plt.title(f"State of {reg}")
            plt.show()
        else:
            print("Register not found.")
    
    def simulate_qiskit(self):
        """Executa um circuito simples no Qiskit para simulação."""
        print("Simulating a simple quantum circuit with Qiskit...")
        qc = QuantumCircuit(2)
        qc.h(0)  # Coloca o primeiro qubit em superposição
        qc.cx(0, 1)  # Aplica emaranhamento (CNOT)
        
        simulator = Aer.get_backend('statevector_simulator')
        result = execute(qc, simulator).result()
        statevector = result.get_statevector()
        
        print("Statevector:", statevector)


# Testando a nova linguagem
if __name__ == "__main__":
    bql = BQLInterpreter()
    commands = [
        "CREATE q1 4",
        "CREATE q2 4",
        "ENTANGLE q1 q2",
        "APPLY_NOISE q1 0.1",
        "DISTILL q1",
        "SHOW q1",
        "PLOT q1",
        "SIMULATE"
    ]
    
    for cmd in commands:
        bql.execute(cmd)
ef __init__(self):
     
