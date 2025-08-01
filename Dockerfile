# Use a Python 3.9 base image on Debian 11 ("bullseye"), which is still supported.
FROM python:3.9-slim-bullseye

# Set the working directory inside the container
WORKDIR /amrlib

# Copy your local project files into the container. This is the standard practice.
COPY . /amrlib

# Install git and other system dependencies needed to build Python packages.
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the amrlib package itself.
RUN pip install --no-cache-dir -e .

# The default command when the container starts.
CMD ["/bin/bash"]