## **Descrição**

**Este projeto implementa um agente aspirador de pó em Python, utilizando os seguintes recursos:**

- Simulação de ambiente: Um ambiente 2D com células sujas e limpas é criado para simular o cenário de limpeza.
- Agente de Aspiração: Um agente inteligente é implementado para navegar no ambiente e limpar as células sujas.
  - Estratégias de Limpeza:
    - Limpeza Simples: O agente se move para a célula suja mais próxima.
    - Limpeza Inteligente: O agente prioriza a limpeza da célula atual se estiver suja, caso contrário, se move para a célula suja mais próxima.
  - Visualização: Uma interface gráfica com Pygame é utilizada para visualizar o ambiente e o movimento do agente.

### **Instalação**

- Clone este repositório: git clone https://github.com/josesantosdev/vacuum-cleaner-agent.git
  Instale as dependências: pip install -r requirements.txt



### **Execução**

- Execute o script principal: python vacuum-cleaner-agent
  Observe a interface gráfica e acompanhe o agente limpando o ambiente.
- Opções:
  - Tamanho do ambiente: O tamanho do ambiente (número de linhas e colunas) pode ser configurado no script main.py.
  - Estratégias de limpeza: Você pode escolher entre a limpeza simples ou inteligente no script main.py.
  - Visualização: A velocidade da simulação e o tamanho das células podem ser ajustados na interface gráfica.
    Melhorias Futuras
  - Implementar diferentes algoritmos de navegação para otimizar o movimento do agente.
    Adicionar sensores e obstáculos para aumentar a complexidade do ambiente.
  - Implementar aprendizado de máquina para que o agente aprenda a limpar o ambiente de forma autônoma.
    Considerações
  - Este projeto serve como um ponto de partida para explorar diferentes aspectos da inteligência artificial e da robótica. O código pode ser facilmente adaptado para diferentes cenários e objetivos.

Licença
Este projeto está licenciado sob a licença MIT.
