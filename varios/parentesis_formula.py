def parentesis(formula, operacion):
    resultado = []
    index_oper = formula.find(operacion)
    
    if index_oper == -1:
       resultado.append(formula)
       resultado.append(False)
       return resultado 
    
    lista = list(formula)
    lista.insert(index_oper - 1, '(')
    lista.insert(index_oper + 3, ')')
    
    if operacion == '*':
        lista[index_oper+1] = 'p'
    elif operacion == '/':
        lista[index_oper+1] = 'd'

    formula = "".join(lista)
    resultado.append(formula)
    resultado.append(True)
    
    return resultado

def mult_or_division(formula):
   ready = True
   while ready:
      lista = parentesis(formula, '*')
      formula = lista[0]
      ready = lista[-1]
   ready = True
   while ready:
      lista = parentesis(formula, '/')
      formula = lista[0]
      ready = lista[-1]
   return formula 

formula = '3+5*6-4/5'

print(mult_or_division(formula))


    


