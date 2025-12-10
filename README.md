🌐 Two-Tier Flask Web Application

A cloud-ready Flask + MySQL dashboard, fully containerized with Docker, automated using Jenkins, and deployed on AWS EC2.

🚀 What This Project Does

Runs a Flask dashboard UI

Stores user records inside a MySQL database

Uses Docker Compose to orchestrate multiple containers

Automates build and deployment via Jenkins

Hosts the complete app on AWS EC2 for 24×7 access

🏗️ How It Works
Browser → Flask Web App → MySQL Database
                 (Both inside Docker Containers)
                   Hosted on AWS EC2

⚙️ Technology Used

Flask (Application Layer)

MySQL (Database Layer)

Docker & Docker Compose (Containerization)

Jenkins (CI/CD Automation)

AWS EC2 (Cloud Hosting)

Git + GitHub (Version Control)

🌩️ Cloud Deployment Highlights

Containers run in detached background mode

MySQL volume preserves data across restarts

Jenkins redeploys automatically after updates

EC2 ensures continuous availability even when offline
