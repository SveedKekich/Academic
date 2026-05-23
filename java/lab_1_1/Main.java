package lab_1_1;


class DoublyLinkedList {
    class Node {
        int data;
        Node prev;
        Node next;

        Node(int data) {
            this.data = data;
        }
    }

    private Node head;
    private Node tail;

    public void add(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = tail = newNode;
        } else {
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
    }

    public void remove(int data) {
        Node current = head;

        while (current != null) {
            if (current.data == data) {

                if (current == head) {
                    head = current.next;
                    if (head != null) {
                        head.prev = null;
                    }
                }

                else if (current == tail) {
                    tail = current.prev;
                    tail.next = null;
                }

                else {
                    current.prev.next = current.next;
                    current.next.prev = current.prev;
                }

                return;
            }

            current = current.next;
        }
    }

    public void printList() {
        Node current = head;

        if (current == null) {
            System.out.println("Список порожній");
            return;
        }

        System.out.print("Вміст списку: ");

        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }

        System.out.println();
    }
}

public class Main {
    public static void main(String[] args) {

        DoublyLinkedList list = new DoublyLinkedList();

        list.add(10);
        list.add(20);
        list.add(30);
        list.add(40);
        list.add(50);

        System.out.println("Після додавання елементів:");
        list.printList();

        list.remove(20);
        list.remove(40);

        System.out.println("Після видалення елементів:");
        list.printList();
    }
}