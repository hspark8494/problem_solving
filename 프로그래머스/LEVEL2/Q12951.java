package programmers;

//Q12951 문자열 만들기
//https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=java
class Solution {
    public String solution(String s) {
    	char[] chars = s.toLowerCase().toCharArray();
    	char pre = ' ';
    	for(int i=0; i<chars.length; i++) {
    		if(pre == ' ') chars[i] = Character.toUpperCase(chars[i]);
    		pre = chars[i];
    	}
        return String.valueOf(chars);
    }
}