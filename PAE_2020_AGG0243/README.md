## Bem Vindo à Página do Projeto PAE 2020

Nossa intenção aqui, foi ilustrar a importância do uso de equações diferencias (ED's), com alguns exemplos aplicáveis ao estudo da Geofísica. Com esse objetivo em mente, disponibilizamos alguns códigos básicos em linguagem Python, que permitem a execução e interação do estudante. Os códigos podem ser alterados pelo usuário que tenha uma noção básica de Python, modificando valores de váriáveis de acordo com o modelo de interesse. Em alguns casos, ferramentas interativas do ipywidgets permitem a interação em tempo real, mesmo que não se tenha familiaridade com programação.

### Acesso aos arquivos
Para baixar os arquivos, clique no botão "View on GitHub" localizado no início da página.

### Disposição de arquivos

Os arquivos estão organizados em dois grupos, um de códigos executáveis, outro de mini relatórios que fornecem detalhes básicos sobre os problemas abordados e a composição dos códigos. Arquivos com extensão "ipynb", devem ser executados em ipyhton notebook, já aqueles com extensões "py", em qualquer IDE rodando Python 3.

### Estrutura básica de código

Os códigos estão estruturados em alguns blocos para facilitar o entendimento e modificações. O trecho abaixo é um exemplo de bloco responsável pela chamada de **módulos do Python** necessários ao funcionamento dos programas.

```python
# MODULOS PYTHON

import numpy as np
import math as mh
import matplotlib.pyplot as plt
```
Abaixo temos um exemplo de bloco de **funções**, que são responsáveis pelo cálculo das grandezas envolvidas no problemas.

```python
# FUNCOES

def pot_g(gamma,a,rho,x,x0,z,z0): #calcula o potencial gravitacional
    U = gamma*((4/3)*np.pi*(a**3)*rho)/((x-x0)**2+(z-z0)**2)**(1/2)
    return U
```
Alterações dos modelos em geral devem ser feitas nos blocos de **parâmetros do modelo**, que possuem o seguinte estilo:

```python
# PARAMETROS DO MODELO

# gamma -> constante gravitacional (m³/(km.s²))
x = np.linspace(0,5000,50) #extesao perfil
```
Os resultados podem ser avaliados em figuras, tabelas e animações gerados em blocos marcados como **plotagem** ou algo relacionado.

```python
# ------ ANIMACAO SECAO 1D EM PROFUNDIDADE -------------------------------

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
```

### Suporte ou contato

Gostaria de contribuir, tirar dúvidas, indicar bugs? Entre em contato com [estagiário PAE 2020](felipeiag2012@gmail.com).
