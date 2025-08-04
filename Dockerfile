# Use a Python 3.9 base image on Debian 11 ("bullseye"), which is still supported.
FROM python:3.9-slim-bullseye

# Set the working directory inside the container
WORKDIR /amrlib

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    wget \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy your local project files into the container.
COPY . /amrlib

# Install the Python dependencies, but exclude torch from requirements.txt
# This prevents it from trying to download the huge CUDA files.
RUN sed -i '/torch/d' requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Manually install the CPU-only version of torch
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Install the amrlib package itself.
RUN pip install --no-cache-dir -e .

# --- The Correct Model Installation Steps from the Documentation ---
# Create the data directory
RUN mkdir -p amrlib/data
WORKDIR /amrlib/amrlib/data

# Download and install the parse model (xfm_bart_large)
RUN wget https://github.com/bjascob/amrlib-models/releases/download/parse_xfm_bart_large-v0_1_0/model_parse_xfm_bart_large-v0_1_0.tar.gz && \
    tar -xzvf model_parse_xfm_bart_large-v0_1_0.tar.gz && \
    ln -snf model_parse_xfm_bart_large-v0_1_0 model_stog

# Download and install the generate model (t5wtense)
RUN wget https://github.com/bjascob/amrlib-models/releases/download/model_generate_t5wtense-v0_1_0/model_generate_t5wtense-v0_1_0.tar.gz && \
    tar -xzvf model_generate_t5wtense-v0_1_0.tar.gz && \
    ln -snf model_generate_t5wtense-v0_1_0 model_gtos

# Download the spaCy model
WORKDIR /amrlib
RUN python3 -m spacy download en_core_web_sm

# Set the default command when the container starts.
CMD ["/bin/bash"]