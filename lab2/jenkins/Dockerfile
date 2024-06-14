FROM jenkins/jenkins:lts

# Install Python and pip
USER root
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

# Install Docker CLI
RUN apt-get install -y apt-transport-https ca-certificates curl software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y docker-ce-cli

USER jenkins

# Create Jenkins workspace directory
RUN mkdir -p /var/jenkins_home/workspace
WORKDIR /var/jenkins_home/workspace

# Copy Jenkinsfile and project files
COPY . /var/jenkins_home/workspace

# Define the default command
CMD ["sh", "-c", "java -jar /usr/share/jenkins/jenkins.war"]
