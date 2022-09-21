import java.util.AbstractMap.SimpleEntry;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		int total = 0;
		for(int i=0; i<10; i++) {
			int n =sc.nextInt();
			total += n;
			if(map.containsKey(n)) {
				map.put(n, map.get(n)+1); 
			}else {
				map.put(n, 1);
			}
		}
		System.out.println((int)(total/10));
		Entry<Integer, Integer> x = new SimpleEntry<Integer, Integer>(0,0);
		for(Entry<Integer, Integer> e : map.entrySet()) {
			if(e.getValue() > x.getValue()){
				x = e;
			}
		}
		System.out.println(x.getKey());
		sc.close();
	}
}
