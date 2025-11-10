int i;
int numero;
int soma;
float media;
int qtd;
int continuar;
soma = 0;
qtd = 0;
continuar = 1 == 1;
printf("=== Programa de Cálculo de Média ===");
do {
printf("Digite um número: ");
scanf("%d", numero);
soma = soma + numero;
qtd = qtd + 1;
printf("Deseja continuar? (1 para sim, 0 para nao): ");
scanf("%d", continuar);
}
 while (continuar);
printf("Números lidos: ", qtd);
printf("Soma total: ", soma);
if (qtd > 0) {
media = soma / qtd;
printf("Média final: ", media);
}
else {
printf("Nenhum número foi informado.");
}
printf("=== Teste de repetição for ===");
for (i = 1; i <= 5; i = i + 1) {
printf("Valor atual de i: ", i);
}
printf("=== Teste de repetição while ===");
i = 0;
while (i < 3) {
printf("Contador: ", i);
i = i + 1;
}
printf("=== Fim do programa ===");
