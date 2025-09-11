from flask import Flask
app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return """
    <html>
      <head>
        <title>Resume</title>
      </head>
      <body>
        <h1>Yashwanth B</h1>
        <h2>DevSecOps Engineer</h2>
        <p>Email: <a href="mailto:yashwanthbhaskar0@gmail.com">yashwanthbhaskar0@gmail.com</a></p>
        <p>Mobile: +91 9916949343</p>
        <p>
          <a href="https://www.linkedin.com/in/yashwanth-b-43ba74219" target="_blank">LinkedIn</a> | 
          <a href="https://github.com/Yashwanth0422" target="_blank">GitHub</a>
        </p>

        <h3>Professional Summary:</h3>
        <p>
          DevOps Engineer with X years of experience designing scalable and secure infrastructure in AWS environments. Expert in CI/CD automation, cloud-native deployments, cost optimization, and infrastructure as code using Terraform, Helm, and GitHub Actions. Proven ability to deliver compliant cloud platforms with strong focus on performance, reliability, and security.
        </p>

        <h3>Core Competencies:</h3>
        <ul>
          <li>Programming Languages: Shell scripting</li>
          <li>Version Control: GitHub, AWS CodeCommit</li>
          <li>CI/CD Tools: Jenkins, GitHub Actions, ArgoCD</li>
          <li>Cloud Platforms: AWS, GCP</li>
          <li>Infrastructure as Code (IaaC) & Scaling: Terraform, Terragrunt, Helm, Ansible, Karpenter</li>
          <li>Monitoring Tools: Grafana, SonarQube, Cloudwatch</li>
        </ul>

        <h3>Experience:</h3>
        <ul>
          <li>Company Name: Pierian Services – Role: DevOps Engineer</li>
          <li>Company Name: Infosys – Role: DevOps Engineer, Bangalore from 2024</li>
        </ul>

        <h3>Project Description:</h3>
        <p><strong>Debt Collection SaaS & Aaas Platform</strong> - xxxx</p>
        <p><strong>E-Commerce website (xxxx):</strong> This is a java-based project, involving development of an e-commerce website focused on promoting and selling products online, offering features such as a product catalog, shopping cart, payment gateway.</p>
        
        <h3>AI-Driven CI/CD Automation</h3>
        <p>Tech: Llama3.2, GitHub Actions, Docker, AWS Bedrock</p>
        <ul>
          <li>Auto-generated optimized Dockerfiles (reduced image size by 35% via multi-stage builds)</li>
          <li>Dynamically adjusted Terraform resource allocations (cut infra costs by 20% via AI-driven scaling recommendations)</li>
          <li>Reduced Docker build times by 40% (from 8 mins → 4.8 mins per build)</li>
        </ul>

        <h3>Serverless Data Lake (AWS Glue + QuickSight)</h3>
        <p>Built a serverless data lake to ingest/transform 10TB+ of transactional data</p>

        <h3>Roles and Responsibilities:</h3>
        <ul>
          <li>Automated 50+ CI/CD pipelines using Jenkins, GitHub Actions & ArgoCD, improving deployment speed by 60% across microservices.</li>
          <li>Built GKE & EKS clusters with Helm & Terraform & Terragrunt, reducing infrastructure provisioning time by 50%.</li>
          <li>Leveraged AWS key services: EC2, IAM, S3, RDS, etc.</li>
          <li>Integrated Datadog APM/logs and set up SLO/SLI tracking, improving incident response by 40%.</li>
          <li>Aided Equabli in PCI-DSS & SOC 2 compliance audits.</li>
          <li>Configured and deployed Dynamic CCaaS solution using Amazon Connect.</li>
          <li>Automated code deployment workflows across 48+ repositories with GitHub Actions & ECR.</li>
          <li>Architected BCP-DR and Zero Trust security policies.</li>
          <li>Managed GCP infrastructure reducing cloud spend by 20%.</li>
          <li>Developed automation scripts in Python, reducing manual work by 60%.</li>
        </ul>

        <h3>Education:</h3>
        <ul>
          <li>B.E – Jyothy Institute Of Technology, VTU, 2022 (62%)</li>
          <li>12th – Narayana PU College, 2018 (74%)</li>
          <li>10th – Narayana E-techno School, 2016 (10 CGPAs)</li>
        </ul>
      </body>
    </html>
    """, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
