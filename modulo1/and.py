"""
 Operadores Logicos
 * and (e) or (ou) not (não)
 * or- Qualquer condição verdadeira avaliada
 * todas as expressão como verdadeira
 * Se qualquer valor for considerado verdadeiro,
 * a expressão interira será avalida naquele valor.
 * São considerado falsy 
 * 0 0.0 '' False
 * Tambem existe o tipo 
 * None que é usado para representar um não valor  

entrada = input("[E]nter [S]air: ")
senha = input('Senha: ')
senha_per = '1234'

if entrada == "E" and senha == senha_per:
    print("Entrar")
"""
entrada = input("[E]nter [S]air: ")
senha = input('Senha: ')
senha_per = '1234'
    
if (entrada == "E" or entrada == 'e') and  senha == senha_per :
    print("Entrar")
    
    