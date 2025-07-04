import os
import re

# 配置
translated_dir = r"e:/Documents/Work/VSCode/PS4MR/translated/"
raw_dir = r"e:/Documents/Work/VSCode/PS4MR/raw/"

# 获取所有 translated 下的 markdown 文件
md_files = [f for f in os.listdir(translated_dir) if f.lower().endswith('.md')]

for md_file in md_files:
    translated_path = os.path.join(translated_dir, md_file)
    # 获取对应 raw 文件名
    raw_name = md_file.replace('_translated', '')
    raw_path = os.path.join(raw_dir, raw_name)
    if not os.path.exists(raw_path):
        print(f"Raw file not found for {md_file}, skipped.")
        continue

    with open(translated_path, 'r', encoding='utf-8') as f:
        trans_content = f.read()
    with open(raw_path, 'r', encoding='utf-8') as f:
        raw_content = f.read()

    # 提取 translated 文件中的本地图片链接
    trans_pattern = r'!\[]\(([^)]+img\d+\.[a-zA-Z0-9]+)\)'
    trans_links = re.findall(trans_pattern, trans_content)

    # 提取 raw 文件中的网络图片链接
    raw_pattern = r'!\[]\((https://cdn-mineru.openxlab.org.cn/extract/[^)]+)\)'
    raw_links = re.findall(raw_pattern, raw_content)

    if len(trans_links) != len(raw_links):
        print(f"Warning: 图片数量不一致，{md_file} 跳过。({len(trans_links)} vs {len(raw_links)})")
        continue

    # 替换本地链接为网络链接
    for local, net in zip(trans_links, raw_links):
        trans_content = trans_content.replace(local, net)

    # 保存
    with open(translated_path, 'w', encoding='utf-8') as f:
        f.write(trans_content)
    print(f"已替换: {md_file}，共 {len(trans_links)} 个图片链接。")
    input("请检查该文件效果，如有问题请按Ctrl+C终止，按回车继续处理...\n")

print("所有 translated 图片链接已替换为 raw 网络链接！")
