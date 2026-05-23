package lab_1_3;

import java.util.LinkedList;
import java.util.Queue;

class Student {
    private String lastName;
    private String firstName;
    private int course;
    private String studentId;
    private int conferenceCount;
    private int itCertificatesCount;

    public Student(String lastName, String firstName, int course, String studentId, int conferenceCount, int itCertificatesCount) {
        this.lastName = lastName;
        this.firstName = firstName;
        this.course = course;
        this.studentId = studentId;
        this.conferenceCount = conferenceCount;
        this.itCertificatesCount = itCertificatesCount;
    }

    public String getStudentId() {
        return studentId;
    }

    @Override
    public String toString() {
        return String.format("| %-12s | %-10s | %-4d | %-12s | %-16d | %-21d |", 
                lastName, firstName, course, studentId, conferenceCount, itCertificatesCount);
    }
}

class Node {
    Student student;
    Node left;
    Node right;

    public Node(Student student) {
        this.student = student;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    private Node root;

    public BinaryTree() {
        this.root = null;
    }

    public void insert(Student student) {
        root = insertRec(root, student);
    }

    private Node insertRec(Node root, Student student) {
        if (root == null) {
            root = new Node(student);
            return root;
        }

        if (student.getStudentId().compareTo(root.student.getStudentId()) < 0) {
            root.left = insertRec(root.left, student);
        } else if (student.getStudentId().compareTo(root.student.getStudentId()) > 0) {
            root.right = insertRec(root.right, student);
        }

        return root;
    }

    public void printBreadthFirst() {
        if (root == null) {
            System.out.println("Дерево порожнє");
            return;
        }

        System.out.println(new String(new char[93]).replace("\0", "-"));
        System.out.printf("| %-12s | %-10s | %-4s | %-12s | %-16s | %-21s |\n", 
                "Прізвище", "Ім'я", "Курс", "Студ. квиток", "Участь у конф.", "IT Сертифікати");
        System.out.println(new String(new char[93]).replace("\0", "-"));

        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            Node tempNode = queue.poll();
            System.out.println(tempNode.student);

            if (tempNode.left != null) {
                queue.add(tempNode.left);
            }

            if (tempNode.right != null) {
                queue.add(tempNode.right);
            }
        }
        System.out.println(new String(new char[93]).replace("\0", "-"));
    }
}

public class Main {
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();

        tree.insert(new Student("Шевченко", "Ігор", 3, "KB10293847", 2, 3));
        tree.insert(new Student("Коваленко", "Ганна", 2, "KB01928374", 4, 1));
        tree.insert(new Student("Мельник", "Олег", 4, "KB56473829", 1, 5));
        tree.insert(new Student("Бондар", "Марія", 1, "KB00112233", 0, 2));
        tree.insert(new Student("Ткаченко", "Артем", 3, "KB44556677", 3, 0));

        tree.printBreadthFirst();
    }
}