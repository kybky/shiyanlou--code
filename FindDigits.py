# 打开并读取文件里的字符串
with open('文件路径') as f:  #这里填写入字符串的文件路径
    s = f.read()
    res = ""
    # 循环字符串里的每个字符，判断是否为数字
    for char in s:
        if char.isdigit():   #isdigit()函数判断是否为数字
            res += char
    print(res)

    #实现一个程序用来提取文件中的字符串中的数字，然后打印输出。