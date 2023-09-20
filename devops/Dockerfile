# Use the jupyter/scipy-notebook image as the base
FROM jupyter/scipy-notebook:latest

# Switch to root to install system packages
USER root

# Install Python 3.10 and required system dependencies
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get install -y python3.10 python3.10-dev python3.10-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install pip for Python 3.10 using get-pip.py
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3.10 get-pip.py && \
    rm get-pip.py

# Update pip and set up Python 3.10 environment
RUN python3.10 -m pip install --upgrade pip setuptools wheel

# Switch back to the jovyan user
USER jovyan

# Install the desired Python packages for JupyterLab, intellisense, and data science
RUN python3.10 -m pip install \
    "jupyterlab>=3,<4" \
    "jupyter-lsp" \
    "python-lsp-server[all]" \
    "pandas" \
    "numpy" \
    "matplotlib" \
    "seaborn" \
    "scipy" \
    "scikit-learn" \
    "statsmodels" \
    "sympy" \
    "nltk" \
    "gensim" \
    "tensorflow" \
    "keras" \
    "xgboost" \
    "lightgbm" \
    "plotly" \
    "bokeh" \
    "altair" \
    "geopandas" \
    "folium"


# Set Python 3.10 as the default kernel
RUN python3.10 -m ipykernel install --user

# Start JupyterLab with Python 3.10
CMD ["start-notebook.sh", "--NotebookApp.default_url=/lab", "--NotebookApp.kernel_spec_manager_class=nb_conda_kernels.CondaKernelSpecManager"]
