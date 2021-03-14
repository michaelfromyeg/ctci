// A simple CPP program to introduce 
// a linked list 

// #include <bits/stdc++.h> 
#include <iostream>
using namespace std;


class Node { 
public: 
    int data; 
    Node* next; 
}; 


void printList(Node* n) 
{ 
    while (n != NULL) { 
        cout << n->data << " -> " << " "; 
        n = n->next; 
    } 
}

int main() 
{ 
    cout << endl;
    Node* head = NULL; 
    Node* one = NULL; 
    Node* two = NULL; 
    Node* three = NULL; 
  
    head = new Node(); 
    one = new Node(); 
    two = new Node(); 
    three = new Node(); 
  
  
    head->data = 0;
    head->next = one;

    one->data = 1;
    one->next = two;

    two->data = 2; 
    two->next = three; 
 
    three->data = 3;
    three->next = NULL; 

    printList(head);
    cout << endl;
    head->next = two;
    two->next = one;
    one->next = three;

    cout << "After modification: " << endl;

    printList(head);
    cout << endl;
    return 0; 
}
