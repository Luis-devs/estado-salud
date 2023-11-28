import json

#Insertar diagnóstico a la base de datos

def insertar_diagnóstico(diag, ID): 
    query = f'UPDATE info_paciente SET Diagnóstico = {diag} WHERE Documento = {ID}'
    return query

#Verificar si el id que se quiere añadir ya existe
def ver_paciente(Id_):
    ver = f'SELECT * FROM info_paciente WHERE Documento = {Id_}'
    return ver

#Traer datos biométricos
def traer_paciente(Id_):
    bring = f'SELECT Peso, Altura, Medida_cintura, Medida_cadera, Medida_cuello, Sexo FROM info_paciente WHERE Documento = {Id_}'
    return bring

#Validar datos numéricos
def validardato(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return '\nPor favor ingrese un dato numérico, intente de nuevo'
