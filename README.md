# AI-Powered-Personal-Finance-Analyzer-Assistant
AI-powered application that processes UPI transaction statements from multiple apps and generates actionable insights and personalized financial advice using LLMs. The system extract transaction details from varied PDF formats, structure the data, analyze spending behavior, and deliver tailored recommendations to users via an interactive report.

## 💼 Business Use Cases
- **Personal Finance Management** : Help users track and understand spending behavior.
- **Spending Habit Detection** : Identify patterns, frequent merchants, and wasteful expenses.
- **Budgeting Assistant** : Recommend personalized savings strategies and alert users.
- **Multi-App Integration** : Unify transactions across different UPI platforms.

## 📑 Project Structure

```
personal-finance-analyzer/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── .github/
│    └── workflows/
│         └── deploy.yml

```

## 🚀 Features
- Upload **Paytm Transaction History PDF**
- Extract transactions with **PyPDF2**
- Generate financial insights via **SambaNova Cloud (Llama 3.1)**
- Breakdown: income, expenses, savings, trends
- 📥 Downloadable **PDF report**
- Auto-deployed to Hugging Face Spaces via GitHub Actions 🚀
---

## 🛠️ Tech Stack
- **Python 3.9+**
- Streamlit
- SambaNova Cloud (OpenAI-compatible client)
- PyPDF2 (PDF text extraction)
- ReportLab (PDF report generation)
- Hugging Face Spaces for deployment
---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ThilagavathyVenkatesan/AI-Powered-Personal-Finance-Analyzer-Assistant.git
cd personal-finance-analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 API Key Setup
Before running the app, set your SambaNova Cloud API key as an environment variable:

### Linux/Mac

```bash
export SAMBA_API_KEY=your_api_key_here
```

### Windows (PowerShell)

```powershell
setx SAMBA_API_KEY "your_api_key_here
```

## ▶️ Running the App Locally
```bash
streamlit run app.py
```
## ☁️ Deployment
```
This project is set up for auto-deployment to Hugging Face Spaces.
### Steps:
Create a Hugging Face Space (SDK = Streamlit).

Generate an Access Token (role = Write).

Add it to GitHub:

Repo → Settings → Secrets and variables → Actions → New repository secret

Name: HF_TOKEN

Value: paste your token

Now every git push to main will redeploy the app automatically 🚀.
```

## 📄 License

MIT License

---

# 📄 .github/workflows/deploy.yml
```yaml
name: 🚀 Deploy to Hugging Face Spaces (force push)

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
        with:
          persist-credentials: false
          fetch-depth: 0

      - name: Set up git user
        run: |
          git config --global user.email "action@github.com"
          git config --global user.name "github-actions[bot]"

      - name: Push to Hugging Face Space
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: |
          set -e
          HF_REPO="https://user:$HF_TOKEN@huggingface.co/spaces/Thilagavathy/finalproject.git"

          # Remove old remote if exists, then add fresh one
          git remote remove hf || true
          git remote add hf "$HF_REPO"

          # 🚨 Force push GitHub main branch → Hugging Face main
          git push hf main --force

```
## ✅ How to Use
```
1.Copy these files into your local project folder.

2.Run the Git commands:

git init
git add .
git commit -m "Initial commit - Finance Analyzer"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/personal-finance-analyzer.git
git push -u origin main

3.Add HF_TOKEN in GitHub repo → Settings → Secrets → Actions.

4.Done 🎉 → Your Hugging Face Space auto-deploys on every push.
```
## 📸 Screenshots
<img width="1366" height="768" alt="Screenshot (77)" src="https://github.com/user-attachments/assets/33abd28a-2f51-4be7-b363-327a0e9ba411" />
<img width="1366" height="768" alt="Screenshot (78)" src="https://github.com/user-attachments/assets/bf26094f-d3e4-444b-8208-b9bb59492b67" />
<img width="1366" height="768" alt="Screenshot (79)" src="https://github.com/user-attachments/assets/7b076642-1fab-43b2-8c04-8a6cd4513286" />
