/**
 * Done by:
 * Student Name: Svitlichnyi Dmitro
 * Student Group: 123
 * Lab 2.5
 */
#include <iostream>
using std::cin, std::cout;
struct Node
{
    int data;
    Node *next;
};

inline void addToFront(Node **head, int value)
{
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = *head;
    *head = newNode;
}

inline void removeFromFront(Node **head)
{
    if (*head != nullptr)
    {
        Node *temp = *head;
        *head = (*head)->next;
        delete temp;
    }
}

inline void AddToEnd(Node **head, int value)
{
    Node *newNode = new Node;
    newNode->data = value;
    newNode->next = nullptr;
    if (*head == nullptr)
    {
        *head = newNode;
    }
    else
    {
        Node *current = *head;
        while (current->next != nullptr)
        {
            current = current->next;
        }
        current->next = newNode;
    }
}

inline void RemoveFromEnd(Node **head)
{
    if (*head == nullptr)
        return;

    if ((*head)->next == nullptr)
    {
        delete *head;
        *head = nullptr;
    }
    else
    {
        Node *current = *head;
        while (current->next->next != nullptr)
        {
            current = current->next;
        }
        delete current->next;
        current->next = nullptr;
    }
}

inline Node *SearchElement(Node *head, int value)
{
    Node *current = head;
    while (current != nullptr)
    {
        if (current->data == value)
        {
            return current;
        }
        current = current->next;
    }
    return nullptr;
}

inline void ReverseList(Node **head)
{
    Node *prev = nullptr;
    Node *current = *head;
    Node *next = nullptr;

    while (current != nullptr)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

inline void sortList(Node **head)
{
    if (*head == nullptr || (*head)->next == nullptr)
        return;

    bool swapped;
    Node *current;
    Node *last = nullptr;

    do
    {
        swapped = false;
        current = *head;

        while (current->next != last)
        {
            if (current->data > current->next->data)
            {
                std::swap(current->data, current->next->data);
                swapped = true;
            }
            current = current->next;
        }
        last = current;
    } while (swapped);
}

struct DoublyNode
{
    int data;
    DoublyNode *prev;
    DoublyNode *next;
};

inline DoublyNode *toTwoWayList(Node *head)
{
    if (head == nullptr)
        return nullptr;

    DoublyNode *newHead = new DoublyNode;
    newHead->data = head->data;
    newHead->prev = nullptr;
    newHead->next = nullptr;

    DoublyNode *tail = newHead;
    Node *current = head->next;

    tail->next = newHead;
    newHead->prev = tail;

    return newHead;
}

inline void clearList(Node **head)
{
    while (*head != nullptr)
    {
        removeFromFront(head);
    }
}

inline void printList(Node *head)
{
    Node *current = head;
    while (current != nullptr)
    {
        std::cout << current->data << " -> ";
        current = current->next;
    }
    std::cout << "null" << std::endl;
}
int main()
{
    Node *head = nullptr;

    // Adding elements to the list
    addToFront(&head, 10);
    addToFront(&head, 20);
    addToFront(&head, 60);
    AddToEnd(&head, 30);
    AddToEnd(&head, 5);
    AddToEnd(&head, 34);

    // Printing the list
    std::cout << "List after adding elements: ";
    printList(head);

    // Removing an element from the front and end
    removeFromFront(&head);
    RemoveFromEnd(&head);
    std::cout << "List after removing an element: ";
    printList(head);

    Node *found = SearchElement(head, 10);
    if (found != nullptr)
    {
        std::cout << "Found element: " << found->data << std::endl;
    }
    else
    {
        std::cout << "There are no such elements" << std::endl;
    }

    ReverseList(&head);
    std::cout << "List after reversing: ";
    printList(head);

    sortList(&head);
    std::cout << "List after sorting: ";
    printList(head);

    DoublyNode *twoWayList = toTwoWayList(head);
    std::cout << "Two way list created.\n";

    // Clearing the list
    clearList(&head);
    printList(head);

    return 0;
}