#include <stdio.h>
#include <string.h>

void limpar_entrada() {
    char c;
    while ((c = getchar()) != '\n' && c != EOF) {}
}

void ler_texto(char *buffer, int length) {
    fgets (buffer, length, stdin);
    strtok(buffer, "\n");    
}

int main () {

    int idade;
    double salario, altura;
    char genero;
    char nome [50];

    printf("Digite o valor da idade:");
    scanf ("%d", &idade);

    printf("Digite o valor do salario:");
    scanf ("%lf", &salario);

    printf("Digite o valor da altura:");
    scanf ("%lf", &altura);
 
    printf("Digite o seu nome:");
    limpar_entrada();
    ler_texto(nome, 50);

    printf("Digite o seu genero:");
    scanf("%c", &genero);

    printf("Programa teste\n");
    printf("IDADE = %d\n", idade);
    printf("SALARIO = %.2lf\n", salario);
    printf("ALTURA = %.2lf\n", altura);
    printf("NOME = %s\n", nome);
    printf("GENERO = %c\n", genero);

    return 0;

}