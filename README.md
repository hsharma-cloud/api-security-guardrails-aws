🔐 API Security Guardrails (AWS + Terraform)
📌 Project Background

Modern applications rely heavily on APIs, making them a critical attack surface. Misconfigured APIs can lead to unauthorized access, data exposure, and security breaches.

This project demonstrates how to design and implement security guardrails for APIs using AWS serverless services and Terraform. The focus is on building a secure, observable, and resilient API with layered security controls.

🎯 Objectives
Build a secure API using AWS serverless architecture
Apply layered security guardrails across multiple components
Implement monitoring and incident response
Use Infrastructure as Code (Terraform) for consistency and repeatability
Simulate real-world failure scenarios and validate alerting
🏗️ Architecture
Client → API Gateway → Lambda → CloudWatch Logs
                         ↓
                  CloudWatch Alarm
                         ↓
                        SNS
                         ↓
                      Email Alert
🛡️ Security Guardrails Implemented
1. Access Control (API Layer)
API Gateway enforces controlled access through a defined route (/secure)
Prevents direct access to backend services
2. Least Privilege (Compute Layer)
Lambda function uses an IAM role with minimal required permissions
Reduces risk in case of compromise
3. Infrastructure Control (Deployment Layer)
Entire infrastructure is defined using Terraform
Prevents manual misconfiguration
Enables consistent and repeatable deployments
4. Monitoring & Logging (Visibility Layer)
CloudWatch captures logs and metrics from Lambda
Provides visibility into system behavior and API usage
5. Incident Response (Response Layer)
CloudWatch Alarm detects Lambda errors
SNS sends real-time email alerts
Enables rapid detection and response to issues
🚨 Incident Response Workflow
Lambda Error → CloudWatch Logs → Alarm Triggered → SNS → Email Notification
🧪 Testing & Validation
API tested using curl
Simulated failure by introducing an error in Lambda function
Verified:
Error detection in CloudWatch
Alarm triggering
Email alert delivery via SNS
🛠️ Technologies Used
AWS Lambda
Amazon API Gateway
Amazon CloudWatch
Amazon SNS
Terraform
🚀 Deployment
terraform init
terraform apply
🧹 Cleanup
terraform destroy
🎯 Key Outcomes
Designed and deployed a secure serverless API
Implemented layered security guardrails
Built monitoring and automated incident response pipeline
Demonstrated real-world cloud security architecture
🧠 Key Learnings
Importance of securing APIs at multiple layers
Practical implementation of least privilege and access control
Building observability using CloudWatch
Automating incident detection and response
Managing infrastructure using Terraform
🔥 Future Enhancements
Add AWS WAF for advanced threat protection
Implement authentication (JWT / Cognito)
Add rate limiting and throttling
Integrate with SIEM for centralized monitoring
📎 Author

Hari Sharma
GitHub: https://github.com/hsharma-cloud
