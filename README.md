# devops-ecom-k8s
DevOps E-Commerce Kubernetes Project (DevOps-ECom-K8s)
This project demonstrates a complete, end-to-end DevOps workflow for a microservices-based e-commerce application. The entire infrastructure is managed as code and deployed to a Kubernetes cluster on AWS, showcasing modern cloud-native practices from planning and development to monitoring and security.


🏛️ Architecture Diagram
This diagram illustrates the flow of the CI/CD pipeline and the deployed application architecture on AWS.

graph TD
    subgraph "Developer Workflow"
        A[Developer pushes code to GitHub] --> B{GitHub Actions CI/CD};
    end

    subgraph "CI Pipeline (GitHub Actions)"
        B --> C[Run Tests & Scans];
        C --> D[Build Docker Image];
        D --> E[Push Image to Docker Hub];
    end

    subgraph "CD Pipeline (GitHub Actions)"
        E --> F[Deploy to EKS];
    end

    subgraph "AWS Cloud Infrastructure (Managed by Terraform)"
        G[AWS EKS Cluster]
        H[VPC with Public/Private Subnets]
        I[NAT Gateway]
        J[Internet Gateway]
        K[Application Load Balancer]

        H --> G;
        I --> H;
        J --> H;
        K --> H;
    end

    subgraph "Running Application in EKS"
        F --> G;
        L[User Request] --> K;
        K --> M[Product Service Pods];
        M --> H;
    end

    style B fill:#8957E5,stroke:#333,stroke-width:2px
    style F fill:#388BFD,stroke:#333,stroke-width:2px
    style G fill:#FF9900,stroke:#333,stroke-width:2px

🛠️ Technology Stack
This project utilizes a modern, cloud-native toolchain.

Category

Tool / Technology

Cloud Provider

Amazon Web Services (AWS)

Containerization

Docker

Orchestration

Kubernetes (Amazon EKS)

CI/CD

GitHub Actions

Infrastructure as Code

Terraform

Application Backend

Python (FastAPI)

Version Control

Git & GitHub

Container Registry

Docker Hub

Monitoring

Prometheus & Grafana (via Helm)

✨ Key DevOps Concepts Demonstrated
Infrastructure as Code (IaC): The entire AWS environment (VPC, EKS Cluster, Networking) is defined and managed using Terraform, ensuring it is repeatable, version-controlled, and automated.

CI/CD Automation: A complete GitHub Actions pipeline automatically tests, builds, and deploys the application to Kubernetes on every push to the main branch.

Containerization: The application is containerized using Docker, ensuring consistency across local development and cloud environments.

Orchestration: Kubernetes (EKS) is used to manage the containerized application, handling scaling, and service discovery.

Observability: A monitoring stack with Prometheus and Grafana is deployed to provide real-time visibility into the health and performance of the cluster and application.

Cost Management: A core principle of the project is the ability to create and destroy the entire environment on-demand using terraform apply and terraform destroy, preventing unnecessary cloud costs.

📂 Repository Structure
The repository is organized into distinct directories for clean separation of concerns:

/
├── .github/workflows/      # GitHub Actions CI/CD pipeline definitions
├── iac/                    # All Terraform code for AWS infrastructure
├── kubernetes/manifests/   # Kubernetes Deployment and Service YAML files
├── services/               # Source code for the application microservices
│   └── product-service/
├── tests/                  # Test files for the application
└── README.md               # This file

🚀 How to Run This Project
Prerequisites
An AWS Account with credentials configured for the AWS CLI.

Terraform installed.

kubectl installed.

helm installed.

A Docker Hub account.

Step 1: Configure Secrets
Fork this repository and add the following secrets to Settings > Secrets and variables > Actions:

DOCKERHUB_USERNAME: Your Docker Hub username.

DOCKERHUB_TOKEN: A Docker Hub access token with "Read & Write" permissions.

AWS_ACCESS_KEY_ID: Your AWS access key.

AWS_SECRET_ACCESS_KEY: Your AWS secret key.

Step 2: Provision the Infrastructure
All AWS resources are created with Terraform.

# Navigate to the infrastructure directory
cd iac

# Initialize Terraform
terraform init

# Apply the configuration to build the VPC and EKS cluster
# This will take 15-20 minutes.
terraform apply

Step 3: Connect to the EKS Cluster
Configure kubectl to communicate with your new cluster.

aws eks update-kubeconfig --region us-east-1 --name devops-ecom-cluster

Step 4: Trigger the CI/CD Pipeline
The pipeline will automatically deploy the application. To trigger it, simply make a small change to the application code and push it.

# Make a small change, for example, in services/product-service/src/main.py
# Then commit and push the change
git add .
git commit -m "Triggering initial deployment"
git push origin main

The application will be deployed and accessible via a public Load Balancer URL, which can be found by running kubectl get service product-service.

💰 Cost Management
This project creates resources that incur costs on AWS. To stop all costs, you must destroy the infrastructure when you are finished.

# Navigate to the infrastructure directory
cd iac

# Destroy all AWS resources
terraform destroy
