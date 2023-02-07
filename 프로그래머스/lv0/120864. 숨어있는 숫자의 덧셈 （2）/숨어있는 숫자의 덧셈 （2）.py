import re
solution = lambda x: sum(map(int, filter(str.isnumeric, re.split("([aA-zZ])+", x))))