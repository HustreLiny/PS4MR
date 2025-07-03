import os
import re

# 1. 指定 translated 目录
ROOT = r"e:\Documents\Work\VSCode\PS4MR\translated"

# 匹配 Markdown 标题
heading_re = re.compile(r'^(#{1,6})\s+(.*)$')

def process_file(path):
    # 读取所有行，不保留末尾换行符
    lines = open(path, encoding='utf-8').read().splitlines()
    merged = []
    i = 0
    while i < len(lines):
        m1 = heading_re.match(lines[i])
        if m1:
            # 跳过空行，寻找下一个非空行
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            # 如果下一个非空行也是同级标题，就合并
            if j < len(lines):
                m2 = heading_re.match(lines[j])
                if m2 and m1.group(1) == m2.group(1):
                    # 合并成一行：中文标题  两个空格  英文标题
                    merged.append(f"{m1.group(1)} {m1.group(2)}  {m2.group(2)}")
                    i = j + 1
                    continue
        # 否则正常保留此行
        merged.append(lines[i])
        i += 1

    # 2. 确保每行末尾都有两个空格（排除纯空行）
    out = []
    for ln in merged:
        if ln.strip() != "" and not ln.endswith("  "):
            ln = ln + "  "
        out.append(ln)

    # 写回文件，末尾加一个换行
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

if __name__ == "__main__":
    for dirpath, _, filenames in os.walk(ROOT):
        for fn in filenames:
            if fn.endswith(".md"):
                process_file(os.path.join(dirpath, fn))