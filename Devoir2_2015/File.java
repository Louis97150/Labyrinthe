public class File {
    public int[] elements;
    public int start;
    public int end;
    public int size;
    
    public File(int size){
        this.elements = new int[size];
        this.start = 0;
        this.end = 0;
        this.size = size;
    }

    public void push(int element){
        if ((end + 1) % size == start) {
            System.out.println("File is full");
            return;
        }
        elements[end] = element;
        end = (end + 1) % size;
    }

    public int pop(){
        if (start == end) {
            System.out.println("File is empty");
            return -1;
        }
        int result = elements[start];
        start = (start + 1) % size;
        return result;
    }

    public int length(){
        return (end + size - start) % size;
    }

    public void print(){
        int length = length();
        for (int i = 0; i < length; i++) {
            System.out.print(elements[(start + i) % size] + " ");
        }
        System.out.println();
    }

    public boolean search(int value){
        int length = length();
        for (int i = 0; i < length; i++) {
            if (elements[(start + i) % size] == value) {
                return true;
            }
        }
        return false;
    }

    public void remove(int value){
        int length = length();
        for (int i = 0; i < length; i++) {
            if (elements[(start + i) % size] == value) {
                for (int j = i; j < length - 1; j++) {
                    elements[(start + j) % size] = elements[(start + j + 1) % size];
                }
                end = (end + size - 1) % size;
                break;
            }
        }
    }
}
