import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

	static class Person {
		public int weight;
		public int height;

		Person(int weight, int height) {
			this.weight = weight;
			this.height = height;
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		List<Person> persons = new ArrayList<Person>();

		for (int i = 0; i < n; i++) {
			String[] s = br.readLine().split(" ");
			persons.add(new Person(Integer.parseInt(s[0]), Integer.parseInt(s[1])));
		}
		
		for(Person curr : persons) {
			int result = 1;
			for(Person next: persons) {
				if (curr.weight < next.weight && curr.height < next.height) {
					result++;
				}
			}
			System.out.print(result + " ");
		}

	}
}