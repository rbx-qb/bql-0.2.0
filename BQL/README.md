# BQL: Bosonic Quantum Language

BQL (Bosonic Quantum Language) é uma linguagem de programação para manipulação e simulação de estados bosônicos em computação quântica. A linguagem permite criar registros bosônicos, emaranhá-los, aplicar ruídos e realizar destilação de emaranhamento, além de suportar integração com IBM Quantum.

## 📜 Sobre o Projeto

O objetivo da BQL é fornecer uma interface acessível para experimentação com sistemas bosônicos contínuos, expandindo as capacidades das linguagens convencionais como Qiskit. A abordagem proposta é baseada no artigo:

> *Hardware-Efficient Entanglement Distillation Using Bosonic Systems* (Jacoby, Arnon-Friedman, Rosenblum, 2025)

## 🔧 Funcionalidades

- Criar registros bosônicos com múltiplos níveis.
- Aplicar operações de emaranhamento entre registros.
- Simular a aplicação de ruído e analisar seus efeitos.
- Implementar técnicas de destilação para aumentar a fidelidade do emaranhamento.
- Visualizar estados quânticos com gráficos interativos.
- Executar simulações no IBM Quantum.

## 📂 Estrutura do Repositório
```
BQL-Project/
│── bql_interpreter.py   # Implementação principal da linguagem
│── tests/               # Scripts de testes
│── docs/                # Documentação e paper científico
│   ├── paper/           # Paper em LaTeX
│   ├── figures/         # Imagens usadas no paper
│── examples/            # Exemplos de código
│── README.md            # Este arquivo
```

## 🚀 Instalação e Uso

### Requisitos
- Python 3.8+
- Bibliotecas: `numpy`, `matplotlib`, `qiskit`

### Instalação
```bash
pip install numpy matplotlib qiskit
```

### Uso
```python
from bql_interpreter import BQLInterpreter

bql = BQLInterpreter()
bql.execute("CREATE q1 4")
bql.execute("ENTANGLE q1 q2")
bql.execute("APPLY_NOISE q1 0.1")
bql.execute("DISTILL q1")
bql.execute("SHOW q1")
```

## 🧪 Testes
Para rodar os testes automatizados:
```bash
python -m unittest discover tests/
```

## 🎯 Contribuição
Se deseja contribuir:
1. Faça um fork do repositório.
2. Crie uma branch (`git checkout -b feature-nova`).
3. Faça commit das suas mudanças (`git commit -m 'Nova feature'`).
4. Faça push para a branch (`git push origin feature-nova`).
5. Abra um Pull Request.

## 📜 Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
