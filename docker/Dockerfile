# Defines a CUDA-enabled Docker image suitable for installing all dependencies
# to this project.

FROM ghcr.io/allenai/pytorch:2.2.2-cuda11.8-python3.11

# Install necessary utilities
RUN apt-get update && apt-get install -y \
    bash-completion \
    coreutils \
    vim \
    git \
    && rm -rf /var/lib/apt/lists/*

# Enable bash completion and other basic shell features
RUN echo "source /etc/bash_completion" >> ~/.bashrc \
    && echo "alias ll='ls -alF'" >> ~/.bashrc \
    && echo "alias la='ls -A'" >> ~/.bashrc \
    && echo "alias l='ls -CF'" >> ~/.bashrc

# Set working directory
WORKDIR /workspace

# Set CUDA environment variable
ENV CUDA_HOME=/opt/conda

# Use bash as the shell
SHELL ["/bin/bash", "-c"]

# Set the NVIDIA devices visible to Docker
ENV NVIDIA_VISIBLE_DEVICES=all
ENV NVIDIA_DRIVER_CAPABILITIES=compute,utility

# Default command to run bash
ENTRYPOINT ["/bin/bash"]

