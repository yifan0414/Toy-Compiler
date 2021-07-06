import Parser

global Parser_r1, Parser_r2,temp,four,key, structTable, count, structID, structSet, currentStruct
def goon(a):
    global Parser_r1, Parser_r2, temp
    print()
    print(Parser_r1)
    print(Parser_r2)
    print(temp)
    if a == 1: # 对应非终结符，进入下一个产生式
        b = Parser_r1[0]
        str1 = "fun_" + str(b) + "()"
        return eval(str1)
    else: # 目前匹配的符号，终结符
        temp += [ Parser_r2[0]]
        t = [ Parser_r2[0]]
        Parser_r2 = Parser_r2[1:]
        return  t


def fun_0():
    global Parser_r1, Parser_r2,temp
    Parser_r1 = Parser_r1[1:]
    goon(1) # struct
    goon(1) # 数据类型
    goon(1) # 标识符
    goon(2)
    goon(2)
    goon(2)
    goon(1) # 语句列表
    goon(2)
    temp = temp[:-8]
    temp += []
    return 0

def fun_1():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    goon(2)
    temp = temp[:-3]
    temp += [("语句列表",-1,-1)]
    return 0

def fun_2():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    # print("fun_2:", temp)
    return 0

def fun_3():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    return 0

def fun_4():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    # print("fun_2:", temp)
    return 0

def fun_5():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    temp = temp[:-2]
    temp +=[("语句列表",-1,-1)]
    return 0

def fun_6():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [("语句列表", -1, -1)]
    return 0

def fun_7():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(2)
    temp = temp[:-2]
    temp += [("语句",-1,-1)]
    return 0

def fun_8():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(2)
    temp = temp[:-2]
    temp += [("语句",-1,-1)]
    return 0

def fun_9():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp +=[("语句",-1,-1)]
    return 0

def fun_10():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]
    return 0

def fun_11():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]
    return 0

def fun_12():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]
    return 0
def fun_13():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]
    return 0

def fun_14():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    goon(1)
    temp = temp[:-3]
    temp += [("声明语句",-1,-1)]
    return 0

def fun_15():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("声明语句2",-1,-1)]
    return 0

def fun_16():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    temp = temp[:-2]
    temp += [("声明语句3",-1,-1)]
    return 0

def fun_17():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [("声明语句3", -1, -1)]
    return 0

def fun_18():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    temp [-2] = temp[-1]
    temp = temp[:-1]
    return 0

def fun_19():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    return 0

def fun_20():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [("赋值语句1", -1, -1)]
    return 0

# < 赋值语句2 > ::= <=> <表达式>
def fun_21():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    print("---------------", temp)
    if temp[-2][1] == "=":
        print(("=",temp[-1][1],"_",temp[-3][1]))
        four +=[("=",temp[-1][1],"_",temp[-3][1])]
        # 对于a = b + c 来说，temp[-1][1] = b+c, temp[-3][1] = a
    else:
        print(("=", temp[-1][1], "_", temp[-2][1]))
        four += [("=", temp[-1][1], "_", temp[-2][1])]
        # 对于 a = 10来说，temp[-1][1] = 10, temp[-2][1] = a
    temp = temp[:-2]
    temp += [("赋值语句2", -1, -1)]
    return 0

def fun_22():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    print(("+",temp[-2][1],1,temp[-2][1]))
    four += [("+",temp[-2][1],1,temp[-2][1])]
    return 0

def fun_23():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    print(("+",temp[-2][1],1,temp[-2][1]))
    four += [("-",temp[-2][1],1,temp[-2][1])]
    return 0

# < 赋值语句2> ::=<OP><表达式>
def fun_24():
    global Parser_r1, Parser_r2,temp,four,ntemp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    print(("=", 0, "_", "t" + str(ntemp)))
    four += [("=", 0, "_", "t" + str(ntemp))]
    four += [("j","_","_",len(four)+2)]
    print(("=",1,"_","t"+str(ntemp)))
    four +=[("=",1,"_","t"+str(ntemp))]
    temp[-2] =(temp[-1][0],"t"+str(ntemp),-1)
    temp = temp[:-1]
    ntemp +=1
    print(Parser_r1)
    print(Parser_r2)
    print(temp)

    return 0

