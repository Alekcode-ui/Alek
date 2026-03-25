# -*- coding: utf-8 -*-
import os
import sys
import time
import socket
import subprocess

# ══════════════════════════════════════════
#  FECHAR COM O X DO CMD (Windows)
# ══════════════════════════════════════════
if os.name == "nt":
    import ctypes
    import ctypes.wintypes
    CTRL_CLOSE_EVENT = 2
    @ctypes.WINFUNCTYPE(ctypes.wintypes.BOOL, ctypes.wintypes.DWORD)
    def _handler(event):
        if event == CTRL_CLOSE_EVENT:
            os.system("cls")
            sys.exit(0)
        return False
    ctypes.windll.kernel32.SetConsoleCtrlHandler(_handler, True)

R      = "\033[0m"
AMBER  = "\033[38;2;200;150;35m"
AMBL   = "\033[38;2;255;210;80m"
SEPIA  = "\033[38;2;160;110;50m"
CREAM  = "\033[38;2;215;195;150m"
GRAY   = "\033[38;2;100;90;75m"
DRED   = "\033[38;2;150;35;35m"
GREEN  = "\033[38;2;80;180;80m"
BOLD   = "\033[1m"

# ══════════════════════════════════════════
#  PIXEL ART  —  ALEK
# ══════════════════════════════════════════
ON  = AMBL + "██" + R
OFF = "  "

LETRAS = {
    "A": [[0,1,1,1,0],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]],
    "L": [[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,1,1,1]],
    "E": [[1,1,1,1,1],[1,0,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,1,1,1]],
    "K": [[1,0,0,1,0],[1,0,1,0,0],[1,1,0,0,0],[1,0,1,0,0],[1,0,0,1,0]],
}

def exibir_banner():
    BI = 50
    print(f"\n  {AMBER}╔{'═'*BI}╗{R}")
    print(f"  {AMBER}║{'':^{BI}}║{R}")
    for row in range(5):
        linha = ""
        for i, letra in enumerate(["A","L","E","K"]):
            for bit in LETRAS[letra][row]:
                linha += ON if bit else OFF
            if i < 3:
                linha += "  "
        print(f"  {AMBER}║{R}  {linha}  {AMBER}║{R}")
    print(f"  {AMBER}║{'':^{BI}}║{R}")
    print(f"  {AMBER}╚{'═'*BI}╝{R}\n")


# ══════════════════════════════════════════
#  HEISENBERG
# ══════════════════════════════════════════
def exibir_heisenberg():
    G = GRAY
    A = AMBER
    S = SEPIA
    arte = [
        "                          -+****##%@@*                      ",
        "                @@@@*+++**##***#*##%%@#%@@@@@@*             ",
        "              :=@@@@***###*-.......==+%%%@@@@@@@@           ",
        "             :+*@@@@.:::::..............:::-+@@@@           ",
        "             =+:.......................::::-+@@@@           ",
        "             ++.........................:::-+@@@@           ",
        "             ++........................::::-=@@@@@          ",
        "             ++........................::::-+%@@@@@         ",
        "             +*::::::::::::::.:::.....:::::-*#@@@@@@%       ",
        "   :=++++++++*+::::::::::::::::.:.....::.::-+*@@@@@@@@@@@@@ ",
        "   =+====++++=-:::.....................:::-:=++@@@%@@@@@@@@ ",
        "   =#*+.......::::....................::::::-=:+@:+.=*@@*@@ ",
        "   :@+#---::...::-:::::...............::::::-=-+@-%%@@@@@@@ ",
        "    *@%#++++---...:.....:::..........:::::=*@@@=#@-@@@@@@@  ",
        "       =##**%%@@#@@@@@@@@@%#*++*%%#**+====*@@@@@*@@@@       ",
        "            @@*##@%@@@%#*+==-*%%%%*==+++++*@@+@@#@@@        ",
        "            =@@:-+.==#%@@#=:+*=-.**==--:---@@@*@+@@         ",
        "             @@++===-=*#*#%#**+=+*=-#-=-:-:-#@+@@@@         ",
        "             +@@+--=*#%@@@@+:*+*%*.:*#-..:::%@*@@@          ",
        "              @@#-++=+*=:.-:-+.+@#::-+**-:::@@%@@@          ",
        "              +@@@@+-:+-=-.::::=@#.:------==@@@@@           ",
        "               +@@@=:+#+=-.::::+@#:.:-:::-.%@%@@@           ",
        "                 @@+=--=+=--=*-%#*-.:---:=-@@@@@            ",
        "                -@@%=-==**#@@@@@#+:.::-==+@@@@@             ",
        "              -+##%@#-=%@%#++*%#-::.:.:::.@%@@@@+           ",
        "            :+##=:=@@=+%+:#@@@@#*++:...-*#%@@#@@@@*         ",
        "          :=**+:.-*+**+*:+*====..:=-..:*@@%*+---@@@@@       ",
        "       :=+**=:...=##*.*+-*@@@@@##*=-:::@@@@=------@@@@@@@   ",
        "   :=+++*+=:.....+%#*@#=::+++-:-:.:::.=@%@@---:::-#*%@@@@@* ",
        "  :=++++=:........+@%*+@@-:-:...::::...+%@@:.:::::::--=@@%@@ ",
        "  =+=:............-@%+@=@@--+-.:--::=+:=**-...::::::::---=@@ ",
        "  ++...............@@.%@#@%-*+::-:=*%#*::.....::::::::::--@@ ",
        "  ++...............*@=:@@@@+@@#=+=+=+#@:...........:::::-:@@ ",
        "  ++...............:@@:--@*%@#=+%@@@+@@-:.............::-:@@ ",
        "  ++................=@@+@@%*@-*@@@@%#@@-:::...........::-:@@ ",
        "  ++.................%@@=@@@@@@%#*=#%@@#=-:...........::::@@ ",
        "  ++.................-@@@@+#@@%==--#@@@@--::..........:.::%% ",
        "  =+............. ...:=#%*+%@@@*%@@@%@@*...::.........:...%% ",
        "  ==.......................-*@@@@@**@@@....::.......:.....## ",
        "  -+============+++++++**+++#@@@@@@@@@%++++*###############* ",
        "  :-==========+++++++***+++*%@@@@@@@@@++++*###############*- ",
    ]
    for l in arte:
        print(f"{A}{l}{G}")
    print(f"{G}")


