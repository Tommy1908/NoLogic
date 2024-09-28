#Es necesario que haya un parentesis general y uno para cada evaluacion


def evaluar(formula: str, valores: dict[str, str]) -> str:
    formula = formula.replace(' ', '')
    
    #print(formula)

    #Reemplazar las variables por sus valores de verdad
    for key,value in valores.items():
        formula = formula.replace(key,value)        
    #print(formula)


    while(len(formula) != 1):
        formula = evaluarNegaciones(formula)
        #print(formula)  
        formula = evaluarFormulasAtomicas(formula)
        #print(formula)
    return formula


    

def evaluarNegaciones(formula:str) -> str:
    formula = list(formula)
    formulaEvaluada = []

    for i in range(len(formula)):
        if formula[i] == '¬' and formula[i+1] == 'T':
            formulaEvaluada += 'F'
            formula[i+1] = " "
        elif formula[i] == '¬' and formula[i+1] == 'F':
            formulaEvaluada += 'T'
            formula[i+1] = " "
        elif formula[i] == '¬' and formula[i+1] == '¬':
            formula[i+1] = " "
        else:
            formulaEvaluada += formula[i]
    #print(formulaEvaluada)
    formulaEvaluada = listToString(formulaEvaluada)
    formula = listToString(formula)
    
    #Limpiamos y vuelve a formula
    formula = formulaEvaluada
    #print(formula)
    return formula

def evaluarFormulasAtomicas(formula:str) -> str:
    formula = formula.replace("(F&F)", 'F')
    formula = formula.replace("(T&F)", 'F')
    formula = formula.replace("(F&T)", 'F')
    formula = formula.replace("(T&T)", 'T')
    formula = formula.replace("F&F", 'F')
    formula = formula.replace("T&F", 'F')
    formula = formula.replace("F&T", 'F')
    formula = formula.replace("T&T", 'T')
    formula = formula.replace("(F^F)", 'F')
    formula = formula.replace("(T^F)", 'F')
    formula = formula.replace("(F^T)", 'F')
    formula = formula.replace("(T^T)", 'T')
    formula = formula.replace("F^F", 'F')
    formula = formula.replace("T^F", 'F')
    formula = formula.replace("F^T", 'F')
    formula = formula.replace("T^T", 'T')

    formula = formula.replace("(F|F)", 'F')
    formula = formula.replace("(T|F)", 'T')
    formula = formula.replace("(F|T)", 'T')
    formula = formula.replace("(T|T)", 'T')
    formula = formula.replace("(FVF)", 'F')
    formula = formula.replace("(TVF)", 'T')
    formula = formula.replace("(FVT)", 'T')
    formula = formula.replace("(TVT)", 'T')
    formula = formula.replace("F|F", 'F')
    formula = formula.replace("T|F", 'T')
    formula = formula.replace("F|T", 'T')
    formula = formula.replace("T|T", 'T')
    formula = formula.replace("FVF", 'F')
    formula = formula.replace("TVF", 'T')
    formula = formula.replace("FVT", 'T')
    formula = formula.replace("TVT", 'T')

    formula = formula.replace("(T<->T)", 'T')
    formula = formula.replace("(F<->F)", 'T')
    formula = formula.replace("(F<->T)", 'F')
    formula = formula.replace("(T<->F)", 'F')
    formula = formula.replace("T<->T", 'T')
    formula = formula.replace("F<->F", 'T')
    formula = formula.replace("F<->T", 'F')
    formula = formula.replace("T<->F", 'F')

    formula = formula.replace("(T->T)", 'T')
    formula = formula.replace("(T->F)", 'F')
    formula = formula.replace("(F->T)", 'T')
    formula = formula.replace("(F->F)", 'T')
    formula = formula.replace("T->T", 'T')
    formula = formula.replace("T->F", 'F')
    formula = formula.replace("F->T", 'T')
    formula = formula.replace("F->F", 'T')

    return formula

def listToString(lista:list[str]) -> str:
    res = ""
    for i in lista:
        res += i
    res = res.replace(" ","")
    return res