# <表达式> ::= <左项><运算符1>
def fun_25():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    print("--------------------------------")
    print(temp)
    if temp[-2][1] != "=" and temp[-3][1] != "=":
        print(("j" + str(temp[-2][1]), temp[-3][1], temp[-1][1], len(four) + 3))
        four += [("j" + str(temp[-2][1]), temp[-3][1], temp[-1][1], len(four) + 3)]
    elif temp[-2][1] != "=" :
        if temp[-3][1] != "=":
            print((str(temp[-3][1]), temp[-2][1], temp[-1][1], len(four) + 3))
            four += [(str(temp[-3][1]), temp[-2][1], temp[-1][1], len(four) + 3)]

    print(temp)
    temp[-2] = temp[-1]
    temp = temp[:-1]
    return 0

# <运算符1>::=<运算符><右项>
def fun_26():
    global Parser_r1, Parser_r2, temp ,ntemp ,four
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    print((temp[-2][1],temp[-3][1],temp[-1][1],"t"+str(ntemp)))
    four +=[(temp[-2][1],temp[-3][1],temp[-1][1],"t"+str(ntemp))]
    temp = temp[:-2]
    temp += [(temp[-1][0], "t"+str(ntemp), temp[-1][2])]
    ntemp +=1
    return 0

def fun_27():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    return 0

def fun_28():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    return  0

def fun_29():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    return 0

def fun_30():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    temp[-2] = temp[-1]
    temp = temp[:-1]
    return 0

def fun_31():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [temp[-1]]
    return 0

def fun_32():
    global Parser_r1, Parser_r2, temp,four,ntemp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    print((temp[-2][1],temp[-3][1],temp[-1][1],"t"+str(ntemp)))
    four+=[(temp[-2][1],temp[-3][1],temp[-1][1],"t"+str(ntemp))]
    temp = temp[:-2]
    temp += [(temp[-1][0],"t"+str(ntemp), temp[-1][2])]
    ntemp += 1
    return 0

def fun_33():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [("右项", -1, -1)]
    return 0

def fun_34():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    t = goon(2)
    return t


def fun_35():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    return 0

def fun_36():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    return 0

# < 条件语句 > ::= <if ><(> <条件式> <)><{> < 语句列表 ><}><条件语句2>
def fun_37():
    global Parser_r1, Parser_r2, temp, ntemp, four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(2)
    goon(1)
    print(("j==", temp[-1][1], 0, "to"))
    four += [("j==", temp[-1][1], 0, "to")]
    k = len(four)
    goon(2)
    goon(2)
    goon(1)
    four += [("j","_","_","to")]
    four[k - 1] = (four[k-1][0], four[k-1][1], four[k-1][2], len(four))
    k = len(four)
    goon(2)
    goon(1)
    four[k - 1] = (four[k - 1][0], four[k - 1][1], four[k - 1][2], len(four))
    temp = temp[:-8]
    temp += [("条件语句",1,-1)]
    return 0

def fun_38():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    temp += [temp[-1]]
    return 0

# < 条件语句2 > ::= <else> <{>< 语句列表 ><}>
def fun_39():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    temp = temp[:-4]
    temp+=[("条件语句2",-1,-1)]
    return 0

def fun_40():
    global Parser_r1, Parser_r2, temp, ntemp, four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    print(("!",temp[-1][1],"_",temp[-1][1]))
    four +=[("!",temp[-1][1],"_",temp[-1][1])]
    temp [-2] = temp[-1]
    temp =temp[:-1]
    return 0

def fun_41():
    global Parser_r1, Parser_r2, temp, ntemp, four
    Parser_r1 = Parser_r1[1:]
    goon(1)
    return 0
# < for循环 > ::= <for><(> <赋值语句><;><条件式> <;><赋值语句> <)><{>< 语句列表 ><}>
def fun_42():
    global Parser_r1, Parser_r2, temp, ntemp, four
    Parser_r1 = Parser_r1[1:]
    n_start_for = len(four)
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    goon(1)
    print(("j==",temp[-1][1],0,""))
    four += [("j==",temp[-1][1],0,"")]
    k=len(four)
    goon(2)
    goon(1)
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    four+=[("j","_","_",n_start_for)]
    four[k - 1] = (four[k - 1][0], four[k - 1][1], four[k - 1][2], len(four))
    temp = temp[:-11]
    temp += [("for循环", -1, -1)]
    return 0

