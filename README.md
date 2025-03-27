# Controle de Reprodução de Vídeo e Música com Gestos

## Descrição do Projeto

Este projeto tem como objetivo desenvolver uma aplicação de Visão Computacional avançada que permite aos usuários controlar a reprodução de vídeo e música utilizando gestos manuais. Através do uso da câmera do dispositivo, é possível pausar, despausar e realizar outras funções de controle de mídia sem a necessidade de interagir diretamente com dispositivos físicos como teclado e mouse. Essa tecnologia oferece uma camada adicional de acessibilidade e conveniência, tornando-a particularmente valiosa para pessoas com dificuldades visuais, de mobilidade, ou qualquer pessoa que busque uma forma mais intuitiva e livre para interagir com seus dispositivos.

### Funcionalidades Principais

- **Pausar e Despausar:** Ao mostrar a palma da mão aberta, o usuário pode pausar a reprodução de vídeos ou músicas.
- **Ajuste de Volume:**
    - O gesto de "rock", realizado com a mão, é responsável por aumentar o volume da reprodução.
    - O gesto de "3" (indicador, médio e anelar levantados), realizado com a mão, é responsável por diminuir o volume da reprodução.
    - Ao mostrar o dedo indicador voltado para cima, o som da reprodução é ativado/desativado.
- **Velocidade da reprodução:**
    - O gesto de "Hang Loose", realizado com a mão, é responsável por acelerar a velocidade da reprodução.
    - O gesto de "V", realizado com a mão, é responsável por desacelerar a velocidade da reprodução.
- **Mudança de faixa:**
    - Ao mostrar o dedo indicador voltado para a direita, a reprodução é avançada, mudando para a próxima reprodução.
    - Ao mostrar o dedo indicador voltado para a esquerda, a reprodução é recuada, mudando para a reprodução anterior.

(Nota: Este projeto está em desenvolvimento contínuo, e novas funcionalidades serão adicionadas à medida que avançarmos.)

## Tecnologias Utilizadas

- **OpenCV:** Para captura de imagem e reconhecimento de gestos.
- **PyAutoGUI:** Para automação de tarefas de controle de mouse e teclado.
- **MediaPipe:** Para reconhecimento de gestos e outras tarefas de processamento de vídeo e imagem.
  
## Instruções de Instalação

Siga os passos abaixo para instalar e utilizar esta aplicação:

1. **Verificação de Instalação do Python:** Certifique-se de que o Python está instalado em sua máquina. Se necessário, visite [python.org](https://python.org) para baixar e instalar a versão mais recente.

2. **Instalação das Dependências:** O funcionamento do projeto depende de diversas bibliotecas. Utilize o gerenciador de pacotes pip para instalar o OpenCV e outras bibliotecas necessárias:

    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

## Configuração do Ambiente

Antes de executar a aplicação, é necessário configurar o ambiente de desenvolvimento:

1. **Clone o Repositório:** Clone o repositório do projeto para sua máquina local.
2. **Ambiente Virtual:** Recomenda-se a criação de um ambiente virtual Python para o projeto. Isso pode ser feito com o seguinte comando:

    ```bash
    python -m venv venv
    ```

    Ative o ambiente virtual com:

    - No Windows: `venv\Scriptsctivate`
    - No Linux ou macOS: `source venv/bin/activate`

3. **Instale as Dependências:** Com o ambiente virtual ativado, instale todas as dependências necessárias conforme mencionado acima.

## Uso

Para iniciar a aplicação, execute o script principal com o comando abaixo, certificando-se de que está no diretório do projeto:

```bash
python detection_gesture_app.py
```

### Interagindo com a Aplicação

1. **Inicie a Aplicação:** Execute o script conforme instruído.
2. **Realize os Gestos:** Faça os gestos pré-definidos em frente à câmera para controlar a reprodução de sua mídia.
3. **Ajuste Conforme Necessário:** Baseado no feedback visual, ajuste seus gestos para otimizar o reconhecimento pela aplicação.

## Objetivo Geral
Avaliar a implementação e eficácia de uma aplicação de Visão Computacional que permite aos usuários controlar a reprodução de vídeo e música utilizando gestos manuais.
