print("\nOlá utilizador!")
print("Porfavor introduza as suas notas dos três diferentes testes: ")

nota1 = float(input("\nTeste 1 \"25%\": "))
nota2 = float(input("Teste 1 \"35%\": "))
nota3 = float(input("Teste 1 \"40%\": "))

MAX = 20
MIN = 0

if nota1 > MAX or nota2 > MAX or nota3 > MAX:
    print("atuamae")
elif  nota1 < MIN or nota2 < MIN or nota3 < MIN:
        print("atuamae2")  
elif nota1 >= MIN and nota2 >= MIN and nota3 >= MIN:
    if nota1 <= MAX and nota2 <= MAX and nota3 <= MAX:
        nota1_1 = nota1 * 25
        nota2_2 = nota2 * 35
        nota3_3 = nota3 * 40 
        notafinal = (nota1_1 + nota2_2 + nota3_3) / 100 
        print("A tua média é igual a: ",notafinal)    
        if notafinal >= 9.5:
            print("Por isso estás Aprovado")
        else:
            print("Por isso estás Reprovado")