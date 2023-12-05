# IMPORTS

import Jogo
import MainMenuAndCharCreation
import START
import UserImputsAndGameOptions

# YOU DIED 

def ASCII_YouDied():
    print("|                         ■ —————————————————————————————————————————————————————————————————————————————————————————————————————————■                          |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                           ▄██   ▄    ▄██████▄  ███    █▄       ████████▄   ▄█     ▄████████ ████████▄                                         |")
    print("|                                           ███   ██▄ ███    ███ ███    ███      ███   ▀███ ███    ███    ███ ███   ▀███                                        |")
    print("|                                           ███▄▄▄███ ███    ███ ███    ███      ███    ███ ███▌   ███    █▀  ███    ███                                        |")
    print("|                                           ▀▀▀▀▀▀███ ███    ███ ███    ███      ███    ███ ███▌  ▄███▄▄▄     ███    ███                                        |")
    print("|                                           ▄██   ███ ███    ███ ███    ███      ███    ███ ███▌ ▀▀███▀▀▀     ███    ███                                        |")
    print("|                                           ███   ███ ███    ███ ███    ███      ███    ███ ███    ███    █▄  ███    ███                                        |")
    print("|                                           ███   ███ ███    ███ ███    ███      ███   ▄███ ███    ███    ███ ███   ▄███                                        |")
    print("|                                           ▀█████▀   ▀██████▀  ████████▀       ████████▀  █▀     ██████████ ████████▀                                          |")
    print("|                                                                                                                                                               |")
    print("|                                                         ┏┓   ┏┓┳┳┳┏┳┓                ┳┓   ┳┓┏┓┏┓┏┳┓┏┓┳┓┏┳┓                                                    |")
    print("|                                                    -~-  ┣┫   ┃┃┃┃┃ ┃  -~-       -~-  ┣┫   ┣┫┣ ┗┓ ┃ ┣┫┣┫ ┃   -~-                                               |")
    print("|                                                         ┛┗•  ┗┻┗┛┻ ┻                 ┻┛•  ┛┗┗┛┗┛ ┻ ┛┗┛┗ ┻                                                     |")
    print("|                                                                                                                                                               |")
    print("|                         ■ —————————————————————————————————————————————————————————————————————————————————————————————————————————■                          |")
    print("|                                    Rafael Matias                        PW 23/25                               ETIC Algarve                                   |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    while True:
        opcao = input("Escolha uma opção: ").strip()

        if opcao == 'A':

            print("|                         ■ —————————————————————————————————————————————————————————————————————————————————————————————————————————■                          |")
            print("|                                                                                                                                                               |")
            print("|                                                                                                                                                               |")
            print("|                                                                       SAIR DO JOGO?                                                                           |")
            print("|                                                                IRÁ PERDER TODO O PROGRESSO                                                                    |")
            print("|                                                      - [A] Sim -                       - [B] Não -                                                            |")
            print("|                                                                                                                                                               |")
            print("|                                                                                                                                                               |")
            print("|                         ■ —————————————————————————————————————————————————————————————————————————————————————————————————————————■                          |")

            while True:
                opcao = input("Escolha uma opção: ").strip()

                if opcao == 'A':
                    import MainMenuAndCharCreation as GoBackTo
                    GoBackTo.MainMenu()  
                    break
                if opcao == 'B':
                    import Jogo as StartOver 
                    StartOver.Jogo()
                    break
                else:
                    if opcao != 'A' and opcao != 'B':
                        print("ERRO: Insira uma opção válida.")
        if opcao == 'B':
            import Jogo as StartOver 
            StartOver.Jogo()
            break



# OBSERVAR

def ASCII_OLHO():
    print("                                                                                                                                                               ")
    print("             ⠀⠀       ⠀⠀⠀⠀⠀⠀⠀                                   ⠀⠀     ⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                       ")
    print("             ⠀⠀⠀⠀⠀⠀⠀⠀       ⠀⠀                                         ⠀⢀⣄⠀⠀⢿⡇⠀⠀⣾⢀⣸⣄⠀⢠⡐⡄⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                 ")
    print("⠀⠀              ⠀⠀⠀⠀⠀⠀                                              ⡀⠀⢧⢘⣼⣤⠴⠾⣿⡛⠋⣿⡏⢹⡏⠉⣽⢻⢛⡟⢲⡿⣤⣠⣆⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                              ")
    print("⠀⠀⠀⠀ ⠀⠀⠀                                                        ⠀⢻⣤⡼⠿⣟⣿⣷⣤⣸⣿⣦⣿⣷⣿⣷⣾⣿⣿⣿⣷⣟⣁⣴⡿⠟⠲⣤⣴⠃⠀⢀⠄⠀⠀⠀⠀⠀                                                ")
    print("⠀⠀⠀             ⠀⠀                                             ⠰⣼⣶⣎⣉⣙⣿⣿⠿⢻⣿⠟⠋⠉⠙⢟⣛⠀⠀⠀⠙⠟⢿⡙⠛⠿⣶⣶⡾⠋⢉⣳⣴⡟⡠⠀⢀⢀⠀⠀                                              ")
    print("⠀    ⠀⠀                                                      ⠠⣄⣠⣋⣉⣹⣿⠟⠋⠀⠀⡾⠁⠀⠀⢀⣾⣿⣿⣿⠷⠀⢤⡀⠈⣷⠀⠀⠀⠉⠻⢿⣿⣿⡿⠛⢧⣠⣾⠞⠀⠀                                                ")
    print("⠀⠀                                                          ⣀⣞⣭⣽⡿⠟⠁⠀⠀⠀⠀⡇⠀⠀⠀⢸⣿⣿⣿⣿⣄⣀⣠⠇⠀ ⢸⠀⠀⠀⠀⠀⠀⠈⠛⣾⣿⣿⣯⠴⠂⣀⡴                                                ")
    print("⠀                                                          ⠐⠦⠴⣶⡿⡟⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠘⢿⣿⣿⣿⡿⠃⠀⠀⠀ ⡿⠀⠀⠀⠀⠀⠀⢀⣾⣿⣭⣍⡉⠉⠉⠁⠀                                                ")
    print("                                                           ⠎⢩⠟⠋⢃⢳⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠉⠀⠀⠀⠀  ⢀⡾⠁⠀⠀⠀⠀⣀⣴⣿⣟⣋⠉⠉⡓⠦⠀⠀⠀                                                ")
    print("                                                            ⠘⠒⠒⠘⠢⠧⢤⣀⡀⠀⠀⠀⠀⠈⠻⢦⣀⠀⠀⠀⠀⢀⣀⡴⠛⠁⠀⠀⣀⣤⣾⣿⣏⡉⠉⢉⡿⠿⠀⠀⠀⠀                                                 ")
    print("⠀    ⠀                                                       ⠀⠀  ⠦⢤⡾⣿⡿⣷⣶⣦⣤⣄⣀⣈⣉⣉⣉⣉⣉⣁⣠⣤⣴⣾⡿⣿⣿⢧⡀⠈⣹⠶⠋⠀⠀⠀                                                     ")
    print("⠀    ⠀⠀⠀                                                            ⠈⠓⠤⣋⠁⡼⠛⠛⡿⣿⠖⢛⣿⠛⠛⣿⡟⠛⠻⣿⡱⠄⠉⣣⠼⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                 ")
    print("⠀⠀   ⠀⠀⠀                                                               ⠀⠉⠓⠤⢤⣹⣁⠀⢸⡇⠀⠀⠸⡃⣀⣀⠬⠷⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                 ")
    print("⠀    ⠀⠀⠀⠀⠀                                                                     ⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                                  ")
    print("                                                                        ┏┓┳┓┏┓┏┓┳┓┓┏┏┓┳┓                                                                      ")
    print("                                                                    -~- ┃┃┣┫┗┓┣ ┣┫┃┃┣┫┣┫ -~-                                                                  ")
    print("                                                                        ┗┛┻┛┗┛┗┛┛┗┗┛┛┗┛┗                                                                      ")
    print("                                                                                                                                                               ")



# Vitória Nível I (Demo)

def ASCII_LVLI_SUCCESS():
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                         ■ —————————————————————————————————————————————————————————————————————————————————————————————————————————■                          |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    print("|                                              ▄██   ▄    ▄██████▄  ███    █▄        ▄█     █▄   ▄█  ███▄▄▄▄                                                    |")
    print("|                                              ███   ██▄ ███    ███ ███    ███      ███     ███ ███  ███▀▀▀██▄                                                  |")
    print("|                                              ███▄▄▄███ ███    ███ ███    ███      ███     ███ ███▌ ███   ███                                                  |")
    print("|                                              ▀▀▀▀▀▀███ ███    ███ ███    ███      ███     ███ ███▌ ███   ███                                                  |")
    print("|                                              ▄██   ███ ███    ███ ███    ███      ███     ███ ███▌ ███   ███                                                  |")
    print("|                                              ███   ███ ███    ███ ███    ███      ███     ███ ███  ███   ███                                                  |")        
    print("|                                              ███   ███ ███    ███ ███    ███      ███ ▄█▄ ███ ███  ███   ███                                                  |")
    print("|                                              ▀█████▀   ▀██████▀  ████████▀        ▀███▀███▀  █▀    ▀█   █▀                                                    |")
    print("|                                                                                                                                                               |")
    print("|                                                                  ┓ ┏┓┓┏┏┓┓   ┳  ┏┓┓ ┏┓┏┓┳┓                                                                    |")
    print("|                                                              -~- ┃ ┣ ┃┃┣ ┃   ┃  ┃ ┃ ┣ ┣┫┣┫ -~-                                                                |")
    print("|                                                                  ┗┛┗┛┗┛┗┛┗┛  ┻  ┗┛┗┛┗┛┛┗┛┗                                                                    |")
    print("|                                                                                                                                                               |")
    print("|                         ■ —————————————————————————————————————————————————————————————————————————————————————————————————————————■                          |")
    print("|                                    Rafael Matias                        PW 23/25                               ETIC Algarve                                   |")
    print("|                                                                                                                                                               |")
    print("|                                                                                                                                                               |")
    
    while True:
        opcao = input("FIM DO DEMO. [A] JOGAR DE NOVO     [B] MAIN MENU: ").strip()

        if opcao == 'A':
            import Jogo as StartOver 
            StartOver.Jogo()
            break
        
        if opcao == 'B':
            import MainMenuAndCharCreation as GoBackTo
            GoBackTo.MainMenu()  
            break

        else:
            if opcao != 'A' and opcao != 'B':
                print("ERRO: Insira uma opção válida.")



                

