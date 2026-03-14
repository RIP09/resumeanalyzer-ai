
```markdown
# 🚀 SmartRes AI: Professional Resume Analyzer

**SmartRes AI** is an intelligent career tool designed to bridge the gap between job seekers and recruiters. Built for the **UnsaidTalks: Code the Future** hackathon, it leverages the **Google Gemini 1.5 Flash** model to provide deep, recruiter-level insights.

## 🌟 Key Features
- **ATS-Style Scoring:** Instant rating out of 10 based on JD relevance.
- **Strict 2-Line Summary:** Generates high-impact professional summaries designed to pass human screening.
- **Skill Gap Analysis:** Highlights specific missing keywords and technologies required by the JD.
- **Actionable Task:** Provides a single, high-priority "Improvement Task" to help the user reach a score of 8/10.
- **Smart Model Fallback:** Built-in technical redundancy to ensure stability across different Gemini API versions.

## 🏗️ Technical Stack
- **Frontend:** [Streamlit](https://streamlit.io/)
- **AI Engine:** [Google Gemini API](https://ai.google.dev/)
- **PDF Processing:** [PyPDF2](https://pypdf2.readthedocs.io/)
- **Language:** Python 3.9+

---

## 🛠️ Installation & Setup

To run this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/RIP09/resumeanalyzer-ai.git
cd resumeanalyzer-ai

```

### 2. Install Dependencies

Make sure you have Python installed, then run:

```bash
pip install streamlit google-generativeai PyPDF2 python-dotenv

```
```# Step A: Ensure pip is up to date
python -m pip install --upgrade pip
```
```# Step B: Install the necessary tools (Fixed command)
python -m pip install streamlit google-generativeai PyPDF2 python-dotenv
```
```To update Libraries
pip install -U google-genai
```
### 3. Configure API Credentials

Create a `.env` file in the root directory and add your Google API Key:

env

GOOGLE_API_KEY=your_api_key_here



### 4. Run the Application

```bash
streamlit run app.py
```
   OR 
```   
python -m streamlit run app.py
```
---   

## 🚦 How to Use

1. **Upload:** Drop your resume in PDF format into the uploader.
2. **Input:** Paste the Job Description you are targeting in the text area.
3. **Analyze:** Click the **"Analyze Resume"** button.
4. **Iterate:** Review the **Gap Analysis** and perform the **Improvement Task** suggested by the AI to boost your score.

## 🛡️ Security Note

This project uses `.env` files to manage API keys. Ensure the `.env` file is included in your `.gitignore` to prevent leaking credentials to public repositories.

---

**Developed for the UnsaidTalks Hackathon | March 2026**

```
If Error comes :
 now when i tap to Analyze Resume it's saying AI Error: 429 RESOURCE_EXHAUSTED. {'error': {'code': 429, 'message': 'You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_input_token_count, limit: 0, model: gemini-2.0-flash\n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 0, model: gemini-2.0-flash\n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 0, model: gemini-2.0-flash\nPlease retry in 48.022582141s.', 'status': 'RESOURCE_EXHAUSTED', 'details': [{'@type': 'type.googleapis.com/google.rpc.Help', 'links': [{'description': 'Learn more about Gemini API quotas', 'url': 'https://ai.google.dev/gemini-api/docs/rate-limits'}]}, {'@type': 'type.googleapis.com/google.rpc.QuotaFailure', 'violations': [{'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_input_token_count', 'quotaId': 'GenerateContentInputTokensPerModelPerMinute-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.0-flash'}}, {'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerMinutePerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.0-flash'}}, {'quotaMetric': 'generativelanguage.googleapis.com/generate_content_free_tier_requests', 'quotaId': 'GenerateRequestsPerDayPerProjectPerModel-FreeTier', 'quotaDimensions': {'location': 'global', 'model': 'gemini-2.0-flash'}}]}, {'@type': 'type.googleapis.com/google.rpc.RetryInfo', 'retryDelay': '48s'}]}}
```
```
Solution:
🛠️ How to fix this right now
1. The "Wait and Retry" (Easiest)
Look at the error message: Please retry in 48s. Google's free tier has a RPM (Requests Per Minute) limit.

Stop clicking the button.

Wait exactly one full minute.

Click "Analyze Resume" again. It will likely work.

2. Switch to a Different Model (The Hack)
Different models have separate quotas. If gemini-2.0-flash is exhausted, gemini-1.5-flash might still have room.

Change this line in your app.py:

Python
# Change from 2.0 to 1.5
model="gemini-1.5-flash" 
3. Create a Second API Key (The Backup)
If you have truly exhausted your daily limit:

Go back to Google AI Studio.

Create a New Project and generate a New API Key.

Update your .env file with this new key.
```
Developed by Deepanshu Murmu
For Code the Future: AI Edition Hackathon
---

