# def trim(s):
#     L=len(s)
#     while L==0:
#         return s      
#     while  s[:1]==' ':
#         s=s[1:]
#         return trim(s) 
#     while s[-1]==' ':
#         s=s[:-1]
#         return trim(s) 
#     return s
# 下面的方法更简洁

def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s



if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


