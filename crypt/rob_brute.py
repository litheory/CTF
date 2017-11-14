#lstr="""synt{RNJVHSU489tuqqqjUS894}"""

#str="-2:dcug86\\ozj\\|r9YJCycY72NYToQFe7QJL;"
str="l1cg{faslaicas1irh3cpb}csis3"

for p in range(127):
    str1 = '\n'
    for i in str:
        temp = chr((ord(i)+p)%127)
        if 32<ord(temp)<127 :
            str1 = str1 + temp 
            feel = 1
        else:
            feel = 0
            break
    if feel == 1:
        print(str1)