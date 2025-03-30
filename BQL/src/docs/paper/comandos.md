Comandos BQL

    CREATE <name> <levels>

        Descrição: Cria um registro quântico bosônico com um número específico de níveis.

        Exemplo: CREATE reg1 5 – Cria um registro chamado reg1 com 5 níveis.

    ENTANGLE <reg1> <reg2>

        Descrição: Entangle dois registros quânticos.

        Exemplo: ENTANGLE reg1 reg2 – Entangle os registros reg1 e reg2.

    APPLY_NOISE <reg> <strength>

        Descrição: Aplica ruído ao registro quântico.

        Exemplo: APPLY_NOISE reg1 0.1 – Aplica ruído com força 0.1 ao registro reg1.

    DISTILL <reg>

        Descrição: Realiza a destilação de entrelaçamento em um registro quântico.

        Exemplo: DISTILL reg1 – Realiza a distilação do entrelaçamento no registro reg1.

    SHOW <reg>

        Descrição: Exibe o estado atual de um registro quântico.

        Exemplo: SHOW reg1 – Exibe o estado do registro reg1, incluindo um gráfico de seus níveis e probabilidades.

    EXPORT

        Descrição: Exporta os dados dos registros quânticos para um arquivo JSON.

        Exemplo: EXPORT – Salva os dados de todos os registros em um arquivo .json.
