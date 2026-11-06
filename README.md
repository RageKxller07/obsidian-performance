# OBSIDIAN® PERFORMANCE LABS

Obsidian is a secure, full-stack biometrics and performance tracking dashboard designed for multi-discipline athletes and coaches. It replaces messy spreadsheets and bloated commercial apps with a fast, private, and analytical local platform.

## 🚀 Features
* **Secure Authentication:** User accounts are protected via Werkzeug password hashing and Flask-Login session management.
* **Multi-Discipline Logging:** Dynamically adapts inputs for Sprint (Speed), Endurance (Distance), and Strength (Volume/Reps) sessions.
* **Advanced Analytics Engine:** Uses Pandas and Matplotlib to instantly calculate Personal Records, Epley 1RM estimates, volume tonnage, and render dark-aesthetic trajectory graphs.
* **AI Coach Integration:** Connects to the Google GenAI API to generate plain-English, actionable insights based on the athlete's last 5 sessions.
* **Professional Exports:** Generate and download fully formatted PDF dossiers and DOCX reports with a single click.

## 🛠️ Tech Stack
* **Backend:** Python, Flask, SQLite
* **Data Science:** Pandas, Matplotlib
* **AI/LLM:** Google GenAI API
* **Frontend:** HTML5, CSS3 (Glassmorphism styling), Vanilla JavaScript
* **Export Utilities:** FPDF, python-docx

## ⚙️ Local Installation
1. **Clone the repository:**
   \`\`\`bash
   git clone https://github.com/YourUsername/obsidian-performance.git
   cd obsidian-performance
   \`\`\`

2. **Install dependencies:**
   \`\`\`bash
   pip install flask pandas matplotlib fpdf python-docx flask-login werkzeug google-genai
   \`\`\`

3. **Set your API and Secret Keys:**
   Set your environment variables or update the `main.py` file with your Gemini API key and Flask Secret Key.
   \`\`\`bash
   export OBSIDIAN_SECRET_KEY="your-secure-key"
   export GEMINI_API_KEY="your-gemini-key"
   \`\`\`

4. **Run the application:**
   \`\`\`bash
   python main.py
   \`\`\`
   Navigate to `http://127.0.0.1:5000` in your browser.

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.
