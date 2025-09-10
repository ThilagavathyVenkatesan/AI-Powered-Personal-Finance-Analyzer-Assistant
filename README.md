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
name: 🚀 Deploy to Hugging Face Spaces

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.9"

      - name: Install dependencies
        run: |
          pip install huggingface_hub

      - name: Push to Hugging Face Space
        env:
          HF_TOKEN: ${{ secrets.HF_TOKEN }}
        run: |
          huggingface-cli repo create finance-analyzer --type space --sdk streamlit --yes --token $HF_TOKEN || true
          huggingface-cli upload ./ --repo finance-analyzer --token $HF_TOKEN --repo-type space --commit-message "🚀 Auto-deploy from GitHub"
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
