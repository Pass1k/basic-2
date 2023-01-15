import re

with open('numbers.txt', 'r') as f_in, open('answer.txt', 'w') as f_out:
    f_out.write(str(sum(map(int, re.findall(r"(?ms)\d+", f_in.read())))))
