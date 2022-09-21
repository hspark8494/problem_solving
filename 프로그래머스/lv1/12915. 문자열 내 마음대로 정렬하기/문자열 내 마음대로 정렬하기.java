import java.util.Arrays;

class Solution {
    public String[] solution(String[] strings, int n) {
    	Arrays.sort(strings, (o1, o2) -> {
    		String s1 = (String)o1;
    		String s2 = (String)o2;
    		
    		return (s1.charAt(n)+s1).compareTo(s2.charAt(n)+s2);
    	});
    	
        return strings;
    }
}