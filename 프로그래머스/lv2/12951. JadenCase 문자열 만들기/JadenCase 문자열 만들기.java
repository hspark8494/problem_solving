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