print((r:=__import__("functools").reduce,f:=__import__("re").findall,r(lambda a,n:(False,a[1],a[2])if n=="don't()"else(True,a[1],a[2])if n=="do()"else(a[0],a[1]+(j:=r(lambda a,b:int(a)*int(b),f(r"mul\((\d+),(\d+)\)",n)[0])),a[2]+(j if a[0] else 0)),f(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))","".join(open("input.txt").readlines())),(True,0,0)))[2:][0][1:])