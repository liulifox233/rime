# ChatGPT 生成

# 从文件读取数据
input_filename = "input.txt"  # 输入文件名
output_filename = "output_dict.yml"  # 输出文件名

# 从文件读取输入数据
def read_input_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

# 解析输入数据
def parse_to_rime_dict(input_data):
    lines = input_data.strip().split("\n")
    rime_dict = []
    current_category = None

    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            # 保存分类作为注释
            current_category = line[1:].strip()
            rime_dict.append(f"# {current_category}")
        elif line:
            try:
                # 将键值对提取出来
                key, emoji = line.split(maxsplit=1)
                rime_dict.append(f"{emoji.strip()}	{key.strip()}")
            except ValueError:
                print(f"警告: 跳过无法解析的行: {line}")

    return rime_dict

# 生成 Rime 格式词典
def generate_rime_dict(rime_dict_lines, output_filename):
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write("---\n")
        file.write("name: nmbxd\n")
        file.write("version: \"1.2\"\n")
        file.write("sort: by_weight\n")
        file.write("use_preset_vocabulary: false\n")
        file.write("...\n\n")

        for line in rime_dict_lines:
            file.write(line + "\n")

# 从文件读取并执行转换
input_data = read_input_file(input_filename)
rime_dict_lines = parse_to_rime_dict(input_data)
generate_rime_dict(rime_dict_lines, output_filename)

print(f"Rime 词典文件已生成: {output_filename}")
