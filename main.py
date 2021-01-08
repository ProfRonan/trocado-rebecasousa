"""Arquivo principal que será interpretado pelo interpretador."""
def entrada ():
      global valor 
      valor = float(input("Digite um valor a ser trocado até R$10:"))
      teste_valor()

def teste_valor():
      if valor > 10:
        print("Por favor digite um valor válido:")
        entrada()
      else:
        teste_troco()

def main(): 

    """Função principal que será rodada quando o script for passado para o interpretador."""
    entrada()

def teste_troco():
  global valor
  valor = valor * 100
  print("São necessárias:")
  if valor//100 > 0:
    print(f"moedas de R$ 1.00: {valor//100:.0f}")
  valor = valor%100
  if valor//50 > 0:
    print(f"moedas de R$ 0.50: {valor//50:.0f}")
  valor = valor%50
  if valor//25 > 0:
    print(f"moedas de R$ 0.25: {valor//25:.0f}")
  valor = valor%25    
  if valor//10 > 0:
    print(f"moedas de R$ 0.10: {valor//10:.0f}")
  valor = valor%10
  if valor//5 > 0:
    print(f"moedas de R$ 0.05: {valor//5:.0f}")
  valor = valor%5
  if valor//1 > 0:
    print(f"moedas de R$ 0.01: {valor//1:.0f}")

       

if __name__ == '__main__':
    main()
