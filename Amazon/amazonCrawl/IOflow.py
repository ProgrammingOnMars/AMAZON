


'''
写入文件内容
'''

# 读取搜索关键词txt
def read_info():
    content = []
    f = open(r'关键词.txt')
    line = f.readline()
    while line:
        # print(line, end='')
        line = f.readline()
        content.append(line)
    f.close()
    return content



# 写入txt文件
def finally_write_txt(path, content):
    f = open(r'符合条件的{}.txt'.format(path), 'a', encoding='utf8')
    f.write(content)
    f.write("\n")
    f.close()

# 写入txt文件
def new_finally_write_txt(path ,content):
    f = open(r'符合条件的camera.txt', 'a', encoding='utf8')
    f.write(content)
    f.write("\n")
    f.close()

# 写入txt文件
def write_txt(content):
    f = open(r'符合条件的personal computer.txt', 'a', encoding='utf8')
    f.write(content)
    f.write("\n")
    f.close()


# 日志
def log(content):
    f = open(r'personal computer-Journal.txt', 'a', encoding='utf8')
    f.write(content)
    f.write("\n")
    f.close()