# ══════════════════════════════════════════
#  UTILITÁRIOS
# ══════════════════════════════════════════
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def digitar(texto, delay=0.028):
    for ch in texto:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sep():
    print(f"  {AMBER}{'─'*54}{R}")

def pausar():
    input(f"\n  {GRAY}[ pressione ENTER para voltar... ]{R}")


# ══════════════════════════════════════════
#  ABERTURA
# ══════════════════════════════════════════
def tela_abertura():
    limpar()
    exibir_banner()
    sep()
    print()
    exibir_heisenberg()
    sep()
    digitar(f"  {SEPIA}\"Eu não estou em perigo. EU sou o perigo.\"{R}", delay=0.032)
    sep()
    print()
    input(f"  {AMBL}[ pressione ENTER para entrar... ]{R}")


# ══════════════════════════════════════════
#  MENU PRINCIPAL
# ══════════════════════════════════════════
def menu_principal():
    while True:
        limpar()
        exibir_banner()

        w = 49
        print(f"  {AMBER}╔{'═'*w}╗{R}")
        print(f"  {AMBER}║{CREAM}{'  MENU PRINCIPAL — ALEK v1.0':^{w}}{AMBER}║{R}")
        print(f"  {AMBER}╠{'═'*w}╣{R}")
        print(f"  {AMBER}║  {AMBL}1{AMBER}  →  {CREAM}Testar conexão / ping        {AMBER}║{R}")
        print(f"  {AMBER}║  {AMBL}2{AMBER}  →  {CREAM}Informações do sistema       {AMBER}║{R}")
        print(f"  {AMBER}║  {AMBL}3{AMBER}  →  {CREAM}Rede                         {AMBER}║{R}")
        print(f"  {AMBER}║  {AMBL}4{AMBER}  →  {CREAM}Sobre o programa             {AMBER}║{R}")
        print(f"  {AMBER}║  {DRED}0{AMBER}  →  {CREAM}Sair                         {AMBER}║{R}")
        print(f"  {AMBER}╚{'═'*w}╝{R}")
        sep()

        op = input(f"  {AMBL}Escolha: {R}").strip()
        if   op == "1": opcao_ping()
        elif op == "2": opcao_sistema()
        elif op == "3": menu_rede()
        elif op == "4": opcao_sobre()
        elif op == "0": sair()
        elif op.upper() == "WW": segredo_ww()
        else:
            print(f"\n  {DRED}\u26a0  Opcao invalida.{R}")
            time.sleep(1.1)
       
