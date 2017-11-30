n = 5000 #nb ppl dans le graphe
gpr = 1 #gossip per sec
gpra = 100 #for attackers
iter = 50
gountil = 35
xfoisnba = 2
import random

moyennescoretab = []

for nbaa in range(1, gountil) :
    nba = nbaa*xfoisnba
    scoretab = []
    for jj in range(iter) :
        print(nbaa, jj)
        ppl = [i for i in range(n)]
        attackers = [i for i in range(nba)]
        alice = n-1
        status = [None for i in range(n)] #true if alice, false if attackers
        status[-1] = True
        restant = n-1
        for k in range(100) :
            gentil = [i for i in range(n) if status[i] == True]
            mechant = [i for i in range(n) if status[i] == False]
            #priorité aux gentil
            for mec in mechant :
                if mec in attackers :
                    for _ in range(gpra) :
                        tmp = random.randint(0, n-1)
                        if status[tmp] == None :
                            status[tmp] = False
                            restant -= 1
                else :
                    for _ in range(gpr) :
                        tmp = random.randint(0, n-1)
                        if status[tmp] == None :
                            status[tmp] = False
                            restant -= 1
                    
            for _ in gentil :
                for _ in range(gpr) :
                    tmp = random.randint(0, n-1)
                    if status[tmp] == None :
                        status[tmp] = True
                        restant -= 1
                    if tmp in attackers :
                        for i in attackers :
                            if status[i] == None :
                                status[i] = False #instant gossip
                                restant -= 1
            if restant == 0 :
                break
        score = sum(status)/n
        scoretab.append(score)
    moyennescoretab.append(sum(scoretab)/iter)



from matplotlib import pyplot as plt

plt.plot([100*xfoisnba*i/n for i in range(1, gountil)], [100*(1-i) for i in moyennescoretab])
plt.legend = ["% des attaquants", "% de réussite de l'attaque"]
plt.show()
