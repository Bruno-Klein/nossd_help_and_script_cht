import os


# By Bruno Klein
# brunoklein@protonmail.com
# A Python script to count how many plots in each level with a specific path, modify this path in the script before running: directory_to_scan = "/path/to/your/directory"
# 一個Python腳本，用於統計特定路徑下每個層級中有多少個圖，運行前在腳本中修改此路徑：directory_to_scan = "/path/to/your/directory"

# Specify the directory to scan
# 指定掃描目錄
directory_to_scan = "/path/to/your/directory"

# Define size ranges in bytes with ±0.5 GiB tolerance
# 定義大小範圍（以位元組為單位），容差為 ±0.5 GiB
size_ranges = {
    "C10": ((70.8 - 0.5) * 1024**3, (70.8 + 0.5) * 1024**3),
    "C11": ((64.9 - 0.5) * 1024**3, (64.9 + 0.5) * 1024**3),
    "C12": ((60.8 - 0.5) * 1024**3, (60.8 + 0.5) * 1024**3),
    "C13": ((57.3 - 0.5) * 1024**3, (57.3 + 0.5) * 1024**3),
    "C14": ((53.8 - 0.5) * 1024**3, (53.8 + 0.5) * 1024**3),
    "C15": ((50.3 - 0.5) * 1024**3, (50.3 + 0.5) * 1024**3),
    "C30": ((47.51 - 0.5) * 1024**3, (47.51 + 0.5) * 1024**3),
    "C31": ((44.93 - 0.5) * 1024**3, (44.93 + 0.5) * 1024**3),
    "C32": ((42.30 - 0.5) * 1024**3, (42.30 + 0.5) * 1024**3),
    "C33": ((39.65 - 0.5) * 1024**3, (39.65 + 0.5) * 1024**3),
    "C34": ((36.96 - 0.5) * 1024**3, (36.96 + 0.5) * 1024**3),
    "C35": ((34.36 - 0.5) * 1024**3, (34.36 + 0.5) * 1024**3),
    "C36": ((31.71 - 0.5) * 1024**3, (31.71 + 0.5) * 1024**3),
    "C37": ((28.96 - 0.5) * 1024**3, (28.96 + 0.5) * 1024**3),
    "C38": ((26.16 - 0.5) * 1024**3, (26.16 + 0.5) * 1024**3),
}

# Function to count files in size ranges
# 計算檔案大小範圍內的函數

def count_files_in_size_ranges(directory):
    total_counts = {key: 0 for key in size_ranges.keys()}

    for subdir, _, files in os.walk(directory):
        subdir_counts = {key: 0 for key in size_ranges.keys()}

        for file in files:
            if not file.endswith('.fpt'):
                continue  # Skip files that do not have the .fpt extension

            file_path = os.path.join(subdir, file)
            try:
                file_size = os.path.getsize(file_path)
                for level, (min_size, max_size) in size_ranges.items():
                    if min_size <= file_size <= max_size:
                        subdir_counts[level] += 1
                        total_counts[level] += 1
                        break
            except OSError:
                print(f"Could not access {file_path}, skipping.")

        # Display results for the current subdirectory
        # 顯示目前子目錄的結果
        print(f"\nIn subdirectory: {subdir}")
        for level, count in subdir_counts.items():
            print(f"{level}: {count} files")

    # Display total results
    # 顯示總結果  
    print("\nTotal results:")
    for level, count in total_counts.items():
        print(f"{level}: {count} files")

# Run the function
# 運行函數
count_files_in_size_ranges(directory_to_scan)
