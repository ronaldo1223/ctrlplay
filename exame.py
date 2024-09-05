#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Prova():

    def __init__(self):
        self.questoes = []
        self.resposta=[]

    def motra_questoes(self):
        print(self.questoes)

    def mosrar_resposta(self):
        print(self.resposta)

    def Armazena_QAuestao_resposta(self, novaQuestao, novaResposta):
        self.resposta.append(novaResposta)

