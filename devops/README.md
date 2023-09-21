JupyterLab Docker Setup
docker hub container image

This project provides a Dockerized environment for JupyterLab with enhanced features and popular data science packages. It uses a Dockerfile for the container setup and a docker-compose.yml for orchestrating the container run with volume bindings.

Base Image
The setup is based on the official JupyterLab Docker image: jupyter/scipy-notebook. This image provides a comprehensive environment with many pre-installed scientific computing libraries.

Setup Instructions
1. Directory Setup
Before running the container, create a directory named data_science in the root of this project. This directory will be mounted into the JupyterLab container and will serve as the working directory for your Jupyter notebooks and datasets.

mkdir data_science
2. Setting Permissions
For the JupyterLab container to access and write to the data_science directory, the permissions need to be set to user ID 1000 and group ID 1000.

Linux:
Run the following command:

sudo chown -R 1000:1000 data_science/
Windows:
If you're using WSL (Windows Subsystem for Linux), navigate to your project directory in the WSL terminal and run:

sudo chown -R 1000:1000 data_science/
If you're not using WSL, Docker Desktop for Windows should handle the permissions for you. However, if you encounter any permission issues, consider using WSL or adjusting the Docker settings for file sharing.

3. Running the Container
With docker-compose installed, navigate to the directory containing the docker-compose.yml file and run:

docker-compose up
This will build the Docker image (if not already built) and start the JupyterLab server. You can then access JupyterLab by navigating to http://127.0.0.1:8888/lab/ in your browser.

Conclusion
This setup provides a seamless JupyterLab experience with popular data science packages pre-installed. By using Docker, we ensure a consistent and reproducible environment for all your data science projects.
