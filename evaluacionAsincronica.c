#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef enum {false, true} Bool;
typedef enum {SENT, DELIVERED, FAILED} Status;
typedef struct {
    char text[50];
    Status status;
    char sender[20];
    int destinationCount;
    char *destination[20];
} Message;


typedef void (*FilterFunc)(Message *, void *);

Bool isFailedMessage(Message *message, void *data){
    return message->status = FAILED;
}
Bool isMessageFrom(Message *message, void *data){
    char *sender = (char*) data;
    return strcmp(message->sender, sender) == 0;
}

void countMessages(Message message[], int N, char username[], int *sent, int *received){
    *sent = 0;
    *received = 0;
    Message *ptr = message;

    for (int i = 0; i < N; i++) {    
        if (!strcmp(username, (ptr + i)->sender)) (*sent)++;

        for (int j = 0; j < (ptr + i)->destinationCount; j++) {
            if (!strcmp(username, (ptr + i)->destination[j])) (*received)++;
        }
    }
}

// char** filterMessages(char **messages, int N, FilterFunc filter, void *data, int *n) {

// }
int main(){
    int sent, received;
    char users[][20] = {
        "Samuel",
        "Anna",
        "Ramiro",
        "Daniele",
        "Gigi",
        "Sabina",
        "Diego",
        "Miguel",
        "Profe",
        "Jose",
    };

    Message messages[] = {
        {"Este es el primer mensaje", SENT,  "Samuel", 1, {"Anna"}},
        {"Examen Asincrono 1", SENT,  "Ramiro", 1, {"Miguel"}},
        {"Diseno de Estructura de Datos", SENT,  "Miguel", 1, {"Diego"}},
        {"Este es un proyecto de examen", SENT,  "Diego", 1, {"Samuel"}},
        {"Mi cumple es el jueves", SENT,  "Anna", 1, {"Sabina"}},
        {"Hoy es 9 de septiembre de 2024", SENT,  "Daniele", 1, {"Gigi"}},
        {"Estoy en una sala colaborativa", SENT,  "Samuel", 1, {"Gigi"}},
        {"Tengo una laptop", SENT,  "Anna", 1, {"Diego"}},
        {"Profe pongame 10", SENT,  "Samuel", 1, {"Profe"}},
        {"Apoco si", SENT, "Jose", 1, {"Ramiro"}}
    };

    int nUsers = sizeof(users) / sizeof(users[0]);
    char (*ptrUser)[20] = users;

    int N = 10;
    for (int i = 0; i < nUsers; i++){        
        countMessages(messages, N, *(ptrUser + i), &sent, &received);
        printf("%s sent: %d messages\n", *(ptrUser + i), sent);
        printf("%s received: %d messages\n", *(ptrUser + i), received);
        printf("\n");
    }

    return 0;
}