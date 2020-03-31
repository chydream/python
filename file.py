# open() close()
f = open('tool.py')
dir(f)
help(f)
print(f)
f.close()

# 自动关闭
with open('base.py') as b:
    print(123)
