import sys, json, os, locale, requests
from deep_translator import GoogleTranslator
from datetime import datetime
from termcolor import colored

versao = "v.23.12.1"
arqMeta = os.path.expanduser("~/.linguax/meta.dados")
arqXLSX = os.path.expanduser("~/.linguax/historico.xlsx")
indice = {
   "Africâner": "af",
    "Albanês": "sq",
    "Amárico": "am",
    "Árabe": "ar",
    "Armênio": "hy",
    "Azerbaijano": "az",
    "Bengali": "bn",
    "Bielorrusso": "be",
    "Bósnio": "bs",
    "Búlgaro": "bg",
    "Catalão": "ca",
    "Checo": "cs",
    "Chinês (Simplificado)": "zh",
    "Chinês (Tradicional)": "zh-TW",
    "Croata": "hr",
    "Dinamarquês": "da",
    "Eslovaco": "sk",
    "Esloveno": "sl",
    "Espanhol": "es",
    "Estoniano": "et",
    "Finlandês": "fi",
    "Francês": "fr",
    "Georgiano": "ka",
    "Alemão": "de",
    "Grego": "el",
    "Hebraico": "he",
    "Hindi": "hi",
    "Holandês": "nl",
    "Húngaro": "hu",
    "Indonésio": "id",
    "Inglês": "en",
    "Italiano": "it",
    "Japonês": "ja",
    "Letão": "lv",
    "Lituano": "lt",
    "Macedônio": "mk",
    "Malaio": "ms",
    "Maltês": "mt",
    "Nepalês": "ne",
    "Norueguês": "no",
    "Persa": "fa",
    "Polonês": "pl",
    "Português": "pt",
    "Punjabi": "pa",
    "Romeno": "ro",
    "Russo": "ru",
    "Sérvio": "sr",
    "Sueco": "sv",
    "Tailandês": "th",
    "Tâmil": "ta",
    "Tcheco": "cs",
    "Telugu": "te",
    "Turco": "tr",
    "Ucraniano": "uk",
    "Urdu": "ur",
    "Vietnamita": "vi",
    "Galês": "cy",
    "Xhosa": "xh",
    "Iídiche": "yi",
    "Ioruba": "yo",
    "Zulu": "zu",
}

def funcaoTraduzirBasica(texto, i_entrada, i_saida):
    return GoogleTranslator(source=i_entrada, target=i_saida).translate(texto)

def traduzirCompleta(idioma_os):
    def verificarCodigo(codigo):
        return codigo in indice.values()

    _, saida_v = verificarIdioma()
    lista_frase = funcaoTraduzirBasica("Lista de idiomas em 'Ajuda'.", "pt", idioma_os)
    entrada_frase = funcaoTraduzirBasica(
        "Idioma de entrada  (vazio para detecção automática) ➜ ", "pt", idioma_os
    )
    saida_frase = funcaoTraduzirBasica(
        "Idioma de saída (vazio para idioma salvo em perfil [" + saida_v + "]) ➜ ",
        "pt",
        idioma_os,
    )
    traduzir_frase = funcaoTraduzirBasica("Palavra ou frase ➜ ", "pt", idioma_os)
    while True:
        try:
            os.system("clear")
            print(colored(lista_frase, "white", "on_magenta", attrs=["bold"]))
            entrada = input(
                (colored(" ➜ ", "black", "on_white", attrs=["bold"]) + entrada_frase)
            )
            if verificarCodigo(entrada):
                break
            if entrada == "":
                entrada = "auto"
                break
        except KeyboardInterrupt:
            pass
            configuracaoMenu()
    while True:
        try:
            os.system("clear")
            print(colored(lista_frase, "white", "on_magenta", attrs=["bold"]))
            saida = input(
                (colored(" ➜ ", "black", "on_white", attrs=["bold"]) + saida_frase)
            )
            if verificarCodigo(saida):
                break
            if saida == "":
                saida = saida_v
                break
        except KeyboardInterrupt:
            configuracaoMenu()
    while True:
        try:
            os.system("clear")
            print(colored(lista_frase, "white", "on_magenta", attrs=["bold"]))
            frase = input(
                (colored(" ➜ ", "black", "on_white", attrs=["bold"]) + traduzir_frase)
            )
            if frase != "":
                break
        except KeyboardInterrupt:
            configuracaoMenu()
    resp = funcaoTraduzirBasica(frase, entrada, saida)
    guardarDados(frase, resp, saida)
    print((colored(resp, attrs=["bold"])))

