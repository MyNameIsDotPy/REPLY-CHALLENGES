import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file = open("example.txt","r")

ipt = file.readline()#input()
C, R, S = map(int, ipt.split())
ipt = file.readline()#input()
LenSnakes = sorted(list(map(int, ipt.split())), reverse=True)

board = np.zeros((R,C))
for i in range(R):
    ipt = file.readline()
    board[i] = board[i] + np.array(list(map(int, ipt.replace("*","-1").split())))

[print(i) for i in board]

#for row in range(R):
#    for column in range(C):


ax = sns.heatmap(board, linewidth=0.5, cmap='coolwarm')


plt.show()