class Solution {
    public int fib(int n) {
        int previous = 0;
        int current = 1;
      
        while (n-- > 0) {
            int next = previous + current;
            previous = current;
            current = next;
        }
      
        return previous;
    }
}