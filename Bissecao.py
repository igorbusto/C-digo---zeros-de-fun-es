def func(x): 
    return 10 - x*x

def bisection(a,b): 
  
    if (func(a) * func(b) >= 0): 
        print("Você não inseriu valores válidos para a ou b\n") 
        return
   
    c = a 
    while ((b-a) >= 0.01): 
        # Ponto médio
        c = (a+b)/2
        # Checar se ponto médio é a raiz
        if (func(c) == 0.0): 
            break
        # Deicidir o lado da repeitção (+/-)
        if (func(c)*func(a) < 0): 
            b = c 
        else: 
            a = c 
    print("O valor da raiz é:","%.4f"%c) 

# Valores iniciais
a = -2
b = 5
bisection(a, b) 