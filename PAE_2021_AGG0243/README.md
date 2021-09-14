## Bem Vindo à Página do Projeto PAE 2021
O objetivo principal dessas rotinas é ilustrar aos alunos como o conteúdo ministrado na disciplina (equações diferenciais ED's) contribui para o entendimento dos estudos geofísicos. Com esse objetivo em mente, disponibilizamos alguns códigos básicos em linguagem Python, que permitem a execução e interação do estudante. Os códigos podem ser alterados pelo usuário que tenha uma noção básica de Python, modificando valores de váriáveis de acordo com o modelo de interesse. 

### Acesso aos arquivos
Para baixar os arquivos, clique no botão "View on GitHub" localizado no início da página.

### Disposição de arquivos

Foram criados dois arquivos com extensão "ipynb" que devem ser executados em ipython notebook. Os arquivos são independentes, pois cada um aborda um problema geofísico. No próprio código executável está descrito detalhes básicos sobre o problema abordado e a matemática envolvida no algoritmo.


### Estrutura básica de código

Os códigos estão estruturados em alguns blocos para facilitar o entendimento e modificações. O trecho abaixo é um exemplo de bloco responsável pela chamada de **módulos do Python** necessários ao funcionamento dos programas.

```python
# MODULOS PYTHON

import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt
```
Abaixo temos um exemplo de bloco de **funções**, que são responsáveis pelo cálculo das grandezas envolvidas no problemas.

```python
# FUNCOES

def fun_t(x_t,y_t):
    "Funcao para reduzir a EDO de quarta ordem para primeira ordem. Carga Triangular"
    l_t=1 #Alterar o valor da metade da base do triangulo
    derivatey0=y_t[1]
    derivatey1=y_t[2]
    derivatey2=y_t[3]
    derivatey3=-4*y_t[0]+(1-(x_t/l_t))*np.heaviside(1-(x_t/l_t),1)
    return np.vstack ((derivatey0,derivatey1,derivatey2,derivatey3))
```
Alterações dos modelos em geral devem ser feitas nos blocos de **parâmetros do modelo**, que possuem o seguinte estilo:

```python
# PARAMETROS DO MODELO

#Configurando "chutes" iniciais
x_initial=np.linspace(0,infinity,101)
y_initial= np.zeros((4, x_initial.size))
```
Os resultados podem ser avaliados em gráficos gerados em blocos marcados como **plotagem** ou algo relacionado.

```python
# PLOTAGEM DOS RESULTADOS

x_barra=x_initial
w=solution.sol(x_barra)[0]
plt.plot(x_barra, w)
plt.xlabel("x_barra")
plt.ylabel(y_label)
plt.ylim(max(w), min(w)-0.02)
plt.title(titulo)
plt.show()
```

### Suporte ou contato

Gostaria de contribuir, tirar dúvidas, indicar bugs? Entre em contato com [estagiário PAE 2021](lais.nathalia.rodrigues@usp.br).