# ══════════════════════════════════════════
#  SUBMENU REDE / HACKING
# ══════════════════════════════════════════
def menu_rede():
    while True:
        limpar()
        exibir_banner()

        w = 49
        print(f"  {AMBER}╔{'═'*w}╗{R}")
        print(f"  {AMBER}║{CREAM}{'  REDE / HACKING':^{w}}{AMBER}║{R}")
        print(f"  {AMBER}╠{'═'*w}╣{R}")
        print(f"  {AMBER}║  {AMBL}1{AMBER}  →  {CREAM}Ver IP local e externo                 {AMBER}║{R}")
        print(f"  {AMBER}║  {AMBL}2{AMBER}  →  {CREAM}Scanner de portas                      {AMBER}║{R}")
        print(f"  {AMBER}║  {AMBL}3{AMBER}  →  {CREAM}Dispositivos na rede (Wi-Fi)           {AMBER}║{R}")
        print(f"  {AMBER}║  {AMBL}4{AMBER}  →  {CREAM}Traceroute                             {AMBER}║{R}")
        print(f"  {AMBER}║  {DRED}0{AMBER}  →  {CREAM}Voltar                                 {AMBER}║{R}")
        print(f"  {AMBER}╚{'═'*w}╝{R}")
        sep()

        op = input(f"  {AMBL}Escolha: {R}").strip()
        if   op == "1": rede_ip()
        elif op == "2": rede_scanner()
        elif op == "3": rede_dispositivos()
        elif op == "4": rede_traceroute()
        elif op == "0": break
        else:
            print(f"\n  {DRED}⚠  Opção inválida.{R}")
            time.sleep(1.1)


# ──────────────────────────────────────────
#  1. VER IP LOCAL E EXTERNO
# ──────────────────────────────────────────
def rede_ip():
    limpar(); exibir_banner(); sep()
    print(f"  {BOLD}{AMBER}VER IP LOCAL E EXTERNO{R}\n")

    # IP local
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
        s.close()
    except Exception:
        ip_local = "Não foi possível obter"

    # Hostname
    hostname = socket.gethostname()

    # IP externo via curl/powershell
    try:
        if os.name == "nt":
            resultado = subprocess.check_output(
                ["powershell", "-Command", "(Invoke-WebRequest -Uri 'https://api.ipify.org').Content"],
                timeout=5, stderr=subprocess.DEVNULL
            ).decode().strip()
        else:
            resultado = subprocess.check_output(
                ["curl", "-s", "https://api.ipify.org"],
                timeout=5
            ).decode().strip()
        ip_externo = resultado
    except Exception:
        ip_externo = "Sem conexão ou timeout"

    print(f"  {SEPIA}{'Hostname':<18}{R}{CREAM}{hostname}{R}")
    print(f"  {SEPIA}{'IP Local':<18}{R}{GREEN}{ip_local}{R}")
    print(f"  {SEPIA}{'IP Externo':<18}{R}{GREEN}{ip_externo}{R}")
    pausar()


