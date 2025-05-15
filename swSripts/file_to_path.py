import os
import numpy as np

# 遍历inputdir目录下所有的.npy文件，并将它们拼接到指定的outpath，同时打印每个outpath
def concatenate_npy_files(inputdir, outdir):
    # 获取目录下所有.npy文件
    npy_files = [f for f in os.listdir(inputdir) if f.endswith('.npy')]
    
    # 初始化拼接结果为空
    concatenated_data = None

    # 拼接文件
    for npy_file in npy_files:
        # npy_path = os.path.join(inputdir, npy_file)
        # # 读取当前.npy文件
        # data = np.load(npy_path)
        # print(f"data: {data}")
        
        # # 更新拼接结果
        # if concatenated_data is None:
        #     concatenated_data = data
        # else:
        #     concatenated_data = np.concatenate((concatenated_data, data), axis=0)
        
        # # 设置输出路径
        outpath = os.path.join(outdir, npy_file)
        
        # 打印出当前拼接后的输出路径
        print(f"- {outpath}")
    
    # # 将最终拼接后的数据保存到输出路径
    # if concatenated_data is not None:
    #     np.save(outpath, concatenated_data)

# 示例调用
inputdir = '/mnt/zzb/peixunban/zzb6/data/zjf_zsw/tokenizer2'  # 替换为输入目录路径
outdir = '/mnt/zzb6data/peixunban/zzb6/data/zjf_zsw/tokenizer2/'      # 替换为输出目录路径
concatenate_npy_files(inputdir, outdir)
