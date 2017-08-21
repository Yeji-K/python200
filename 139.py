f = open('OZSchedulerMainLog.log','r')
lines = f.readlines()
print(type(lines))
for line_num, line in enumerate(lines):
    print('%d %s'%(line_num,line),end='')
f.close()
