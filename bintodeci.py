Ndecimal = int(input('Digite um número em decimal:'))
Nbinario = bin(Ndecimal)
Nhexa = hex(Ndecimal)

print('O número %d em binário é: %s' % (Ndecimal,Nbinario[2:]))
print('O número %d em hexadecimal é: %s' % (Ndecimal,Nhexa[2:]))



