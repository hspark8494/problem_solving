# [Platinum IV] Type Printer - 5467 

[문제 링크](https://www.acmicpc.net/problem/5467) 

### 성능 요약

메모리: 224284 KB, 시간: 3008 ms

### 분류

자료 구조(data_structures), 정렬(sorting), 문자열(string), 트리(trees), 트라이(trie)

### 문제 설명

<p>You need to print N words on a movable type printer. Movable type printers are those old printers that require you to place small metal pieces (each containing a letter) in order to form words. A piece of paper is then pressed against them to print the word. The printer you have allows you to do any of the following operations:</p>

<ul>
	<li>Add a letter to the end of the word currently in the printer.</li>
	<li>Remove the last letter from the end of the word currently in the printer. You are only allowed to do this if there is at least one letter currently in the printer.</li>
	<li>Print the word currently in the printer.</li>
</ul>

<p>Initially, the printer is empty; it contains no metal pieces with letters. At the end of printing, you are allowed to leave some letters in the printer. Also, you are allowed to print the words in any order you like.</p>

<p>As every operation requires time, you want to minimize the total number of operations.</p>

<p>You must write a program that, given the N words you want to print, finds the minimum number of operations needed to print all the words in any order, and outputs one such sequence of operations.  </p>

### 입력 

 <p>Your program must read from the standard input the following data:</p>

<ul>
	<li>Line 1 contains the integer N, the number of words you need to print. (1 ≤ N ≤ 25,000)</li>
	<li>Each of the next N lines contains a word. Each word consists of lower case letters (‘a’ – ‘z’) only and has length between 1 and 20, inclusive. All words will be distinct.</li>
</ul>

### 출력 

 <p>Your program must write to the standard output the following data:</p>

<ul>
	<li>Line 1 must contain an integer M that represents the minimum number of operations required to print the N words.</li>
	<li>Each of the next M lines must contain one character each. These characters describe the sequence of operations done. Each operation must be described as follows:
	<ul>
		<li>Adding a letter is represented by the letter itself in lowercase</li>
		<li>Removing the last letter is represented by the character ‘‐‘ (minus, ASCII code 45)</li>
		<li>Printing the current word is represented by the character ‘P’ (uppercase letter P)</li>
	</ul>
	</li>
</ul>

