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

typedef Bool (*FilterFunc)(Message *message, void *data);

Bool isFailedMessage(Message *message, void *data) {
    return message->status == FAILED; 
}

Bool isMessageFrom(Message *message, void *data) {
    char *sender = (char *) data;  
    return strcmp(message->sender, sender) == 0;
}

void countMessages(Message message[], int N, char username[], int *sent, int *received) {
    *sent = 0;
    *received = 0;

    for (int i = 0; i < N; i++) {    
        if (!strcmp(username, message[i].sender)) (*sent)++;

        for (int j = 0; j < message[i].destinationCount; j++) {
            if (!strcmp(username, message[i].destination[j])) (*received)++;
        }
    }
}

Message **filterMessages(Message* messages[], int N, FilterFunc filter, void *data, int *n) {
    int cont = 0;
    int failed = 0;

    for (int i = 0; i < N; i++) {
        if (messages[i]->status == SENT) {
            if (filter(messages[i],data)) cont ++;
        }
    }
    

    Message **filtMessages = (Message*) malloc(cont * sizeof(Message));
    
    int indx = 0;
    for (int i = 0; i < N; i++) {
        if (messages[i]->status != FAILED){
            if (filter(messages[i], data)) {
            filtMessages[indx++] = messages[i];
            }
        }
    }

    *n = cont;
    return filtMessages;
}

void CountVowels(char array[][30], int* arrInt, int cont) {
    for (int i=0 ; i <5 ; i++) {
            arrInt[i] = 0;
    }
    
    for (int i=0 ; i<cont ; i++) {
        char* texto = array[i];
        printf("%s\n",texto);
        for (int j=0; texto[j] != '\0'; j++) {
            char letra = texto[j];
            switch (letra) {
                case 'a' :
                case 'A' :
                    arrInt[0] ++;
                    break;
                case 'e' :
                case 'E' :
                    arrInt[1] ++;
                    break;
                case 'i' :
                case 'I' :
                    arrInt[2] ++;
                    break;
                case 'o' :
                case 'O' :
                    arrInt[3] ++;
                    break;
                case 'u' :
                case 'U' :
                    arrInt[4] ++;
                    break;
            }
        }
    }
}

int main() {
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
        "Juan"
    };

    Message messages[] = {
        {"Este es el primer mensaje", SENT, "Samuel", 1, {"Anna"}},
        {"Examen Asincrono 1", SENT, "Ramiro", 2, {"Miguel", "Jose"}},
        {"Diseno de Estructura de Datos", SENT, "Miguel", 1, {"Diego"}},
        {"Este es un proyecto de examen", SENT, "Diego", 2, {"Samuel", "Anna"}},
        {"Mi cumple es el jueves", SENT, "Anna", 1, {"Sabina"}},
        {"Hoy es 9 de septiembre de 2024", SENT, "Daniele", 2, {"Gigi", "Juan"}},
        {"Estoy en una sala colaborativa", SENT, "Samuel", 1, {"Gigi"}},
        {"Tengo una laptop", SENT, "Anna", 2, {"Diego", "Juan"}},
        {"Profe pongame 10", SENT, "Samuel", 1, {"Profe"}},
        {"Apoco si", SENT, "Jose", 4, {"Ramiro", "Samuel", "Juan", "Sabina"}}
    };

    int nUsers = sizeof(users) / sizeof(users[0]);
    char (*ptrUser)[20] = users;

    Message *msgPointers[10];
    for (int i = 0; i < 10; i++) {
        msgPointers[i] = &messages[i];
    }

    int N = 10;
    for (int i = 0; i < nUsers; i++) {        
        countMessages(messages, N, *(ptrUser + i), &sent, &received);
        printf("%s sent: %d messages\n", *(ptrUser + i), sent);
        printf("%s received: %d messages\n", *(ptrUser + i), received);
        printf("\n");
    }

    int x = 0, failed = 0 , z = 0;
    Message** newmsg = filterMessages(msgPointers, 10, isMessageFrom,"Samuel", &x);

    printf("CORRECT Sent Messages\n");
    for (int i = 0; i < x; i++) {
        printf("Message [%d]: %s\n",i, newmsg[i]->text);
    }
    printf("\n");
    printf("FAILED Messages\n");
    for (int i = 0; i < N; i++) {
        if (messages[i].status == FAILED ) printf("Message Failed [%d]: %s\n",i, messages[i].text);
    }
    printf("\n");
    
    char TextArray[][30] = {
        "Hola", 
        "Como", 
        "Estas",
        "Mi equipo",
        "Es", 
        "Samuel",
        "Pia",
        "Estamos",
        "Haciendo",
        "El",
        "Trabajo"
    };
    
    int IntArray[5];

    int size = sizeof(TextArray) / sizeof(TextArray[0]);
    int SizeInt = sizeof(IntArray) / sizeof(IntArray[0]);
    
    CountVowels(TextArray, IntArray, size);
    
    for (int i=0 ; i<SizeInt ; i++) {
        switch(i){
            case 0 : 
            printf("Number of vowels a %d\n",IntArray[0]);
            break;
            case 1 :
            printf("Number of vowels e %d\n",IntArray[1]);
            break;
            case 2 :
            printf("Number of vowels i %d\n",IntArray[2]);
            break;
            case 3 :
            printf("Number of vowels o %d\n",IntArray[3]);
            break;
            case 4 :
            printf("Number of vowels u %d\n",IntArray[4]);
            break;
        }
    }

    free(newmsg); 

    return 0;
}
