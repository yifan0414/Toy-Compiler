import sys
import Semantic_analysis

def trans():
    global four,result ,AX, BX,CX
    result = []
    t = []
    data = [-1]*100

    rule = {
        "j==":["判断","JE"],
        "j>":["判断","JG"],
        "j<=":["判断","JNG"],
        "j<":["判断","JL"],
        "j>=":["判断","JNL"],
        "%":["运算",""],
        "=":["赋值","MOV"],
        "+":["运算","ADD"],
        "-":["运算","SUB"],
        "*":["运算","IMUL"],
        "/":["运算","IDIV"],
        "j":["转移","JMP"],
        "j!=":["判断","JNE"],
        "PRINT":["输出",""],
        "SCANF":["输入",""],

    }
    #print("error : 翻译错误")


    tab =  "        "
    result +=[("include io.inc")]
    result += [(".model small")]
    result += [(".stack")]
    result += [(".data")]
    result += [(tab + "DW 100 DUP(0)")]
    const = []
    temp = []
    for i in range(len(four)):
        if four[i][2] == "常量":
            result += [(four[i][3] + "\tDB " + "'" +four[i][1] + "',13,10,'$'")]
            const += [four[i][3]]
            temp += [i] # 保存所有为常量的四元式
    # 删除为字符串常量的四元式
    # for i in temp:
    #     four.pop(i)
    result += [(".code")]
    result += [(".startup")]

    count = 0
    for i in four:
        print(count, end="\t")
        print(i)
        count = count + 1

    n = 0
    for line in four:
        if rule[line[0]][0] == "判断":
            t += [n + 1]
            t += [line[3]]
        elif rule[line[0]][0] == "转移":
            t += [n + 1]
            t += [line[3]]
        n = n + 1
    t = list(set(t))
    t.sort()
    four_in = {}
    m = 1
    for i in t:
        four_in[i] = "CODE" + str(m)
        m += 1
    print(four_in)

    for i in range(len(four)):
        if i in four_in:
            result +=[four_in[i]+":"]
        if rule[four[i][0]][0] == "判断":
            result+=[tab+"MOV AX,DS:["+str(2*data.index(four[i][1]))+"]"]
            result+=[tab+"MOV BX,"+str(four[i][2])]
            result+=[tab+"CMP AX,BX"]
            result+=[tab+""+rule[four[i][0]][1]+" "+four_in[four[i][3]]]
            result+=[""]
        elif rule[four[i][0]][0] == "赋值":
            if four[i][2] == "常量":
                continue
            elif isinstance(four[i][1],int) or isinstance(four[i][1],float):
                data[data.index(-1)] = four[i][3]
                result += [tab+"MOV AX,"+ str(four[i][1])]
                result += [tab+"MOV DS:["+str(2*data.index(four[i][3]))+"],AX"]
            else:
                data[data.index(-1)] = four[i][3]
                result += [tab+"MOV AX,DS:[" + str(2*data.index(four[i][1]))+"]"]
                result += [tab+"MOV DS:[" + str(2 * data.index(four[i][3])) + "],AX"]
        elif rule[four[i][0]][0] == "运算":
            if isinstance(four[i][1],int) or isinstance(four[i][1],float):
                result += [tab+"MOV AX,"+str(four[i][1])]
            else:
                result += [tab+"MOV AX,DS:[" + str(2*data.index(four[i][1]))+"]"]
            if isinstance(four[i][2],int) or isinstance(four[i][2],float):
                result += [tab+"MOV BX,"+str(four[i][2])]
            else:
                result += [tab+"MOV BX,DS:[" + str(2*data.index(four[i][2]))+"]"]
            if four[i][0] == "+" or four[i][0] == "-":
                result += [tab+rule[four[i][0]][1]+" AX,BX"]
            elif four[i][0] == "*":
                result += [tab+"IMUL BX"]
            elif four[i][0] == "/":
                result += [tab+"IDIV BX"]
            else:
                result +=["----运算符未定义---"]
            data[data.index(-1)] = four[i][3]
            result += [tab+"MOV DS:["+str(2*data.index(four[i][3]))+"],AX"]

        elif rule[four[i][0]][0] == "转移":
            result +=[tab+"JMP "+str(four_in[four[i][3]])]
            result +=[""]
        elif rule[four[i][0]][0] == "输出":
            if four[i][1] in const:
                result += [tab+"MOV DX,OFFSET " + four[i][1]]
                result += [tab+"MOV AH,9"]
                result += [tab+"INT 21H"]
            else:
                # result +=[tab+"MOV AX,DS:["+str(2*data.index(four[i][1])) + "]"]
                # result +=[tab+"ADD AX,30H"]
                # result += [tab + "MOV DX,AX"]
                # result +=[tab+"MOV AH,2"]
                # result +=[tab+"INT 21h"]
                #result += [tab + "mov ax,dx"]
                result += [tab + "MOV AX,DS:[" + str(2 * data.index(four[i][1])) + "]"]
                result += [tab + "call dispuib"]
                result += [tab + "call dispcrlf"]
        elif rule[four[i][0]][0] == "输入":
            result +=[tab+"call readuiw"]
            #result +=[tab+"MOV AH,1"]
            #result +=[tab+"INT 21h"]
            result +=[tab+"MOV DS:["+str(2*data.index(four[i][1])) + "], AX"]
    result += [""]
    result += ["CODE"+str(m)+":"]
    # result += [tab+"MOV AX,4c00"]
    # result += [tab+"INT 21h"]
    # result += ["CODE ENDS"]
    result += [".exit"]
    result += ["END"]
    f = open('asm.txt','w')
    for line in result:
        f.write(line + '\n')

def main():
    global four
    four = Semantic_analysis.main()
    trans()

if __name__ == "__main__":
    main()