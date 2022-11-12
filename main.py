def calculate(s):
    def calc(it):
        def update(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)
            if op == "/": stack.append(float(stack.pop() / v))

        num, stack, sign = 0, [], "+"

        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/":
                update(sign, num)
                num, sign = 0, s[it]
            elif s[it] == ".":
                leading_zero = s[it - 1]
                if int(leading_zero) == 0:
                    num = float((leading_zero + s[it] + s[it + 1]))
                    it += 1
                else:
                    raise Exception('Number should be a valid Float!')
            it += 1
        update(sign, num)
        return sum(stack)

    return calc(0)


resultDict = {}
with open("calc.txt") as file:
    while line := file.readline().rstrip():
        rows = line.split("=")
        result = round(calculate(s=rows[1]), 2)
        resultDict[rows[0]] = result
        print(f"Result for {rows[0]} is {result}")
