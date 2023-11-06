pessoas_que_fazem_o_L = 80000
crescimentoA = 0.03
pessoas_que_nao_fazem_o_L = 200000
crescimentoB = 0.015

anos_sem_picanha = 0

while pessoas_que_fazem_o_L < pessoas_que_nao_fazem_o_L:
    pessoas_que_fazem_o_L += pessoas_que_fazem_o_L * crescimentoA
    pessoas_que_nao_fazem_o_L += pessoas_que_nao_fazem_o_L * crescimentoB
    anos_sem_picanha += 1
    
print(f"Em cerca de {anos_sem_picanha}, a população do pais B será de {pessoas_que_nao_fazem_o_L}, e a população do país A será {pessoas_que_fazem_o_L} (faz o L agora)")
    