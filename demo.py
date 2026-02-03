# 请你编写代码，读取文件

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("文件读取成功！")
            return content
    except FileNotFoundError:
        return "文件未找到，请检查路径是否正确。"
    except Exception as e:
        return f"发生错误：{e}"


# 示例用法
if __name__ == "__main__":
    file_path = 'test.txt'  # 替换为你的文件路径
    content = read_file(file_path)
    print(content)
