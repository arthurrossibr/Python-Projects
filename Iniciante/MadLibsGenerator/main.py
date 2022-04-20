# Mad Lib Generator

# Questões para coletar as informações
substantivo = input("Escolha um substantivo: ")
substantivo_plural = input("Escolha um substantivo no plural: ")
verbo = input("Escolha um verbo: ")
lugar = input("Nome de um lugar: ")
adjetivo = input("Escolha um adjetivo: ")
adjetivo2 = input("Escolha outro adjetivo ")

# Une e exibe a história montada
madlib = f"Progamação de computadores é tão {adjetivo}! Isso me deixa o tempo todo animado porque " \
         f"eu amo {verbo}. Fique hidratado e {adjetivo2} como se estivesse em {lugar} usando {substantivo} " \
         f"ou com vários {substantivo_plural}"
print(madlib)