def traduzirArquivo(idioma_os):
    idiomaE, idiomaS = verificarIdioma()
    fraseEndereco = funcaoTraduzirBasica("Digite o endereço do arquivo ➜ ", "pt", idioma_os)
    enderecoArquivoEntrada = input(colored(fraseEndereco, "white", "on_magenta", attrs=["bold"]))

    if not os.path.isfile(enderecoArquivoEntrada):
        print("O arquivo não foi encontrado.")
    else:
        with open(enderecoArquivoEntrada, 'r') as arquivo:
            conteudoArquivo = arquivo.read()
        conteudoTraduzido = funcaoTraduzirBasica(conteudoArquivo, idiomaE, idiomaS)
        with open(enderecoArquivoEntrada+"_linguax", "w") as arquivo:
            arquivo.write(conteudoTraduzido)
        tagArquivo = f"[ARQUIVO={enderecoArquivoEntrada}]"
        guardarDados(tagArquivo+conteudoArquivo, idiomaE, idiomaS)

def configuracaoMenu():
    def menuIdiomas():
        idioma1_frase = funcaoTraduzirBasica(
            "Idioma de entrada (vazio para detecção automática): ", "pt", idioma_os
        )
        idioma2_frase = funcaoTraduzirBasica(
            "Idioma de saída: (vazio para idioma de perfil [" + idioma_os + "]) ",
            "pt",
            idioma_os,
        )
        idioma3_frase = funcaoTraduzirBasica(
            "Idioma de interface Linguax (vazio para idioma do sistema operacional): ",
            "pt",
            idioma_os,
        )
        salvando_frase = funcaoTraduzirBasica("Salvando...", "pt", idioma_os)
        os.system("clear")
        try:
            idioma_entrada = str(
                input(
                    (
                        colored(
                            idioma1_frase + "  ", "white", "on_magenta", attrs=["bold"]
                        )
                    )
                )
            )
            idioma_saida = str(
                input(
                    (
                        colored(
                            idioma2_frase + "  ", "white", "on_magenta", attrs=["bold"]
                        )
                    )
                )
            )
            idioma_linguax = str(
                input(
                    (
                        colored(
                            idioma3_frase + "  ", "white", "on_magenta", attrs=["bold"]
                        )
                    )
                )
            )
            print(
                colored(" " + salvando_frase + " ", "black", "on_white", attrs=["bold"])
            )
        except KeyboardInterrupt:
            configuracaoMenu()
        if idioma_entrada == "":
            idioma_entrada = "auto"
        if idioma_saida == "":
            idioma_saida = idioma_os
        if idioma_linguax == "":
            _, idioma_linguax = detectarIdioma()
        meta = open(arqMeta, "w")
        meta.write(idioma_entrada + "\n" + idioma_saida + "\n" + idioma_linguax)
        meta.close()
        configuracaoMenu()

    def menuHistorico():
        col1 = funcaoTraduzirBasica("Data/Hora", "pt", idioma_os)
        col2 = funcaoTraduzirBasica("Texto Entrada", "pt", idioma_os)
        col3 = funcaoTraduzirBasica("Idioma Saída", "pt", idioma_os)
        col4 = funcaoTraduzirBasica("Idioma Saída", "pt", idioma_os)
        print(
            colored(
                col1 + "  |  " + col2 + "  |  " + col3 + "  |  " + col4,
                "black",
                "on_white",
            )
        )
        with open(arqXLSX, "r") as arquivo:
            contador_linha = 0
            for linha in arquivo:
                if contador_linha > 0:
                    linha_completa = linha.strip()
                    linha_completa = linha_completa.replace(";", "  |  ")
                    print(linha_completa)
                contador_linha += 1

    def menuDesinstalar(numero_frase):
        def desinstalar():
            pasta_linguax = os.path.expanduser("~/.linguax/")
            lancador_linguax = os.path.expanduser("/bin/linguax")
            os.system("clear")
            os.system("sudo rm " + lancador_linguax)
            os.system("rm -r " + pasta_linguax)
            print(colored(tchau_frase, "black", "on_white"))

        entrada = 0
        desinstalar_frase = funcaoTraduzirBasica(
            "Você realmente deseja desinstalar?", "pt", idioma_os
        )
        sim_frase = funcaoTraduzirBasica("Sim.", "pt", idioma_os)
        nao_frase = funcaoTraduzirBasica("Não.", "pt", idioma_os)
        tchau_frase = funcaoTraduzirBasica("Tchau.", "pt", idioma_os)

        while entrada < 1 or entrada > 2:
            os.system("clear")
            print(colored(desinstalar_frase, "white", "on_magenta", attrs=["bold"]))
            print(colored(" 1. " + sim_frase, "black", "on_white"))
            print(colored(" 2. " + nao_frase, "black", "on_white"))
            entrada = int(
                input(
                    colored(numero_frase + "  ", "white", "on_magenta", attrs=["bold"])
                )
            )
            if entrada == 1:
                desinstalar()
            else:
                configuracaoMenu()

    def menuAjuda():
        idioma_nome = funcaoTraduzirBasica("Idioma", "pt", idioma_os)
        idioma_codigo = funcaoTraduzirBasica("Código", "pt", idioma_os)
        func_frase = funcaoTraduzirBasica("Função Simples: ", "pt", idioma_os)
        funcA_frase = funcaoTraduzirBasica(
            "Defina os idiomas de entrada e saída em: Menu > Configurar idiomas de entrada/saída (2).",
            "pt",
            idioma_os,
        )
        funcB_frase = funcaoTraduzirBasica(
            "Com isso configurado você pode utilizar a função de tradução rápida, como no exemplo abaixo:",
            "pt",
            idioma_os,
        )
        funcC_frase = funcaoTraduzirBasica(
            "Documentação:",
            "pt",
            idioma_os,
        )

        list_frase = funcaoTraduzirBasica("Lista de idiomas: ", "pt", idioma_os)
        os.system("clear")
        print(colored(func_frase, "black", "on_white"))

        print(
            funcA_frase
            + "\n"
            + funcB_frase
            + "\n\n"
            + colored("$ liguax ", "white", attrs=["bold"])
            + "Olá Mundo\n  Hello World\n"
        )
        print(
            "%s ➜ %s\n"
            % (funcC_frase, "https://github.com/Bill1300/Linguax/blob/main/README.md")
        )
        print(
            colored(list_frase, "black", "on_white")
            + "\n\n"
            + idioma_nome
            + "   "
            + idioma_codigo
        )

        for idioma, codigo in indice.items():
            print("")  # Separador entre informações
            print(
                colored(" " + idioma + " ", "black", "on_white", attrs=["bold"])
                + (colored(" " + codigo + "  ", "white", "on_magenta", attrs=["bold"]))
            )

    def menuInformacoes():
        dev_frase = funcaoTraduzirBasica("Desenvolvido por", "pt", idioma_os)
        dir_frase = funcaoTraduzirBasica("Diretório", "pt", idioma_os)
        doc_frase = funcaoTraduzirBasica("Documentação", "pt", idioma_os)
        os.system("clear")
        print(
            colored(" Linguax ", "white", "on_magenta", attrs=["bold"])
            + colored("(2023) " + versao + " ", "black", "on_white"),
            "\n" + dev_frase + " ➜ ",
            "Gabriel Ângelo Cerutti",
        )
        print("%s ➜ %s" % (dir_frase, "https://github.com/Bill1300/Linguax"))
        print("%s ➜ %s" % (doc_frase, "https://bill1300.github.io/linguax-docs/"))
    entrada = 0
    idioma_os = idiomaInterface()
    traduzir_frase = funcaoTraduzirBasica(
        "Traduzir uma palavra ou frase.", "pt", idioma_os
    )
    idiomas_frase = funcaoTraduzirBasica(
        "Configurar idiomas de entrada/saída.", "pt", idioma_os
    )
    arquivoFuncao = funcaoTraduzirBasica("Traduzir arquivo.", "pt", idioma_os)
    historico_frase = funcaoTraduzirBasica("Consultar histórico.", "pt", idioma_os)
    desinstalar_frase = funcaoTraduzirBasica("Desinstalar.", "pt", idioma_os)
    informacoes_frase = funcaoTraduzirBasica("Informações.", "pt", idioma_os)
    ajuda_frase = funcaoTraduzirBasica("Ajuda.", "pt", idioma_os)
    numero_frase = funcaoTraduzirBasica("Digite o número do menu ➜ ", "pt", idioma_os)
    v_max = 7
    while entrada < 1 or entrada > v_max:
        os.system("clear")
        print(colored(" Linguax ", "white", "on_magenta", attrs=["bold"]))
        print(colored("1 ➜ ", "black", "on_white", attrs=["bold"]), traduzir_frase)
        print(colored("2 ➜ ", "black", "on_white", attrs=["bold"]), arquivoFuncao)
        print(colored("3 ➜ ", "black", "on_white", attrs=["bold"]), idiomas_frase)
        print(colored("4 ➜ ", "black", "on_white", attrs=["bold"]), historico_frase)
        print(colored("5 ➜ ", "black", "on_white", attrs=["bold"]), desinstalar_frase)
        print(colored("6 ➜ ", "black", "on_white", attrs=["bold"]), ajuda_frase)
        print(colored("7 ➜ ", "black", "on_white", attrs=["bold"]), informacoes_frase)
        try:
            entrada = int(
                input(
                    colored(numero_frase + "  ", "white", "on_magenta", attrs=["bold"])
                )
            )
        except KeyboardInterrupt:
            os.system("clear")
            sys.exit()

        if entrada == 1:
            traduzirCompleta(idioma_os)
        if entrada == 2:
            traduzirArquivo(idioma_os)
        if entrada == 3:
            menuIdiomas()
        if entrada == 4:
            menuHistorico()
        if entrada == 5:
            menuDesinstalar(numero_frase)
        if entrada == 6:
            menuAjuda()
        if entrada == 7:
            menuInformacoes()

