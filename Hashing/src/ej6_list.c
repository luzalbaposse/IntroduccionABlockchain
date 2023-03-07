#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node* addLast(struct node* n, int data) {

    // COMPLETAR
    
    return 0;
}

struct node* removeFirst(struct node* n) {

    // COMPLETAR
    
    return 0;
}

struct node* join(struct node* n1, struct node* n2) {

    // COMPLETAR
    
    return 0;
}

struct node* removeData(struct node* n, int data) {
    
    // COMPLETAR
    
    return 0;
}

void printList(struct node* n) {
    printf("[");
    if(n == 0){
        printf("]\n");
    } else {
        while(n->next != 0){
            printf("%i, ", n->data);
            n = n->next;
        }
        printf("%i]\n", n->data);
    }
}

int main() {
    /*
    // -- Descomentar para probar --
    // Lo siguiente es un ejemplo y DEBE ser modificado.

    struct node *n1 = NULL;
    printList(n1);
    printf("\n");

    printf("Agrego datos a la lista: n1\n");
    n1 = addLast(n1, 2021);
    n1 = addLast(n1, 42);
    n1 = addLast(n1, 0x400);
    printList(n1);
    printf("\n");

    printf("Agrego datos a la lista: n2\n");
    struct node *n2 = NULL;
    n2 = addLast(n2, 0);
    n2 = addLast(n2, 42);
    printList(n2);
    printf("\n");
    
    printf("Join lista n1 y n2: n3\n");
    struct node *n3 = join(n1, n2);
    printList(n3);
    printf("\n");

    printf("RemoveFirst: n3\n");
    n3 = removeFirst(n3);
    printList(n3);
    printf("\n");
    
    printf("RemoveData: 42\n");
    n3 = removeData(n3, 42);
    printList(n3);
    printf("\n");
    
    printf("RemoveFirst dos veces: n3\n");
    n3 = removeFirst(n3);
    n3 = removeFirst(n3);
    printList(n3);
    printf("\n");

    // */

    return 0;
}
