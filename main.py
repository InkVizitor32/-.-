a = ['sds', '3543654', '!!!', '!a', 'wec',
     '4543574357345', 'w243ec', ':)', '2656']

l = []
for i in a:
    if len(i) <= 3:
        l.append(i)

print(l)
