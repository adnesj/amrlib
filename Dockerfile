# Use a Python 3.9 base image on Debian 11 ("bullseye"), which is still supported.
FROM python:3.9-slim-bullseye

# Set the working directory inside the container
WORKDIR /amrlib

# Install system dependencies
# This includes git for cloning, wget for downloading, and build-essential for compiling.
RUN apt-get update && apt-get install -y \
    git \
    wget \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy your local project files into the container.
COPY . /amrlib

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the amrlib package itself.
RUN pip install --no-cache-dir -e .

# Manually download and set up the models as per the documentation
RUN mkdir -p amrlib/data
WORKDIR /amrlib/amrlib/data
RUN wget https://github.com/bjascob/amrlib-models/raw/main/v0_3_0/model_parse_xfm_bart_large.tar.gz && \
    tar -xzvf model_parse_xfm_bart_large.tar.gz && \
    ln -snf model_parse_xfm_bart_large model_stog
RUN wget https://github.com/bjascob/amrlib-models/raw/main/v0_3_0/model_generate_t5_small.tar.gz && \
    tar -xzvf model_generate_t5_small.tar.gz && \
    ln -snf model_generate_t5_small model_gtos

# Download the spaCy model
WORKDIR /amrlib
RUN python3 -m spacy download en_core_web_sm

# Set the default command when the container starts.
CMD ["/bin/bash"]