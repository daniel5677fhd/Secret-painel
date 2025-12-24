import time
import getpass
import sys
import shutil

# =========================
# LIMPAR TELA
# =========================
def limpar_tela():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

# =========================
# CENTRALIZAR HORIZONTAL E VERTICAL
# =========================
def print_centralizado(texto):
    linhas_terminal = shutil.get_terminal_size().lines
    largura_terminal = shutil.get_terminal_size().columns
    linhas_texto = texto.splitlines()
    altura_texto = len(linhas_texto)
    topo = (linhas_terminal - altura_texto) // 2
    print("\n" * topo)
    for linha in linhas_texto:
        print(linha.center(largura_terminal))

# =========================
# FRAMES DA CAVEIRA
# =========================
caveira = [
r"""
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
███▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
""",
r"""
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
███▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐█████░░▄░░█████▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
"""
]

# =========================
# TÍTULO COM BOTÕES
# =========================
TITULO_COM_BOTOES = r"""
+------------------------------------------------+
| ███████╗ ███████╗ ██████╗ ██████╗ ███████╗  |
| ██╔════╝ ██╔════╝██╔════╝██╔═══██╗██╔════╝  |
| ███████╗ █████╗  ██║     ██║   ██║█████╗      |
| ╚════██║ ██╔══╝  ██║     ██║   ██║██╔══╝      |
| ███████║ ███████╗╚██████╗╚██████╔╝███████╗  |
| ╚══════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝   |
|                S E C R E T   L E G I O N            |
|                                                     |
| (1) Consulta de nome                                |
| (2) Consulta de telefone                            |
| (3) Consulta de IP                                  |
| (4) Consulta de DDD                                 |
| (5) Consulta de CPF                                 |
+------------------------------------------------+|
| Digite 0 para sair                              |
"""

# =========================
# RESPOSTAS DOS BOTÕES
# =========================
respostas = {
    "01": "[1;36mVocê escolheu o botão 1![0m",
    "02": "[1;36mVocê escolheu o botão 2![0m",
    "03": "[1;36mVocê escolheu o botão 3![0m",
    "04": "[1;36mVocê escolheu o botão 4![0m",
    "05": "[1;36mVocê escolheu o botão 5![0m",
    
}

# =========================
# MAIN
# =========================
def main():
    senha = getpass.getpass("Digite a senha: ")

    if senha == "adminSecret":
        # animação da caveira
        for _ in range(2):
            for frame in caveira:
                limpar_tela()
                print_centralizado(frame)
                time.sleep(0.4)

        # painel com título e botões
        limpar_tela()
        print_centralizado(TITULO_COM_BOTOES)

        # interação com o usuário
        while True:
            escolha = input("\nEscolha uma opção (1-5) ou 0 para sair: ").strip()
            
            if escolha == "0":
                break
            elif escolha in ["1", "2", "3", "4", "5"]:
                chave = escolha.zfill(2)  # transforma 1 -> 01
                print(f"\n{respostas[chave]}\n")
            else:
                print("\033[1;31mEscolha inválida! Digite 1 a 5 ou 0 para sair.\033[0m")
                time.sleep(1)

        limpar_tela()
    else:
        print("\033[1;31mSenha incorreta!\033[0m")
        time.sleep(2)
        limpar_tela()

if __name__ == "__main__":
    main()
