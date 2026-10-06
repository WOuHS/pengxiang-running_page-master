import os

GPX_FOLDER = r"D:\0\Projects\runningpage2026code\GPX_OUT"
gpx_files = [f for f in os.listdir(GPX_FOLDER) if f.lower().endswith(".gpx")]

for fname in gpx_files:
    full_path = os.path.join(GPX_FOLDER, fname)
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    # 只替换第一个 <trk>，改成带type="Run"
    if "<trk>" in content:
        # 检查是否已经存在type属性
        trk_start_pos = content.find("<trk>")
        fragment = content[trk_start_pos:trk_start_pos+20]
        if 'type=' not in fragment:
            new_content = content.replace("<trk>", '<trk type="Run">', 1)
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ {fname} 已添加 type=\"Run\"")
        else:
            print(f"⏭️ {fname} 已有type，跳过")
    else:
        print(f"❌ {fname} 没有<trk>标签，跳过")
