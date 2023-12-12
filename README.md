<div align="center">
<img  width="240"  src="https://i.imgur.com/6TcTQ9B.png">
</div>

<span>Versão: 23.12.1 <a style="color:#909" href="https://bill1300.github.io/linguax-docs/">Documentação ➜</a></span>

<span>Este obra está licenciado com uma <a style="color:#909" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
Licença Creative Commons Atribuição-NãoComercial-CompartilhaIgual 4.0 Internacional</a>.</span>


### Instalação ➜

Para instalar o programa execute o comando:

>$ bash instalador&#46;sh

(É necessário a inserir a senha de super-usuário)
v
### Execução ➜

#### Modo Simples

Para utilizar o programa execute o comando **linguax** seguido da palavra ou frase a ser traduzida, como no exemplo abaixo:

> $ **linguax** hello world

Saída ➜ olá mundo

<div align="center">
    <img width="600" src="https://i.imgur.com/UI0TOHh.png">
</div>

Para que isso seja executado de modo eficiente e correto defina os idiomas de entrada/saída .

#### Modo Comum

Para a tradução de modo comum, utilize o comando:
> $ **linguax**

Saída ➜ 
<div align="center">
    <img width="600" src="https://i.imgur.com/pRdNJb2.png">
</div>

Selecione **Traduzir uma palavra ou frase** (tecla `1` no menu), informar o idioma de entrada seguindo o código de cada idioma suportado pelo sistema ou deixar vazio para detecção automática, após isso informar o idioma de saída ou deixar vazio para selecionar o idioma salvo em perfil, e por fim descrever a palavra ou frase para ser traduzida.

<div align="center">
    <img width="600" src="https://i.imgur.com/tODDBuV.png">
    <br>
    <img width="600" src="https://i.imgur.com/HCYUnum.png">
    <br>
    <img width="600" src="https://i.imgur.com/UI0TOHh.png">  
</div>

## Traduzir arquivo ➜

Para realizar a tradução de um arquivo de texto, deve ser selecionado o item `2` no menu de opções. É necessário fornecer o endereço do arquivo desejado. Posteriormente, o conteúdo é traduzido e um novo arquivo é gerado no mesmo diretório, mantendo o mesmo nome, porém acrescentando "_linguax". A tradução é realizada para o idioma previamente definido no perfil do usuário.

## Configurar idiomas ➜

Para a configuração de idiomas, no menu deve ser selecionado o item `3`, **Configurar idiomas de entrada/saída.**

<div align="center">
    <img width="600" src="https://i.imgur.com/CDUzTSS.png">
</div>

➜ **Idioma de entrada.**

No início, será solicitado o idioma das palavras e frases a serem processadas, seguindo a formatação correta conforme indicado na tabela abaixo. Se esse campo for deixado vazio, o sistema realizará automaticamente a detecção do idioma de entrada.

➜ **Idioma de saída.**

A segunda questão refere-se ao idioma de saída das palavras e frases a serem processadas, devendo seguir a formatação correta conforme indicado na tabela abaixo. Se este campo for deixado vazio, o idioma de saída será o idioma previamente definido nas traduções anteriores. Caso seja a primeira tradução, o idioma de saída será o idioma atual do sistema operacional.

➜ **Idioma da interface.**

A terceira questão trata do idioma da interface do sistema, o qual deve seguir a formatação correta indicada na tabela abaixo. Se este campo for deixado vazio, o idioma da interface será configurado para o idioma atual do sistema operacional.

➜ **Lista de idiomas suportados:**

Peço desculpas pelo erro anterior. Os códigos fornecidos na lista são padrões ISO 639-1 e são amplamente usados em várias situações, incluindo a identificação de idiomas. No entanto, para o DeepL API, os códigos de idioma são específicos. Aqui estão os códigos de idioma corretos para o DeepL:

