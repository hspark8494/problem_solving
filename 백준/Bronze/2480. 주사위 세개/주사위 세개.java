import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] input = sc.nextLine().split(" ");
		int[] arr = Arrays.stream(input).mapToInt(Integer::parseInt).toArray();
		int result = 0;
		Arrays.sort(arr);

		if(arr[0] == arr[2]) {
			result = arr[0] * 1000 + 10000;
		}else if(arr[1] == arr[0] || arr[1] == arr[2]) {
			result = arr[1] * 100 + 1000;
		}else {
			result = arr[2] * 100;
		}
		
		System.out.println(result);
		
		sc.close();
		
	}
}