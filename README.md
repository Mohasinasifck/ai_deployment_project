# 🚀 AI Model Deployment Project  

## 📖 Overview  
This project demonstrates how to deploy an AI inference model using **Docker, GitHub Actions, and CI/CD pipelines**.  

## 🎯 Features  
- **Containerized Deployment**: Uses **Docker** to package the AI model.  
- **CI/CD Pipeline**: GitHub Actions automate testing and deployment.  
- **Scalability**: Easily deploy the model to cloud platforms.  

---

# ⚙️ **Setup & Installation**  

## 1️⃣ **Clone the Repository**
First, clone the project from GitHub:  
```sh
git clone https://github.com/Mohasinasifck/ai_deployment_project.git
cd ai_deployment_project
```

## 2️⃣ Set Up Python Environment & Install Dependencies
```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
## 3️⃣ Run the Application Locally
With Python
```sh
python app.py
```
This should start your AI model inference server.

# 🚀 Using Docker
## 4️⃣ Build a Docker Image
Ensure Docker is installed and running, then build the image:
```sh
docker build -t ai_inference .
```
## 5️⃣ Run the Docker Container
```sh
docker run -p 5000:5000 ai_inference
```
Your application should now be accessible at http://localhost:5000.

# 🛠 GitHub Actions CI/CD Pipeline Setup
## 6️⃣ Set Up GitHub for CI/CD
Configure Git
```sh
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
Initialize a Git Repository
```sh
git init
git add .
git commit -m "Initial commit"
```
Create & Connect to GitHub Repository
Create a GitHub repository and link it to your local project:

```sh
git remote add origin https://github.com/Mohasinasifck/ai_deployment_project.git
git branch -M main
git push -u origin main
```
🔄 Automated Deployment (CI/CD)
GitHub Actions will automatically build and test the project on every push.

## 7️⃣ Manually Trigger the Workflow
Go to GitHub → Actions

Click on the failed workflow if there is an error.

Click "Re-run jobs" to trigger a new build.

# 📄 Project Structure
```bash
├── app.py                  # AI Model Inference Script
├── Dockerfile              # Dockerfile for containerizing the app
├── requirements.txt        # Python dependencies
├── .github/workflows/ci.yml # CI/CD configuration
├── README.md               # Project documentation
```
