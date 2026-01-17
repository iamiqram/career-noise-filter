# 🎯 Career Noise Filter (AI-Powered)

**Stop guessing. Start focusing.**
A minimal Python CLI tool that helps engineering students prioritize learning by comparing their profile against specific opportunities using Google Gemini AI.

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.8 or higher
- Google Gemini API key ([Get one free here](https://aistudio.google.com/app/apikey))

### 2. Installation

```bash
# Clone the project
git clone [https://github.com/YOUR_USERNAME/career-noise-filter.git](https://github.com/YOUR_USERNAME/career-noise-filter.git)
cd career-noise-filter

# Install dependencies
pip install -r requirements.txt
3. Setup API Key (Important!)
For security, this tool uses environment variables. Do not paste your key directly into the code.

Windows (Command Prompt):

DOS

set GEMINI_API_KEY=your_actual_api_key_here
Mac / Linux / Git Bash:

Bash

export GEMINI_API_KEY="your_actual_api_key_here"
4. Run the Tool
Bash

python career_filter_app.py example_student_profile.json example_internship.txt
Or save the output to a text file:

Bash

python career_filter_app.py example_student_profile.json example_internship.txt > my_roadmap.txt
📋 How It Works
Input your profile (JSON): Your branch, year, current skills, and career goal.

Paste internship/job description (TXT): The specific requirements from a LinkedIn or company post.

Get AI-powered roadmap:

✅ FOCUS NOW (Highest priority skills to bridge the gap)

❌ IGNORE FOR NOW (Distractions to avoid)

📅 LEARN LATER (Skills for future growth)

🎯 CONFIDENCE BOOST (Quick wins based on what you already know)

📁 File Structure
career-noise-filter/
├── career_filter_app.py        # Main application script
├── requirements.txt            # Dependencies
├── example_student_profile.json # Sample student input (Use this for testing)
├── example_internship.txt      # Sample internship description
├── .gitignore                  # Security file (hides keys/personal data)
└── README.md                   # This file
🎯 How to Use with Your Own Data
1. Create Your Profile
Create a new file named my_profile.json (you can copy the structure from example_student_profile.json):

JSON

{
  "name": "Your Name",
  "branch": "Computer Science / IT",
  "year": "2nd Year",
  "current_skills": ["Python", "HTML", "SQL"],
  "career_goal": "Backend Engineer"
}
2. Find a Job Description
Create a text file named internship.txt and paste the "Requirements" section from a real job posting (LinkedIn, Internshala, etc.).

3. Run the Analysis
Bash

python career_filter_app.py my_profile.json internship.txt
(Note: my_profile.json and internship.txt are ignored by Git, so your personal info stays private!)

🔐 Security Note
Never commit your API key to GitHub.

This project includes a .gitignore file to prevent uploading personal data files (my_profile.json, internship.txt) and system files (.env).

🐛 Troubleshooting
"GEMINI_API_KEY environment variable not set"

You forgot Step 3 in "Quick Start". Run set GEMINI_API_KEY=... (Windows) or export GEMINI_API_KEY=... (Mac/Linux) in your terminal before running the script.

"Module not found: google.generativeai"

Run: pip install -r requirements.txt

"404 Not Found / Model not supported"

The script uses gemini-flash-latest to find the best model for your key automatically. Ensure your internet connection is active.

💡 Why This Tool?
Engineering students are often bombarded with contradictory advice ("Learn React!", "No, do CP!", "Focus on AI!"). This tool cuts through the noise by using AI to perform a gap analysis between what you know and what the specific job requires, creating a prioritized roadmap.

📜 License
MIT License - Feel free to use, modify, and distribute.