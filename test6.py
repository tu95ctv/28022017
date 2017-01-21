import re
rs = re.search('^(.*?) ','4G_PQU048A_KGG (B? AT)')
if rs:
    print rs.group(1)