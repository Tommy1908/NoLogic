import newLogic

entry: str = ""
table: list[list[str]] = []
vars: list[str] = []

def get_vars(s: str):
    global vars
    vars = []
    for i in range(len(s)):
        if 122 >= ord(s[i]) >= 97 and s [i] not in vars:
            vars.append(s[i])


def size() -> int:
    return 2 ** len(vars)

def fill_table():
    global table, vars
    table = []
    factor_div: int = 2

    for i in range(len(vars)):
        table.append([])
        while len(table[i]) != size():
            for _ in range(int(size() / factor_div)):
                table[i].append('T')
            for _ in range(int(size() / factor_div)):
                table[i].append('F')

        factor_div *= 2

def print_table():
    global table, vars
    print(f"{vars}  ↓")
    for i in range(size()):
        l = []
        for k in range(len(vars)+1):
            l.append(table[k][i])
        print(l)


def callLogic(funcion:str):
    global table, vars

    
    valores:dict[str,str] = {}
    resultados:list[str] = []

    for i in range(len(table[0])):
        for v in range(len(vars)):
            valores[vars[v]] = table[v][i]
        #Aca hay un diciconario con uno de las combinacion

        resultados.append(newLogic.evaluar(funcion, valores))

    table.append(resultados)
    return resultados

def comparar():
        global table, vars
        f1 = input("Insert first: ")
        get_vars(f1)
        fill_table()
        r1 = callLogic(f1)

        f2 = input("Insert second: ")
        get_vars(f2)
        fill_table()
        r2 = callLogic(f2)

        if(r1==r2):
            print("Son equivalentes")
            print(f"F1 y F2 -> {r1}")

        else:
            print("No equivalentes")
            print(f"F1 -> {r1}")
            print(f"F2 -> {r2}")


print("Welcome to noLogic!")
print("'Q' to exit, 'H' for help")
entry = input("Insert here: ")

while(entry != 'Q'):
    if(entry == "H"):
        print('Variables are lowercase letters\nUse "comp" to enable comparison mode\nUse "Q" to exit')

    elif("comp" in entry):
        comparar()

    else:  
        print(f"Table for: {entry}")
        get_vars(entry)
        fill_table()
        callLogic(entry)
        print_table()


    entry = input("Insert here: ")



#  | & -> <->
# || && => <=>