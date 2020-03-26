/* Good morning! Here's your coding interview problem for today. */

/* This problem was asked by Google. */

/* An XOR linked list is a more memory efficient doubly linked */
/* list. Instead of each node holding next and prev fields, it holds a */
/* field named both, which is an XOR of the next node and the previous */
/* node. Implement an XOR linked list; it has an add(element) which adds */
/* the element to the end, and a get(index) which returns the node at */
/* index. */

/* If using a language that has no pointers (such as Python), you can */
/* assume you have access to get_pointer and dereference_pointer */
/* functions that converts between nodes and memory addresses. */


#include <stdio.h>
#include <stdlib.h>

struct XorList {
    int data;
    uintptr_t npx;
};

typedef struct XorList *xnode;  // define xnode as a pointer of data type struct XorList


uintptr_t xor_ptr(uintptr_t p1, uintptr_t p2) {
    return p1 ^ p2;
}

xnode createXNode() {
    xnode temp; // declare a node
    temp = (xnode) malloc(sizeof(struct XorList));
    temp->npx = 0;
    return temp;
}

xnode addXNode(xnode head, int value){
    xnode temp;
    temp = createXNode();
    temp->data = value;
    if(head == NULL){
        head = temp;
    }
    else{
        temp->npx = xor_ptr(0, (uintptr_t) head);

        head->npx = xor_ptr((uintptr_t) temp,  head->npx);
    }
    return temp;
}

void printX(xnode head) {
    xnode p = head;
    uintptr_t prev = 0;
    while (p != NULL) {
        printf("%d ", p->data);
        // get next pointer
        uintptr_t next = xor_ptr(prev,  p->npx);
        prev = (uintptr_t) p;  // advance prev pointer
        p = (xnode) next;
    }
    printf("\n");
}

void test_xor() {
    xnode head = createXNode();
    head->data = 0;

    for (int i = 1; i < 5; i++) {
        head = addXNode(head, i);
    }

    printX(head);
}

int main() {
    test_xor();
}
