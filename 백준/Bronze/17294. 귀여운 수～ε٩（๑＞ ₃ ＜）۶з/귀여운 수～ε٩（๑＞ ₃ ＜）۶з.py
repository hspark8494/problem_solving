l = list(map(int, list(input())))
if len(l)>=2:
	d = l[0]-l[1]
t = True
for i in range(len(l)-1):
	if l[i] - l[i+1] !=d:
		t = False
		break
print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!" if t else "흥칫뿡!! <(￣ ﹌ ￣)>")

