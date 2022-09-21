import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int result = 0;
        for(int i : scoville) {
            pq.offer(i);
        }
        while(pq.peek()<K) {
            Integer a = pq.poll();
            Integer b = pq.poll();
            if(a == null || a<=0 || b == null) {
                return -1;
            }
            pq.offer(a+b*2);
            result++;
        }

        return result;
    }
}