import os
import streamlit as st
import PyPDF2
from openai import OpenAI
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ✅ Use SambaNova Cloud API
SAMBA_API_KEY = os.getenv("SAMBA_API_KEY")
client = OpenAI(
    api_key=SAMBA_API_KEY,
    base_url="https://api.sambanova.ai/v1"
)

# Streamlit UI
st.set_page_config(page_title="AI Personal Finance Analyzer & Assistant", page_icon="💰", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
    /* Main Title */
    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: 800;
        color: #2E7D32;
        margin-bottom: 10px;
        text-shadow: 1px 1px 4px rgba(46, 125, 50, 0.3);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Subtitle */
    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-bottom: 25px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Buttons */
    .stButton button, .stDownloadButton button {
        background: linear-gradient(135deg, #43A047, #1B5E20);
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 6px;
        border: none;
        font-weight: bold;
        transition: 0.3s ease-in-out;
        box-shadow: 0px 3px 6px rgba(0,0,0,0.2);
    }
    .stButton button:hover, .stDownloadButton button:hover {
        background: linear-gradient(135deg, #1B5E20, #388E3C);
        transform: translateY(-2px);
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    /* Result Card */
    .result-card {
        background: #F1F8E9;
        padding: 18px;
        border-left: 5px solid #2E7D32;
        border-radius: 6px;
        margin-bottom: 15px;
        font-size: 15px;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
    }
    /* Success Banner */
    .success-banner {
        background: linear-gradient(90deg, #2E7D32, #66BB6A);
        color: white;
        padding: 15px;
        font-size: 18px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
        box-shadow: 0px 3px 8px rgba(0,0,0,0.3);
        animation: fadeIn 1.2s ease-in-out;
    }
    /* Subtle animation */
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(10px);}
        to {opacity: 1; transform: translateY(0);}
    }
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: #E8F5E9;
        color: #1B5E20;
        padding: 20px;
    }
    section[data-testid="stSidebar"] .css-1d391kg {
        font-size: 20px;
        font-weight: bold;
        color: #2E7D32;
    }
    section[data-testid="stSidebar"] p {
        font-size: 14px;
        color: #2E7D32;
        margin-bottom: 10px;
    }
    /* Footer */
    .footer {
        position: relative;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 12px;
        font-size: 14px;
        color: #2E7D32;
        background: #E8F5E9;
        border-top: 1px solid #C8E6C9;
        margin-top: 30px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .footer a {
        color: #1B5E20;
        text-decoration: none;
        font-weight: 600;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Info
st.sidebar.title("ℹ️ How to Use This Tool?")
st.sidebar.write("- Upload your Paytm Transaction History PDF.")
st.sidebar.write("- The AI will analyze your transactions.")
st.sidebar.write("- You will receive insights: income, expenses, savings, and trends.")
st.sidebar.write("- Use this data to plan your finances effectively.")

# Titles
st.markdown('<h1 class="main-title">💰 AI-Powered Personal Finance Analyzer & Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Upload your Paytm Transaction History PDF for Financial Insights</p>', unsafe_allow_html=True)


# Upload PDF File
uploaded_file = st.file_uploader("📂 Upload PDF File", type=["pdf"], help="Only PDF files are supported")

def extract_text_from_pdf(file_path):
    """Extracts text from the uploaded PDF file."""
    text = ""
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def analyze_financial_data(text):
    """Sends extracted text to SambaNova Cloud for financial insights."""
    prompt = f"""
    Analyze the following Paytm transaction history and generate financial insights:
    {text}
    Provide a detailed breakdown in the following format:
    **Financial Insights for [User Name]**
    **Key Details:**
    - **Overall Monthly Income & Expenses:**
      - Month: [Month]
      - Income: ₹[Amount]
      - Expenses: ₹[Amount]
    - **Unnecessary Expenses Analysis:**
      - Expense Category: [Category Name]
      - Amount: ₹[Amount]
      - Recommendation: [Suggestion]
    - **Savings Percentage Calculation:**
      - Savings Percentage: [Percentage] %
    - **Expense Trend Analysis:**
      - Notable Trends: [Trend Details]
    - **Cost Control Recommendations:**
      - Suggestion: [Detailed Suggestion]
    - **Category-Wise Spending Breakdown:**
      - Category: [Category Name] - ₹[Amount]
    """

    response = client.chat.completions.create(
        model="Meta-Llama-3.1-8B-Instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()


def generate_pdf_report(insights, filename="Financial_Report.pdf"):
    """Generate a PDF report with financial insights."""
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "📊 Personal Finance Insights Report")

    # Body text
    c.setFont("Helvetica", 11)
    text_object = c.beginText(50, height - 100)
    for line in insights.split("\n"):
        text_object.textLine(line)
    c.drawText(text_object)

    c.save()
    buffer.seek(0)
    return buffer


if uploaded_file is not None:
    file_path = f"temp_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ File uploaded successfully!")

    with st.spinner("📄 Extracting text from document..."):
        extracted_text = extract_text_from_pdf(file_path)

    if not extracted_text:
        st.error("⚠️ Failed to extract text. Ensure the document is not a scanned image PDF.")
    else:
        progress_bar = st.progress(0)
        with st.spinner("🧠 AI is analyzing your financial data..."):
            insights = analyze_financial_data(extracted_text)

        progress_bar.progress(100)

        st.subheader("📊 Financial Insights Report")
        st.markdown(f'<div class="result-card"><b>📄 Financial Report for {uploaded_file.name}</b></div>', unsafe_allow_html=True)

        st.write(insights)

        # ✅ PDF download button
        pdf_buffer = generate_pdf_report(insights)
        st.download_button(
            label="📥 Download Report as PDF",
            data=pdf_buffer,
            file_name="Financial_Report.pdf",
            mime="application/pdf"
        )

        st.markdown('<div class="success-banner">🎉 Analysis Completed! Plan your finances wisely. 🚀</div>', unsafe_allow_html=True)
        st.balloons()

    os.remove(file_path)  # Cleanup

# ✅ Footer
st.markdown("""
    <div class="footer">
        Built with ❤️ using <a href="https://streamlit.io" target="_blank">Streamlit</a> 
        + <a href="https://cloud.sambanova.ai" target="_blank">SambaNova Cloud</a>
    </div>
""", unsafe_allow_html=True)