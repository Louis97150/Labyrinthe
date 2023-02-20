public class Node {
    private int value;
    private Node next = null;

    public Node(int value){
        this.value = value;
    }

    public Node(int value, Node next){
        this.value = value;
        this.next = next;
    }

    public void addValue(int value){
        this.next = new Node(value, this.next);
    }

    public void addNode(Node next){
        next.next = this.next;
        this.next = next;
    }

    public void removeLast(){
        if (this.next == null) {
            return;
        }
        Node current = this;
        while (current.next.next != null) {
            current = current.next;
        }
        current.next = null;
    }

    public void removeValue(int value){
        Node current = this;
        while (current.next != null) {
            if (current.next.value == value) {
                current.next = current.next.next;
                break;
            }
            current = current.next;
        }
    }

    public int length_iteratif(){
        int compteur = 0;
        Node current = this;
        while (current.next != null) {
            compteur++;
            current = current.next;
        }
        return compteur;
    }

    public int length_recurssion(Node node){
        if (node.next == null) {
            return 0;
        }
        return 1 + length_recurssion(node.next);
    }

    public int returnNlast(int nLast){
        int length = this.length_iteratif();
        int targetIndex = length - nLast;
        Node current = this;
        for (int i = 0; i < targetIndex; i++) {
            current = current.next;
        }
        return current.value;
    }

    public void addValue_ordered(int value){
        Node current = this;
        while (current.next != null && current.next.value < value) {
            current = current.next;
        }
        current.next = new Node(value, current.next);
    }

    public void insertSort(){
        Node resultat = null;
        Node current = this;
        while (current != null) {
            Node next = current.next;
            if (resultat == null || resultat.value >= current.value) {
                current.next = resultat;
                resultat = current;
            } else {
                Node currentResult = resultat;
                while (currentResult.next != null &&
                        currentResult.next.value < current.value) {
                    currentResult = currentResult.next;
                }
                current.next = currentResult.next;
                currentResult.next = current;
            }
            current = next;
        }
        this.next = resultat.next;
    }
}