| Índice | Idioma                   | Código |
|--------|--------------------------|--------|
| 1      | Africâner                | af     |
| 2      | Albanês                  | sq     |
| 3      | Amárico                  | am     |
| 4      | Árabe                    | ar     |
| 5      | Armênio                  | hy     |
| 6      | Azerbaijano              | az     |
| 7      | Bengali                  | bn     |
| 8      | Bielorrusso              | be     |
| 9      | Bósnio                   | bs     |
| 10     | Búlgaro                  | bg     |
| 11     | Catalão                  | ca     |
| 12     | Checo                    | cs     |
| 13     | Chinês (Simplificado)    | zh     |
| 14     | Chinês (Tradicional)     | zh-TW  |
| 15     | Croata                   | hr     |
| 16     | Dinamarquês              | da     |
| 17     | Eslovaco                 | sk     |
| 18     | Esloveno                 | sl     |
| 19     | Espanhol                 | es     |
| 20     | Estoniano                | et     |
| 21     | Finlandês                | fi     |
| 22     | Francês                  | fr     |
| 23     | Georgiano                | ka     |
| 24     | Alemão                   | de     |
| 25     | Grego                    | el     |
| 26     | Hebraico                 | he     |
| 27     | Hindi                    | hi     |
| 28     | Holandês                 | nl     |
| 29     | Húngaro                  | hu     |
| 30     | Indonésio                | id     |
| 31     | Inglês                   | en     |
| 32     | Italiano                 | it     |
| 33     | Japonês                  | ja     |
| 34     | Letão                    | lv     |
| 35     | Lituano                  | lt     |
| 36     | Macedônio                | mk     |
| 37     | Malaio                   | ms     |
| 38     | Maltês                   | mt     |
| 39     | Nepalês                  | ne     |
| 40     | Norueguês                | no     |
| 41     | Persa                    | fa     |
| 42     | Polonês                  | pl     |
| 43     | Português                | pt     |
| 44     | Punjabi                  | pa     |
| 45     | Romeno                   | ro     |
| 46     | Russo                    | ru     |
| 47     | Sérvio                   | sr     |
| 48     | Sueco                    | sv     |
| 49     | Tailandês                | th     |
| 50     | Tâmil                    | ta     |
| 51     | Tcheco                   | cs     |
| 52     | Telugu                   | te     |
| 53     | Turco                    | tr     |
| 54     | Ucraniano                | uk     |
| 55     | Urdu                     | ur     |
| 56     | Vietnamita               | vi     |
| 57     | Galês                    | cy     |
| 58     | Xhosa                    | xh     |
| 59     | Iídiche                  | yi     |
| 60     | Ioruba                   | yo     |
| 61     | Zulu                     | zu     |

### Constultar histórico ➜

No histórico, pressionando a tecla `4` no menu de opções, é exibida uma tabela contendo todas as traduções realizadas com a aplicação, tanto no Modo Simples quanto no Modo Comum, apresentando as seguintes informações: Data/Hora, Texto de Entrada, Texto de Saída e Idioma de Saída. Um exemplo dessa tabela é mostrado abaixo:

| Data/Hora  |  Texto Entrada  |  Idioma Saída  |  Idioma Saída|
|---|---|---|---|
| 2023-12-01 15:30:00  | Hello, how are you?        | Hola, ¿cómo estás?      | es           |
| 2023-10-05 16:45:00  | Bonjour, comment ça va?    | Hello, how are you?     | en    

Nessa tabela fictícia, cada linha representa uma tradução realizada, exibindo a data e a hora da operação, o texto de entrada, o texto resultante e o idioma de saída correspondente.


A aplicação cria documentos de texto no diretório `~/.linguax/` do tipo JSON e XLSX mostrando essas informações.

### Desinstalar ➜

Para remover a aplicação Linguax selecione a opção Desinstalar na seção `5` no menu de opções. Assim será questionado a confirmação para a remoção:
    
  `1` - Sim, desinstalar (É necessário a inserir a senha de super-usuário).

  `2` - Não, voltar ao menu.

<div align="center">
    <img width="600" src="https://i.imgur.com/gcLl5Ra.png">
</div>

Ao selecionar a remoção os seguintes itens serão removidos:
- Script de inicialização da aplicação: `/bin/linguax`.
- Diretório `~/.linguax/*` contendo: Script de tradução, dados salvos de perfil e histórico de traduções.

### Ajuda ➜

Nessa seção é apresentado o Modo Simples e o Modo Comum para o usuário.

Os parâmetros disponíveis e a documentação:

- `-a` ou `--ajuda` ➜ Mostrar ajuda.
- `-t [endereço de arquivo]` ou `--texto [endereço de arquivo]` ➜ Traduzir arquivo.

### Informações ➜

Nas informações, seção de número `7`, são apresentadas a versão atual da aplicação Linguax, além do diretório online no GitHub e o link para página de documentação. Isso permite aos usuários obterem detalhes sobre a versão atualizada da aplicação e acessarem o repositório no GitHub para obterem mais informações, contribuírem ou acompanharem o desenvolvimento do projeto.

<div align="center">
    <img width="600" src="https://i.imgur.com/M022FAf.png">
</div>

### Feedback ➜

<span>Encontrou alguma dificuldade durante a execução? Tem alguma ideia para adicionar novas funcionalidades? <a style="color:#909" href="https://forms.gle/eTEJSRYThW8pNynJA">Escreva aqui ➜</a></span>

<hr>

### Estrutura de arquivos

```markdown
├── home/
│   └── .linguax/
│	    ├── executar.py
│	    ├── meta.dados
│	    ├── historico.xlsx
│	    └── historico.json
└── bin/
    └── linguax
```
