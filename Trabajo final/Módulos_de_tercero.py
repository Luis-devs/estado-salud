import math

def IMC(peso, altura):
    result1 = peso / (altura * altura)
    return result1

def ICA(cintura, altura):
    op2_ = altura*100
    result2 = cintura / op2_
    return result2

def PorcentajeGrasaMujer(cintura, cadera, cuello, altura):
    op3 = cintura + cadera - cuello
    op3_ = altura*100
    result3 = (495 / (1.29579 - 0.35004 * (math.log(op3)) + 0.221 * (math.log(op3_))))-450
    return result3

def PorcentajeGrasaHombre(cintura, cuello, altura):
    op4 = cintura - cuello
    op4_ = altura*100
    result4 = (495 / (1.0324 - 0.19077 * (math.log(op4)) + 0.15456 * (math.log(op4_))))-450
    return result4
 
                                         

        
 
 
 