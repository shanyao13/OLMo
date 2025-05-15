# 基础镜像，选一个干净的 miniconda3
FROM continuumio/miniconda3

# 创建一个工作目录
WORKDIR /workspace

# 拷贝环境文件
COPY olmo_env.yaml .

# 创建 Conda 环境
RUN conda env create -f olmo_env.yaml

# 让之后的所有命令都默认在 olmo 环境里运行
SHELL ["conda", "run", "-n", "olmo", "/bin/bash", "-c"]

# 启动 bash
CMD ["bash"]

