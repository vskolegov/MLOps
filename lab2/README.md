# Machine Learning Pipeline Project with Jenkins and Docker

## Overview

This project demonstrates a simple machine learning pipeline using Jenkins for automation and Docker for containerization. The pipeline includes data collection, preprocessing, model training, and prediction.

## Setup Instructions

### 1. Install and start Docker Desktop

Download and install Docker Desktop from the official website: https://www.docker.com/products/docker-desktop

### 2. Build Docker Container


Open a terminal and navigate to the `lab2/jenkins` directory, then run the following commands:

```bash
# Build the Docker image
docker build -t jenkins-ml-pipeline .
```

Now you can find the kenkins image in Docker
 

Run Docker Container:

```bash
# Run the Docker container
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins-ml-pipeline
```

Or manually in Docker Dektop

Copy password from terminal and open Jenkins in your browser at http://localhost:8080.

I recommend immediately installing the proposed modules, especially Git, because it will be difficult to do this later.

## Jenkins

### 1. Password recovery

```bash
docker exec <container_id> cat /var/jenkins_home/secrets/initialAdminPassword
```

![alt text]([example.com/logo.png](https://imgur.com/a/c1MH1IF))

