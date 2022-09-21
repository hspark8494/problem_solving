//Q12915 문자열 내 마음대로 정렬하기
//https://school.programmers.co.kr/learn/courses/30/lessons/12915?language=java
import java.util.Arrays;

class Q12915 {
    public String[] solution(String[] strings, int n) {
    	Arrays.sort(strings, (o1, o2) -> {
    		String s1 = (String)o1;
    		String s2 = (String)o2;
    		
    		return (s1.charAt(n)+s1).compareTo(s2.charAt(n)+s2);
    	});
    	
        return strings;
    }
}