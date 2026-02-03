

def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print("文件写入成功！")
    except Exception as e:
        print(f"写入文件时发生错误: {e}")


write_to_file('output.txt', 'Hello, this is a test content.')
