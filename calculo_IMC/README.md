

## Passo a Passo do Código para Calcular e Classificar o IMC

### 1. **Definir a função para calcular o IMC**
   - A função `calculo_IMC` recebe dois parâmetros: `peso` (em kg) e `altura` (em metros).
   - Ela retorna o valor do IMC calculado pela fórmula:  
     \[
     \text{IMC} = \frac{\text{peso}}{\text{altura}^2}
     \]

   ```python
   def calculo_IMC(peso, altura):
       return peso / (altura**2)
   ```

---

### 2. **Definir a função para classificar o IMC segundo a OMS**
   - A função `classificacao_IMC` recebe o valor do IMC e retorna a classificação correspondente, de acordo com as diretrizes da Organização Mundial da Saúde (OMS).
   - As classificações são:
     - IMC ≤ 18.5: **Baixo Peso**
     - 18.5 < IMC ≤ 24.9: **Peso Normal**
     - 25.0 < IMC ≤ 29.9: **Sobrepeso**
     - 30.0 < IMC ≤ 34.9: **Obesidade Grau I**
     - 35.0 < IMC ≤ 39.9: **Obesidade Grau II**
     - IMC ≥ 40.0: **Obesidade Grau III**

   ```python
   def classificacao_IMC(IMC):
       if IMC <= 18.5:
           return 'Baixo Peso'
       elif IMC <= 24.9:
           return 'Peso Normal'
       elif IMC <= 29.9:
           return 'Sobrepeso'
       elif IMC <= 34.9:
           return 'Obesidade Grau I'
       elif IMC <= 39.9:
           return 'Obesidade Grau II'
       else:
           return 'Obesidade Grau III'
   ```

---

### 3. **Solicitar dados do usuário**
   - O programa solicita ao usuário que insira o **peso** (em kg) e a **altura** (em metros).
   - Os valores são convertidos para `float` para permitir cálculos matemáticos.

   ```python
   peso = float(input('Digite o Peso em kg: '))
   altura = float(input('Digite sua Altura em m: '))
   ```

---

### 4. **Calcular o IMC**
   - O valor do IMC é calculado chamando a função `calculo_IMC` com os valores de `peso` e `altura` fornecidos pelo usuário.
   - O resultado é armazenado na variável `IMC`.

   ```python
   IMC = calculo_IMC(peso, altura)
   ```

---

### 5. **Classificar o IMC segundo a OMS**
   - A função `classificacao_IMC` é chamada com o valor do IMC calculado.
   - O resultado da classificação é armazenado na variável `classificacao`.

   ```python
   classificacao = classificacao_IMC(IMC)
   ```

---

### 6. **Exibir o resultado e a classificação do IMC**
   - O programa exibe o valor do IMC (arredondado para duas casas decimais) e a classificação correspondente.

   ```python
   print('O valor do IMC é:', round(IMC, 2), 'Segundo a OMS sua classificação é:', classificacao)
   ```

---

### Exemplo de Execução

#### Entrada:
   ```
   Digite o Peso em kg: 70
   Digite sua Altura em m: 1.75
   ```

#### Saída:
   ```
   O valor do IMC é: 22.86 Segundo a OMS sua classificação é: Peso Normal
   ```

---

### Resumo do Fluxo do Programa
1. Define as funções para calcular e classificar o IMC.
2. Solicita ao usuário que insira o peso e a altura.
3. Calcula o IMC usando a função `calculo_IMC`.
4. Classifica o IMC usando a função `classificacao_IMC`.
5. Exibe o valor do IMC e a classificação.

