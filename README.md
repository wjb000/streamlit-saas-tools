# Streamlit SaaS Tools Collection

7 ready-to-customize Streamlit product starters you can turn into real paid products.

**Repo:** https://github.com/wjb000/streamlit-saas-tools  
**Goal:** Fast MVPs that can reach $5–10k/month with low ongoing time.

---

## The 7 Tools

| # | Folder | Product | Description |
|---|--------|---------|-------------|
| 1 | `01-pdf-chat` | AI PDF Chat | Upload PDF → ask questions with sources |
| 2 | `02-resume-optimizer` | Resume Optimizer | Upload resume → score + rewrite for target job |
| 3 | `03-content-repurposer` | Content Repurposer | Blog/transcript → Twitter, LinkedIn, email, script |
| 4 | `04-data-cleaner` | CSV/Excel Cleaner + Report | Clean messy data + generate charts & summary |
| 5 | `05-contract-summarizer` | Contract Summarizer | Upload contract → plain English + risks |
| 6 | `06-meeting-notes` | Meeting Notes Organizer | Transcript → summary, action items, follow-ups |
| 7 | `07-product-photo` | Product Photo Enhancer | Background removal + quality boost for e-commerce |

---

## How to Run Any Tool Locally

```bash
# 1. Clone the repo
git clone https://github.com/wjb000/streamlit-saas-tools.git
cd streamlit-saas-tools

# 2. Go into one tool folder
cd 01-pdf-chat

# 3. Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set your OpenAI key (needed for most AI tools)
export OPENAI_API_KEY="sk-your-key-here"

# 6. Run
streamlit run app.py
```

---

## Next Steps to Monetize

1. Add authentication (Streamlit-Authenticator or Supabase)
2. Add Stripe payments
3. Deploy to Streamlit Community Cloud, Render, or Railway
4. Improve UI and add your branding
5. Start getting users

Each folder contains a working MVP you can expand.

---

Built for solo founders who want to ship fast with Python + Streamlit.
