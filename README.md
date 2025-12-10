Two-Tier Flask Web Application (Docker, MySQL, Jenkins, AWS)

This project is a cloud-based two-tier web application built using Flask for the application tier and MySQL for the database tier. Both services are containerized using Docker and orchestrated using Docker Compose. CI/CD automation is handled through Jenkins, and the complete system is deployed on an AWS EC2 instance.

Features

Flask dashboard for displaying database records

MySQL as backend database

Containerized application and database using Docker

Jenkins-based CI/CD automation

Deployment on AWS EC2 with persistent data storage

Architecture

Frontend requests → Flask application

Flask queries → MySQL database

Both containers hosted and orchestrated on AWS EC2

Deployment Summary

Local development and testing completed using Flask and MySQL

Application and database packaged as Docker containers

Jenkins pulls from GitHub and redeploys automatically

Final deployment runs on a cloud server (EC2) with 24×7 availability

Status

The application is fully functional, cloud-hosted, database-driven, and CI-enabled.