# < while循环 > ::= <while> <( ><条件式> <)> <{>< 语句列表 ><}>
def fun_43():
    global Parser_r1, Parser_r2, temp, ntemp, four
    Parser_r1 = Parser_r1[1:]
    n_start_for = len(four)
    goon(2)
    goon(2)
    goon(1)
    print(("j==", temp[-1][1], 0, ""))
    four += [("j==", temp[-1][1], 0, "")] # 这里写如果为假的跳转四元式，跳转标号暂定
    k = len(four)
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    four += [("j", "_", "_", n_start_for)]
    # 这里写之前为假的跳转四元式的跳转标号
    four[k - 1] = (four[k - 1][0], four[k - 1][1], four[k - 1][2], len(four))
    temp = temp[:-7]
    temp += [("while循环", -1, -1)]

def fun_44():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(2)
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    goon(2)
    four+=[("SCANF",temp[-3][1],"_","_")]
    temp=temp[:-7]
    return 0

def fun_45():
    global Parser_r1, Parser_r2, temp,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(2)
    goon(2)
    goon(2)
    goon(1)
    goon(2)
    goon(2)
    four+=[("PRINT",temp[-3][1],"_","_")]
    temp=temp[:-6]
    return  0

def fun_46():
    global Parser_r1, Parser_r2, temp, four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(1)
    temp [-2] =temp [-1]
    temp=temp[:-1]
    temp[-1] = [temp[-1][0],-temp[-1][1],temp[-1][2]]
    return 0
def fun_47():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]
    return 0
def fun_48():
    global Parser_r1, Parser_r2, temp, four
    Parser_r1 = Parser_r1[1:]
    n_start_for = len(four)
    goon(2)     # do
    goon(2)     # {
    goon(1)     # 语句列表
    goon(2)     # }
    goon(2)     # while
    goon(2)     # {
    goon(1)     # 条件式
    print(("j==", temp[-1][1], 1, ""))
    four += [("j==", temp[-1][1], 1, n_start_for)]  # 这里写如果为真的跳转四元式，跳转标号暂定
    goon(2)     # }
    goon(2)     # ;
    temp = temp[:-9]
    temp += [("dowhile", -1, -1)]
def fun_49():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]
def fun_50():
    global Parser_r1, Parser_r2, temp, key ,four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(2)
    key = Parser_r2[0][1]
    goon(1)
    goon(2)
    goon(2)
    goon(1) # case 语句
    goon(2)
    # 回填出口，
    l = len(four)
    for i in range(l):
        if four[i][3] == "to": # break
            four[i] = [four[i][0], four[i][1],four[i][2], l]
    temp = temp[:-7]
    temp += [("switch语句", -1, -1)]
def fun_51():
    global Parser_r1, Parser_r2, temp, four, key
    Parser_r1 = Parser_r1[1:]
    goon(2)
    const = Parser_r2[0][1] # 常量
    goon(1)
    print(("j!=", key, const, "to"))
    four += [("j!=", key, const, "to")]
    k = len(four)
    goon(2) # :
    goon(1) # 语句列表
    # 寻找j!=在四元式中的位置
    four[k - 1] = (four[k - 1][0], four[k - 1][1], four[k - 1][2], len(four))
    goon(1)
def fun_52():
    global Parser_r1, Parser_r2, temp, four
    Parser_r1 = Parser_r1[1:]

def fun_53():
    global Parser_r1, Parser_r2, temp, four
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(2)
    four += [("j", "_", "_", "to")]
    temp = temp[:-2]
    temp += [("break语句",-1,-1)]
def fun_54():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]
    return 0
def fun_55():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
    temp = temp[:-1]

