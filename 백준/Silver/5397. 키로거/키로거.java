import java.io.*;
import java.util.*;

public class Main {
	
	static String find(String str) {
		List<Character> list = new LinkedList<Character>();
		int pos = 0;
		for(char c : str.toCharArray()){
			switch (c) {
				case '<': 
					pos = Integer.max(0, pos-1);
					break;
				case '>':
					pos = Integer.min(pos+1, list.size());
					break;
				case '-':
					if(!list.isEmpty() && pos>0 && pos <=list.size()){
						list.remove(pos-1);
						pos = pos-1;
					}
					break;
				default:
					list.add(pos, c);
					pos++;
			}
		}
		StringBuilder sb = new StringBuilder();
		
		list.forEach(e -> sb.append(e));
		
		return sb.toString();
		
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		for(int i=0; i<n; i++) {
			System.out.println(find(br.readLine()));
		}

	}
}