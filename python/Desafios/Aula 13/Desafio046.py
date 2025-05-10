from time import sleep
import emoji

#Contagem regressiva
print(f'\033[0;92mIniciando a contagem para os fogos!\033[m')
for i in range(10, -1, -1):
    print(f'{i}...')
    sleep(1)

print(emoji.emojize('\033[4;95mBOOOOOOOOOOOOM!!!\033[m:fireworks:'))