# <struct定义语句> ::= <struct> <structID> <{> <struct变量定义> <}> <;>
def fun_56():
    global Parser_r1, Parser_r2, temp, structSet
    Parser_r1 = Parser_r1[1:]
    goon(2)
    goon(2)
    structSet += [temp[-1][1]] # 多个结构体的数据类型
    goon(2)
    goon(1) # 语句列表
    goon(2)
    goon(2)
    temp = temp[:-6]
    temp += [("struct定义语句", -1, -1)]
    return 0
# < 语句 > ::= <struct声明语句>
def fun_57():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(1)
    temp = temp[:-1]
    temp += [("语句", -1, -1)]

# <struct声明语句> ::= <structID> <标识符> <=> <{> <struct常量> <}> <;>
def fun_58():
    global Parser_r1, Parser_r2, temp, four, structID, count, currentStruct
    Parser_r1 = Parser_r1[1:]
    goon(2) # structID
    currentStruct = temp[-1][1]
    goon(1) # 标识符
    structID = temp[-1][1] # 这里保存标识符
    goon(2) # =
    goon(2) # {
    count = 0
    goon(1) # <struct常量>
    goon(2) # }
    goon(2) # ;
    temp = temp[:-7]
    temp += [("struct声明语句", -1, -1)]
# < 数据类型 >::= <char*>
def fun_59():
    global Parser_r1, Parser_r2, temp
    Parser_r1 = Parser_r1[1:]
    goon(2)
# <struct变量定义> ::= <数据类型> <标识符> <;> <struct变量定义>
def fun_60():
    global Parser_r1, Parser_r2, temp, structTable, structSet
    Parser_r1 = Parser_r1[1:]
    goon(1)
    goon(1)
    # structTable[temp[-1][1]] = temp[-2][0]
    if structSet[-1] in structTable.keys():
        structTable[structSet[-1]] += [temp[-1][1]]
    else:
        structTable[structSet[-1]] = [temp[-1][1]]
    goon(2)
    goon(1)
    temp = temp[:-4]

# <struct变量定义> ::= <空>
def fun_61():
    global Parser_r1, Parser_r2, temp, structTable
    Parser_r1 = Parser_r1[1:]

# < struct常量> ::= <常量> <struct分割符号> <struct常量>
def fun_62():
    global Parser_r1, Parser_r2, temp, structTable, four, count, structID, currentStruct
    Parser_r1 = Parser_r1[1:]
    # k = ""
    # for i in range(temp):
    #     if temp[i][0] == "structID":
    #         k = temp[i + 1][1]
    goon(1)
    if temp[-1][0] == "STRING":
        four += [('=', temp[-1][1], "常量", structID + structTable[currentStruct][count])]
    else:
        four += [('=', temp[-1][1], "_", structID + structTable[currentStruct][count])]
    count = count + 1
    goon(1)
    goon(1)
# < struct常量> ::= <空>
def fun_63():
    global Parser_r1, Parser_r2, temp, structTable, four, count
    Parser_r1 = Parser_r1[1:]

# <struct分割符号> ::= <,>
def fun_64():
    global Parser_r1, Parser_r2, temp, structTable, four, count
    Parser_r1 = Parser_r1[1:]
    goon(2)

# <struct分割符号> ::= <空>
def fun_65():
    global Parser_r1, Parser_r2, temp, structTable, four, count
    Parser_r1 = Parser_r1[1:]

# <常量> ::= <STRING>
def fun_66():
    global Parser_r1, Parser_r2, temp, structTable, four, count
    Parser_r1 = Parser_r1[1:]
    goon(2)

def main():
    global temp, Parser_r1, Parser_r2 ,ntemp, four, structTable, count, structID, structSet, currentStruct
    structSet = [] # 结构体的数据类型
    currentStruct = ""
    structID = ""
    count = 0
    four ,temp = [],[]
    # structTable = []
    structTable = {"":[]}
    ntemp = 0
    Parser_r1, Parser_r2 = Parser.main()
    print("******************    语 义 分 析  *******************")
    goon(1)

    print(Parser_r1)
    print(Parser_r2)
    print(temp)

    print("********************    四 元 式   *********************")
    count = 0
    for i in four:
        print(count, end="\t")
        print(i)
        count = count + 1
    return four

if __name__ == "__main__":
    main()