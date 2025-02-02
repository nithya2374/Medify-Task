# 🚀 **Medify Task**

Welcome to the **Medify Assignment**! This guide will walk you through setting up and running the project seamlessly.

---

## 📋 **Prerequisites**
Ensure you have the following installed before proceeding:
- 🐳 [Docker Desktop](https://www.docker.com/products/docker-desktop) – To build and run the Docker container.
- 🐍 Python (Optional) – If you want to test the application locally before containerization.

---

## ⚙️ **Setup Instructions**

### 🔗 Clone the Repository
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/nithya2374/Medify-Task.git
cd Medify-Task
```

### 🏗️ Build the Docker Image
Create a Docker image for the Python application:
```bash
docker build -t python-docker-app .
```

### ▶️ Run the Docker Container
Launch the application inside a container:
```bash
docker run -p 5000:5000 python-docker-app
```
🔗 Now, visit **[http://localhost:5000](http://localhost:5000)** to access the application.

---

## 📂 **Project Structure**
```plaintext
Medify-Assignment
├── LICENSE
├── Dockerfile         # Defines how to build the Docker image
├── code.py            # Main Python script for the application
├── requirements.txt   # List of dependencies for Python
└── README.md          # This documentation
```

---

## ✨ **Customizing the Application**

### 📦 Adding New Dependencies
Need extra Python libraries? Follow these steps:
1. Add them to `requirements.txt`.
2. Rebuild the Docker image:
   ```bash
   docker build -t python-docker-app .
   ```

---

## 🐛 **Troubleshooting**

### ❌ **Container Exits Immediately?**
🔍 **Possible Cause**: Application errors or misconfigurations.
✅ **Solution**: Check the logs with:
   ```bash
   docker logs <container_id>
   ```

### ⚠️ **Port Already in Use?**
🔍 **Possible Cause**: Another process is using port 5000.
✅ **Solution**: Run on a different port:
   ```bash
   docker run -p 8080:5000 python-docker-app
   ```
   Now, visit **[http://localhost:8080](http://localhost:8080)**.

---

## 🎯 **Key Takeaways**
By completing this project, you will:
✅ Understand Docker for containerizing Python applications.
✅ Manage dependencies efficiently using `requirements.txt`.
✅ Build optimized and reproducible Docker images.
✅ Run and test applications in isolated environments.

---

## 📧 **Get in Touch**
For questions, feedback, or collaboration, feel free to reach out:
- 📩 **Email**: [nithyasri17012004@gmail.com](mailto:nithyasri17012004@gmail.com)
- 🐙 **GitHub**: [nithya2374](https://github.com/nithya2374)

---

### ⭐️ **Thank You for Exploring This Assignment!** 🚀

