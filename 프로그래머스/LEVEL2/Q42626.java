package programmers;

// Q42626 더 맵게
// https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=java
import java.util.PriorityQueue;

class Solution {
	public int solution(int[] scoville, int k) {
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		int result = 0;
		for (int i : scoville) {
			pq.offer(i);
		}
		while (pq.peek() < k) {
			Integer a = pq.poll();
			Integer b = pq.poll();
			if (a == null || a <= 0 || b == null) {
				return -1;
			}
			pq.offer(a + b * 2);
			result++;
		}
		return result;
	}
}