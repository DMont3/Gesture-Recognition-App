# cognitiveComputingCP2_3
# Controle de Reprodução de Vídeo e Música com Gestos

## Descrição do Projeto

Este projeto tem como objetivo desenvolver uma aplicação de Visão Computacional avançada que permite aos usuários controlar a reprodução de vídeo e música utilizando gestos manuais. Através do uso da câmera do dispositivo, é possível pausar, despausar e realizar outras funções de controle de mídia sem a necessidade de interagir diretamente com dispositivos físicos como teclado e mouse. Essa tecnologia oferece uma camada adicional de acessibilidade e conveniência, tornando-a particularmente valiosa para pessoas com dificuldades visuais, de mobilidade, ou qualquer pessoa que busque uma forma mais intuitiva e livre para interagir com seus dispositivos.

### Funcionalidades Principais

- **Pausar:** Ao realizar um gesto pré-definido, o usuário pode pausar a reprodução de vídeos ou músicas.
- **Despausar:** Um gesto diferente permite que a reprodução seja retomada.
- **Ajuste de Volume:** Gestos específicos podem aumentar ou diminuir o volume da reprodução.
- **Mudança de Faixa:** Deslizar a mão para a esquerda ou direita pode mudar para a faixa anterior ou seguinte, respectivamente.


(Nota: Este projeto está em desenvolvimento contínuo, e novas funcionalidades serão adicionadas à medida que avançarmos.)

## Tecnologias Utilizadas

- **OpenCV:** Para captura de imagem e reconhecimento de gestos.
- **PyAutoGUI:** Para automação de tarefas de controle de mouse e teclado.

## Instruções de Instalação

Siga os passos abaixo para instalar e utilizar esta aplicação:

1. **Verificação de Instalação do Python:** Certifique-se de que o Python está instalado em sua máquina. Se necessário, visite [python.org](https://python.org) para baixar e instalar a versão mais recente.

2. **Instalação das Dependências:** O funcionamento do projeto depende de diversas bibliotecas. Utilize o gerenciador de pacotes pip para instalar o OpenCV e outras bibliotecas necessárias:

    ```bash
    pip install opencv-python
    ```

    As dependências específicas podem variar conforme o projeto evolui. Para uma lista completa, consulte o arquivo `requirements.txt`.

## Configuração do Ambiente

Antes de executar a aplicação, é necessário configurar o ambiente de desenvolvimento:

1. **Clone o Repositório:** Clone o repositório do projeto para sua máquina local.
2. **Ambiente Virtual:** Recomenda-se a criação de um ambiente virtual Python para o projeto. Isso pode ser feito com o seguinte comando:

    ```bash
    python -m venv venv
    ```

    Ative o ambiente virtual com:

    - No Windows: `venv\Scripts\activate`
    - No Linux ou macOS: `source venv/bin/activate`

3. **Instale as Dependências:** Com o ambiente virtual ativado, instale todas as dependências necessárias conforme mencionado acima.

## Uso

Para iniciar a aplicação, execute o script principal com o comando abaixo, certificando-se de que está no diretório do projeto:

```bash
python nome_do_script.py PRECISA ALTERAR NOME
```

### Interagindo com a Aplicação

1. **Inicie a Aplicação:** Execute o script conforme instruído.
2. **Realize os Gestos:** Faça os gestos pré-definidos em frente à câmera para controlar a reprodução de sua mídia.
3. **Ajuste Conforme Necessário:** Baseado no feedback visual, ajuste seus gestos para otimizar o reconhecimento pela aplicação.

## Contribuições

Contribuições são bem-vindas! Se você tem ideias ou melhorias, sinta-se à vontade para forkar o repositório e submeter um pull request.

# Rubrica de Avaliação para o Projeto de Controle de Reprodução de Vídeo e Música com Gestos

## Objetivo Geral
Avaliar a implementação e eficácia de uma aplicação de Visão Computacional que permite aos usuários controlar a reprodução de vídeo e música utilizando gestos manuais.

## Critérios de Avaliação

### Funcionalidade (90 pontos)
- **Implementação dos Gestos Básicos (40 pontos):** O sistema deve ser capaz de identificar e responder corretamente aos gestos básicos de pausar e despausar a reprodução.
- **Funcionalidades Adicionais (20 pontos):** A aplicação deve incluir funcionalidades extras como mudança de faixa, e feedback visual.
- **Implementação de movimentos não triviais (10 pontos):** A aplicação deve incluir movimentações circulares do dedos com o propósito de ajuste de volume.
- **Precisão no Reconhecimento de Gestos (20 pontos):** A precisão com que o sistema reconhece os gestos manuais dos usuários.

10

## Pontuação Total
- **Excelente (90-100 pontos):** Atende ou excede todas as expectativas em todos os critérios.
- **Bom (70-89 pontos):** Atende às expectativas na maioria dos critérios e excede em alguns.
- **Satisfatório (50-69 pontos):** Atende às expectativas mínimas na maioria dos critérios.
- **Insuficiente (0-49 pontos):** Não atende às expectativas mínimas em vários critérios.


pausar(k) = Mão Aberta
desativa/ativa som = Indicador Para Cima
Aumentar velocidade(>) = Hang Loose
Diminuir velocidade(<) = V de Vitória
avançar(j) = Apontar Esquerda
avançar(l) = Apontar Direita
aumenta volume(seta pra cima) = Rock
diminui volume(seta pra baixo) = Legal