def detectarIdioma():
    idioma_os, _ = locale.getdefaultlocale()
    arg_saida = idioma_os[:2]
    return idioma_os, arg_saida

def idiomaInterface():
    with open(arqMeta, "r") as arquivo:
        linhas = arquivo.readlines()
        if len(linhas) >= 3:
            interface = linhas[2].strip()
            if interface == "auto":
                interface, _ = verificarIdioma()
                linhas[2] = interface  # Atualiza a terceira linha
                with open(arqMeta, "w") as arquivo:
                    arquivo.writelines(linhas)
            return interface

def separarPalavras():
    entrada = " ".join(
        argumento
        for argumento in sys.argv[1:]
        if isinstance(argumento, str) and argumento.strip()
    )
    return entrada

def guardarDados(frase, saida, idioma):
    caminhoArqJSON = os.path.expanduser("~/.linguax/historico.json")
    caminhoArqXLSX = os.path.expanduser("~/.linguax/historico.xlsx")
    data_hora = datetime.now().isoformat()

    # JSON
    dados = {
        "data_hora": data_hora,
        "texto_entrada": frase,
        "texto_saida": saida,
        "idioma_saida": idioma,
    }
    dados_json = json.dumps(dados, indent=4)
    arq = open(caminhoArqJSON, "a")
    arq.write(dados_json + "\n")
    arq.close()

    # XLSX
    dados = data_hora + ";" + frase + ";" + saida + ";" + idioma
    arq = open(caminhoArqXLSX, "a")
    arq.write(dados + "\n")
    arq.close()

