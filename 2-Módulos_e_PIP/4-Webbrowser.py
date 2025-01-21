import webbrowser

done = False

while not done:
    print("O que você deseja fazer?")
    print("1. Aprender Python")
    print("2. Aprender sobre Módulos")
    print("3. Aprender Python, FullStack JS, Inglês e No Code")
    print("4. Sair")
    choice = input("> ")

    if choice == "1":
        webbrowser.open("<http://www.python.org>")
    elif choice == "2":
        webbrowser.open("<https://docs.python.org/3/py-modindex.html>")
    elif choice == "3":
        webbrowser.open("<https://pages.onebitcode.com/>")
    elif choice == "4":
        done = True
    else:
        print("Opção inválida!")