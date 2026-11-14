
#include <stdio.h>
#define SIZE 5

int dq[SIZE];
int front = -1, rear = -1;

int isFull() {
    return (front == 0 && rear == SIZE - 1) || (front == rear + 1);
}

int isEmpty() {
    return front == -1;
}

/* a) Front insertion */
void insertFront(int x) {
    if (isFull()) { printf("Overflow\n"); return; }
    if (isEmpty()) front = rear = 0;
    else if (front == 0) front = SIZE - 1;
    else front--;
    dq[front] = x;
}

/* b) Rear insertion */
void insertRear(int x) {
    if (isFull()) { printf("Overflow\n"); return; }
    if (isEmpty()) front = rear = 0;
    else if (rear == SIZE - 1) rear = 0;
    else rear++;
    dq[rear] = x;
}

/* c) Front deletion */
void deleteFront() {
    if (isEmpty()) { printf("Underflow\n"); return; }
    printf("Deleted %d\n", dq[front]);
    if (front == rear) front = rear = -1;
    else if (front == SIZE - 1) front = 0;
    else front++;
}

/* d) Rear deletion */
void deleteRear() {
    if (isEmpty()) { printf("Underflow\n"); return; }
    printf("Deleted %d\n", dq[rear]);
    if (front == rear) front = rear = -1;
    else if (rear == 0) rear = SIZE - 1;
    else rear--;
}

void display() {
    if (isEmpty()) { printf("Deque is empty\n"); return; }
    int i = front;
    printf("Deque: ");
    while (1) {
        printf("%d ", dq[i]);
        if (i == rear) break;
        i = (i + 1) % SIZE;
    }
    printf("\n");
}

int main() {
    insertRear(10);
    insertRear(20);
    insertFront(5);
    display();
    deleteFront();
    display();
    deleteRear();
    display();
    return 0;
}