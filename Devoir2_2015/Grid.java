public class Grid {
    private int SIZE = 12;

    private Cell head;
    private Cell tail;
    private Cell empty;

    private static class Cell {
        int value;
        Cell next;
        Cell prev;
        Cell up;
        Cell down;

        Cell(int value) {
            this.value = value;
        }
    }
    
    public Grid() {
        head = new Cell(0);
        Cell current = head;
    
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (i == 0 && j == 0) {
                    continue;
                }
    
                int value = i * SIZE + j;
                current.next = new Cell(value);
                current.next.prev = current;
                current = current.next;
    
                if (j == SIZE - 1) {
                    current.next = null;
                }
            }
    
            if (i < SIZE - 1) {
                Cell nextRow = new Cell(0);
                current.down = nextRow;
                nextRow.up = current;
    
                current = nextRow;
                tail = nextRow;
    
                if (i == 0) {
                    head.down = current;
                    current.up = head;
                }
    
                for (int j = 1; j < SIZE; j++) {
                    int value = i * SIZE + j;
                    current.next = new Cell(value);
                    current.next.prev = current;
                    current = current.next;
    
                    if (j == SIZE - 1) {
                        current.next = null;
                    }
    
                    current.up = current.prev.up.next;
                    current.prev.up.next.down = current;
                }
            }
        }
    
        current = head;
        while (current.value != 0) {
            current = current.next;
        }
        empty = current;
    }

    public boolean move(Cell box) {
        if (box == null || box.value == -1) {
            return false;
        }
        
        if ((empty.next == box || empty.prev == box ||
             empty.up == box || empty.down == box)) {
            // Echanger la cellule actuelle et la cellule vide
            int temp = box.value;
            box.value = empty.value;
            empty.value = temp;
    
            // Mettre a jour la cellule vide
            empty = box;
    
            return true;
        }
    
        return false;
    }
    
    public boolean check_complete() {
        Cell actuel = head;
        int expectedValue = 1;

        while (actuel.value != -1) {
            if (actuel.value != expectedValue) {
                if (actuel.value == 0 && expectedValue == SIZE * SIZE) {
                    return true;
                } else {
                    return false;
                }
            }

            expectedValue++;
            actuel = actuel.next;
        }

        return true;
    }

    public void solve_game(){
        // TODO
    }
}