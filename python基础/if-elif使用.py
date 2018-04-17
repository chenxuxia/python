
height=input('请输入身高:')
weight=input('请输入体重:')
bim=weight/pow(height,2)
if bim<18.5:
    print ('过轻')
elif bim<25:
    print('正常')
elif bim<28:
    print('过重')
elif bim<32:
    print('肥胖')
else:
    print('严重肥胖')