def verificarIdioma():
    with open(arqMeta, "r") as arquivo:
        v_entrada = arquivo.readline().strip()

    with open(arqMeta, "r") as arquivo:
        linhas = arquivo.readlines()
        if len(linhas) >= 2:
            v_saida = linhas[1].strip()

    return v_entrada, v_saida

def metaVazio():
    if os.stat(arqMeta).st_size == 0:
        _, idioma_os = detectarIdioma()
        meta = open(arqMeta, "w")
        meta.write("auto" + "\n" + idioma_os + "\n" + idioma_os)
        meta.close()

def verificaConexao():
    url = "https://www.github.com"
    timeout = 5
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        return True
    except (requests.ConnectionError, requests.Timeout, requests.RequestException):
        return False

if verificaConexao():
    frase = separarPalavras()
    metaVazio()
    if frase == "":
        configuracaoMenu()
    else:
        v_entrada, v_saida = verificarIdioma()
        saida = funcaoTraduzirBasica(frase, v_entrada, v_saida)
        guardarDados(frase, saida, v_saida)
        print((colored(saida, attrs=["bold"])))
else:
    print((colored(" Erro de conexão / Conection Error ", "black", "on_white", attrs=["bold"])))
    print("  \U0001F30E ➜ \u274C ➜ \U0001F5A5  ")