# ──────────────────────────────────────────
#  2. SCANNER DE PORTAS
# ──────────────────────────────────────────
def rede_scanner():
    limpar(); exibir_banner(); sep()
    print(f"  {BOLD}{AMBER}SCANNER DE PORTAS{R}\n")

    host = input(f"  {CREAM}Host alvo (ex: 192.168.1.1): {R}").strip()
    if not host:
        print(f"  {DRED}Host inválido.{R}")
        pausar(); return

    try:
        inicio = int(input(f"  {CREAM}Porta inicial (ex: 1): {R}").strip() or "1")
        fim    = int(input(f"  {CREAM}Porta final   (ex: 1024): {R}").strip() or "1024")
    except ValueError:
        print(f"  {DRED}Porta inválida.{R}")
        pausar(); return

    print(f"\n  {GRAY}Escaneando {AMBER}{host}{GRAY} portas {inicio}─{fim}...{R}\n")
    sep()

    abertas = []
    for porta in range(inicio, fim + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        resultado = s.connect_ex((host, porta))
        if resultado == 0:
            abertas.append(porta)
            print(f"  {GREEN}[ABERTA]{R}  porta {AMBL}{porta}{R}")
        s.close()

    sep()
    if abertas:
        print(f"\n  {AMBER}Total de portas abertas: {GREEN}{len(abertas)}{R}")
    else:
        print(f"\n  {GRAY}Nenhuma porta aberta encontrada no intervalo.{R}")
    pausar()


# ──────────────────────────────────────────
#  3. DISPOSITIVOS NA REDE (ARP)
# ──────────────────────────────────────────
def rede_dispositivos():
    limpar(); exibir_banner(); sep()
    print(f"  {BOLD}{AMBER}DISPOSITIVOS NA REDE{R}\n")
    print(f"  {GRAY}Executando varredura ARP... aguarde.{R}\n")
    sep()

    if os.name == "nt":
        # Windows: arp -a lista todos os dispositivos conhecidos
        os.system("arp -a")
    else:
        # Linux/Mac
        os.system("arp -n 2>/dev/null || ip neigh show")

    sep()
    print(f"\n  {GRAY}Dica: execute como administrador para resultados completos.{R}")
    pausar()


# ──────────────────────────────────────────
#  4. TRACEROUTE
# ──────────────────────────────────────────
def rede_traceroute():
    limpar(); exibir_banner(); sep()
    print(f"  {BOLD}{AMBER}TRACEROUTE{R}\n")

    host = input(f"  {CREAM}Host de destino (ex: google.com): {R}").strip() or "google.com"
    print(f"\n  {GRAY}Rastreando rota até {AMBER}{host}{GRAY}...{R}\n")
    sep()

    if os.name == "nt":
        os.system(f"tracert {host}")
    else:
        os.system(f"traceroute {host}")

    pausar()


# ══════════════════════════════════════════
#  OPÇÕES ORIGINAIS
# ══════════════════════════════════════════
def opcao_ping():
    limpar(); exibir_banner(); sep()
    print(f"  {BOLD}{AMBER}TESTE DE CONEXÃO{R}\n")
    host = input(f"  {CREAM}Host (padrão 8.8.8.8): {R}").strip() or "8.8.8.8"
    print(f"\n  {GRAY}Pingando {AMBER}{host}{GRAY}...{R}\n"); sep()
    os.system(f"ping -c 3 {host}" if os.name != "nt" else f"ping -n 3 {host}")
    pausar()

def opcao_sistema():
    limpar(); exibir_banner(); sep()
    print(f"  {BOLD}{AMBER}INFORMAÇÕES DO SISTEMA{R}\n")
    import platform
    for k, v in [
        ("Sistema",     platform.system()),
        ("Versão",      platform.version()[:45]),
        ("Máquina",     platform.machine()),
        ("Processador", platform.processor()[:45]),
        ("Python",      platform.python_version()),
        ("Hostname",    platform.node()),
    ]:
        print(f"  {SEPIA}{k:<14}{R}{CREAM}{v}{R}")
    pausar()

def opcao_sobre():
    limpar(); exibir_banner(); sep()
    print(f"  {BOLD}{AMBER}SOBRE O PROGRAMA{R}\n")
    for k, v in [
        ("Nome",      "ALEK Menu Terminal"),
        ("Versão",    "1.0.0"),
        ("Autor",     "Alek"),
        ("Linguagem", "Python 3"),
        ("Tema",      "Breaking Bad / Heisenberg"),
    ]:
        print(f"  {SEPIA}{k:<12}{R}{CREAM}{v}{R}")
    print(f"\n  {GRAY}Menu interativo com estilo.{R}")
    pausar()


# ══════════════════════════════════════════
#  FUNCAO SECRETA  —  WW
# ══════════════════════════════════════════
def segredo_ww():
    limpar()
    exibir_banner()
    sep()
    print()
    morse = "--. .. - / .... ..- -... / .- .-.. . -.- -.-. --- -.. . -....- ..- .."
    print(f"  {AMBER}[ W W ]{R}")
    print()
    for ch in morse:
        import sys, time
        sys.stdout.write(f"{AMBL}{ch}{R}")
        sys.stdout.flush()
        time.sleep(0.07)
    print()
    print()
    sep()
    digitar(f"  {SEPIA}\"--. .. - / .... ..- -... / .- .-.. . -.- -.-. --- -.. . -....- ..- ..\"  {R}", delay=0.03)
    sep()
    pausar()

def sair():
    limpar(); exibir_banner(); sep()
    digitar(f"\n  {SEPIA}\"O negócio está encerrado.\" — Heisenberg{R}\n", delay=0.04)
    sep(); time.sleep(1); sys.exit(0)


# ══════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════
if __name__ == "__main__":
    try:
        tela_abertura()
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n\n  {DRED}Interrompido.{R}\n")
        sys.exit(0)
