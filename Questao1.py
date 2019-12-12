def main():
    t = int(input("Digite a Quantidade de teste: "))




    for i in range (t):

        print()
        s=input("Digite a Escolha de Sheldon: ")
        print()
        r=input("Digite a Escolha de Raj: ")
        i=i+1


        if s == "tesoura" and r == "papel":
            print("Caso #t:",i,"Bazinga")
        elif s == "papel" and r == "tesoura":
            print("Caso #t:",i,"raj Trapaceou")
        elif s == "tesoura" and r == "tesoura" or s== "papel" and r == "papel":
            print("Caso t:",i," De Novo")
        if s == "papel" and r == "rocha":
            print("Caso #t:",i,"Bazinga")
        elif s == "rocha" and r == "papel":
            print("Caso #t:",i,"raj Trapaceou")
        elif s == "rocha" and r == "rocha" or s== "papel" and r == "papel":
            print("Caso #t:",i," De Novo")
        if s == "rocha" and r == "lagarto":
            print("Caso #t:",i,"Bazinga")
        elif s == "lagarto" and r == "rocha":
            print("Caso #t:",i,"raj Trapaceou")
        elif s == "rocha" and r == "rocha" or s== "lagarto" and r == "lagarto":
            print("Caso #t:",i," De Novo")
        if s == "lagarto" and r == "spock":
            print("Caso #t:",i,"Bazinga")
        elif s == "sporck" and r == "lagarto":
            print("Caso #t:",i,"raj Trapaceou")
        elif s == "lagarto" and r == "lagarto" or s== "spock" and r == "spock":
            print("Caso #t:",i," De Novo")
        if s == "spock" and r == "tesoura":
            print("Caso #t:",i,"Bazinga")
        elif s == "tesoura" and r == "spock":
            print("Caso #t:",i,"raj Trapaceou")
        elif s == "tesoura" and r == "tesoura" or s== "spock" and r == "spock":
            print("Caso #t:",i," De Novo")
        if s == "tesoura" and r == "lagarto":
            print("Caso #t:",i,"Bazinga")
        elif s == "lagarto" and r == "tesoura":
            print("Caso #t:",i,"raj Trapaceou")
        elif s == "tesoura" and r == "tesoura" or s== "lagarto" and r == "lagarto":
            print("Caso #t:",i," De Novo")
        if s == "lagarto" and r == "papel":
            print("Caso #t:",i,"Bazinga")
        elif s == "lagarto" and r == "papel":
            print("Caso #t:",i,"raj Trapaceou")
        elif s == "lagarto" and r == "lagarto" or s== "papel" and r == "papel":
            print("Caso #t:",i," De Novo")
        if s == "papel" and r == "spock":
            print("Caso #t:",i,"Bazinga")
        elif s == "spock" and r == "papel":
            print("Caso #t:",i,"raj Trapaceou")
        elif s == "spock" and r == "spock" or s== "papel" and r == "papel":
            print("Caso #t:",i," De Novo")
        if s == "spock" and r == "rocha":
            print("Caso #t:",i,"Bazinga")
        elif s == "rocha" and r == "sporck":
            print("Caso #t:",i,"raj Trapaceou")
        elif s == "rocha" and r == "rocha" or s== "spock" and r == "spock":
            print("Caso #t:",i," De Novo")
        if s == "rocha" and r == "tesoura":
            print("Caso #t:",i,"Bazinga")
        elif s == "tesoura" and r == "rocha":
            print("Caso #t:",i,"raj Trapaceou")
        elif s == "tesoura" and r == "tesoura" or s== "rocha" and r == "rocha":
            print("Caso #t:",i," De Novo")












main()