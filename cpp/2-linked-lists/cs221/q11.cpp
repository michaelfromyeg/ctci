
#include <iostream>
using namespace std;

struct Node { 
    Node* next;
    int data;
};

Node*& find(Node* head, int index) {
    int count = index;
    Node * curr = head;
    while (--count) {
        curr = curr->next;
    }
    return curr->next;
}

void printList(Node* n) 
{ 
    while (n != NULL) { 
        cout << n->data << " -> " << " "; 
        n = n->next; 
    } 
}

int main() {
    cout << endl;
    Node* head = NULL; 
    Node* three = NULL; 
    Node* twelve = NULL; 
    Node* nine = NULL;
    Node* twofive = NULL;
    Node* fourteen = NULL;  

    head = new Node(); 
    three = new Node(); 
    twelve = new Node(); 
    nine = new Node(); 
    twofive = new Node(); 
    fourteen = new Node(); 
    
    head->data = 1;
    head->next = three;

    three->data = 3;
    three->next = twelve;

    twelve->data = 12; 
    twelve->next = nine; 

    nine->data = 9;
    nine->next = twofive; 

    twofive->data = 25;
    twofive->next = fourteen;

    fourteen->data = 14;
    fourteen->next = NULL;

    printList(head);
    cout << endl;
    Node*& ins = find(head, 3);
    Node mynode;
    mynode.data = 225;
    mynode.next = ins->next;
    ins->next = &mynode;

    printList(head);

    return 0;
}


