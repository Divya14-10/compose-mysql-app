# Docker Compose Project - Flask App + MySQL

This project runs a **Flask Python application** connected to a **MySQL database** using **Docker Compose**.

## ✅ Services
- **app (Flask)**: Runs on port `5000`
- **mysql (MySQL 8.0)**: Runs on port `3306`
- **Volume**: `mysql_data` for persistent DB storage

## ✅ Run Project
```bash
docker compose up -d

