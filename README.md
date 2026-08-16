# SysMetric

SysMetric is a Linux system metrics monitoring application built with Python and Flask. It collects CPU, memory, disk, network, and uptime metrics and stores them in PostgreSQL.

The project demonstrates a complete DevOps workflow using Docker, Jenkins, Kubernetes, and AWS.

## Features

- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Network traffic monitoring
- System uptime monitoring
- Flask REST API
- PostgreSQL database
- Docker containerization
- Docker Compose
- Jenkins CI/CD
- Docker Hub image publishing
- Kubernetes deployment
- AWS CloudFormation infrastructure
- AWS VPC
- EC2
- RDS PostgreSQL
- Application Load Balancer
- IAM
- NAT Gateway

## API Endpoints

### Health Check

GET /health

Returns the application status.

Example response:

{"status": "running"}

### Metrics

GET /metrics

Collects the current system metrics, stores them in PostgreSQL, and returns the metrics as JSON.

## Metrics Collected

SysMetric collects:

- CPU usage
- Memory usage
- Disk usage
- Network bytes sent
- Network bytes received
- System uptime

Metrics are collected using the Python psutil library.

## Project Structure

sysmetric/
├── app.py
├── collector.py
├── database.py
├── test.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── k8s/
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── postgres.yaml
│   ├── app-deployment.yaml
│   └── app-service.yaml
└── aws/
    └── infrastructure.yaml

## Technology Stack

### Application

- Python
- Flask
- psutil
- PostgreSQL
- psycopg2

### DevOps

- Git
- GitHub
- Docker
- Docker Compose
- Jenkins
- Docker Hub
- Kubernetes
- AWS CloudFormation

### AWS

- VPC
- EC2
- RDS PostgreSQL
- Application Load Balancer
- Security Groups
- Internet Gateway
- NAT Gateway
- IAM

## Local Setup

Clone the repository:

git clone https://github.com/atulsharma15446-lang/sysmetric.git
cd sysmetric

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

The application runs on:

http://localhost:8000

Test the health endpoint:

curl http://localhost:8000/health

Test metrics:

curl http://localhost:8000/metrics

## Collector Testing

The metrics collector can be tested independently:

python test.py

This tests metric collection without Flask or the database.

## Docker

Build the image:

docker build -t sysmetric .

Run the container:

docker run -p 8000:8000 sysmetric

## Docker Compose

Start SysMetric and PostgreSQL:

docker compose up --build

Stop the services:

docker compose down

## Kubernetes

The Kubernetes configuration contains:

- Namespace
- ConfigMap
- Secret
- PostgreSQL
- SysMetric Deployment
- SysMetric Service

Apply the resources:

kubectl apply -f k8s/

Check pods:

kubectl get pods -n sysmetric

Check services:

kubectl get services -n sysmetric

The application runs on port 8000 inside the container and uses NodePort 30080 for external access.

## Jenkins CI/CD

The Jenkins pipeline performs:

1. Checkout source code
2. Build Docker image
3. Tag Docker image
4. Login to Docker Hub
5. Push Docker image
6. Deploy to Kubernetes

Docker images use the Jenkins build number for versioning and also receive the latest tag.

## AWS Infrastructure

AWS infrastructure is provisioned using CloudFormation.

The infrastructure includes:

- VPC
- Public and private subnets
- Internet Gateway
- NAT Gateway
- Route Tables
- Security Groups
- Jenkins Controller EC2
- Jenkins Agent EC2
- Metrics Server EC2
- RDS PostgreSQL
- Application Load Balancer
- IAM Role and Instance Profile

Application traffic follows:

Internet → Application Load Balancer → Metrics Server → PostgreSQL RDS

Private resources use the NAT Gateway for outbound internet access.

## Database Configuration

SysMetric uses PostgreSQL.

The application uses these environment variables:

- DB_HOST
- DB_PORT
- DB_NAME
- DB_USER
- DB_PASSWORD

Database credentials should not be committed to GitHub.

## Health Monitoring

The /health endpoint can be used by the Application Load Balancer and Kubernetes health probes to verify that the application is running.

## Future Improvements

- Prometheus integration
- Grafana dashboards
- Persistent Kubernetes storage
- Kubernetes readiness and liveness probes
- HTTPS
- Automated testing in Jenkins
- Monitoring and alerting
- Kubernetes Horizontal Pod Autoscaling
- Improved secrets management
- Terraform-based AWS infrastructure

## Author

Atul Sharma

## License

This project is a learning and portfolio DevOps project.
