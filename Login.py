"""
Descrição:
Este script Python demonstra um sistema de autenticação de login básico, uti
apenas estruturas de dados em memória (dicionários) para simular o armazenam
de usuários. O objetivo é focar na lógica de registro e validação de credenc
exclusivamente para usuários do tipo \'cliente\', sem a complexidade de fram
ou bancos de dados reais.
"""
# Simulação de um \'banco de dados\' em memória
# Armazena usuários clientes com email, senha (texto plano para simplificaçã
USUARIOS_DB = {
 "cliente1@email.com": {"senha": "senha123", "nome": "Cliente Um"},
 "cliente2@email.com": {"senha": "abc456", "nome": "Cliente Dois"}
}
def registrar_cliente(email, senha, nome):
 """
 Simula o registro de um novo cliente.

 Args:
 email (str): Email do cliente.
 senha (str): Senha do cliente.
 nome (str): Nome do cliente.

 Returns:
 dict: Um dicionário indicando sucesso ou falha no registro.
 """
 if email in USUARIOS_DB:
 return {"sucesso": False, "mensagem": "Email já cadastrado."}

 USUARIOS_DB[email] = {"senha": senha, "nome": nome}
 return {"sucesso": True, "mensagem": "Cliente registrado com sucesso."}
def fazer_login_cliente(email, senha):
 """
 Simula o processo de login de um cliente.

 Args:
 email (str): Email do cliente.
 senha (str): Senha fornecida pelo cliente.

 Returns:
 dict: Um dicionário indicando sucesso ou falha no login, e os dados
 """
 if email not in USUARIOS_DB:
 return {"sucesso": False, "mensagem": "Cliente não encontrado."}

 cliente = USUARIOS_DB[email]

 if cliente["senha"] == senha:
 return {
 "sucesso": True,
 "mensagem": "Login de cliente realizado com sucesso!",
 "cliente": {
 "email": email,
 "nome": cliente["nome"]
 }
 }
 else:
 return {"sucesso": False, "mensagem": "Senha incorreta."}
def main():
 print("--- Testes de Registro de Clientes ---")
 # Teste de registro de um novo cliente
 print("Registrando novo cliente:", registrar_cliente("novo_cliente@email
 # Teste de registro de email já existente
 print("Registrando email existente:", registrar_cliente("cliente1@email.

 print("\n--- Testes de Login de Clientes ---")
 # Teste de login bem-sucedido (cliente1)
 print("Login cliente (sucesso):", fazer_login_cliente("cliente1@email.co
 # Teste de login bem-sucedido (cliente2)
 print("Login cliente (sucesso):", fazer_login_cliente("cliente2@email.co
 # Teste de login com senha incorreta
 print("Login cliente (senha incorreta):", fazer_login_cliente("cliente1@
 # Teste de login com cliente não existente
 print("Login cliente (não existe):", fazer_login_cliente("naoexiste@emai

 print("\n--- Estado atual do DB (simulado) ---")
 for email, dados in USUARIOS_DB.items():
 print(f"Email: {email}, Nome: {dados[\'nome\']}")
if __name__ == "__main__":
 main()
