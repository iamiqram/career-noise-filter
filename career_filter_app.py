"""
Career Noise Filter - MVP
Helps engineering students generate prioritized skill roadmaps using AI
"""

import os
import json
import google.generativeai as genai
from typing import Dict, Any

class CareerNoiseFilter:
    """Main application class for generating personalized skill roadmaps"""
    
    def __init__(self):
        """Initialize the Gemini API client"""
        
        # --- GITHUB SAFE MODE ---
        # We get the key from the system, not the code file.
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            raise ValueError("Error: GEMINI_API_KEY not found. Please set it in your terminal using 'set GEMINI_API_KEY=...'")
        
        genai.configure(api_key=api_key)
        
        # Using the alias that works best for your account
        self.model = genai.GenerativeModel('gemini-flash-latest')
    
    def load_student_profile(self, profile_path: str) -> Dict[str, Any]:
        with open(profile_path, 'r') as f:
            return json.load(f)
    
    def load_internship_description(self, desc_path: str) -> str:
        with open(desc_path, 'r') as f:
            return f.read()
    
    def generate_roadmap(self, student_profile: Dict[str, Any], internship_desc: str) -> str:
        prompt = f"""You are a career advisor.
STUDENT PROFILE: {student_profile}
INTERNSHIP: {internship_desc}
TASK: Analyze the gap. Output a prioritized skill roadmap (Focus Now, Ignore For Now, Learn Later, Confidence Boost)."""
        response = self.model.generate_content(prompt)
        return response.text
    
    def run(self, profile_path, internship_path):
        print("🔍 Loading data...")
        profile = self.load_student_profile(profile_path)
        internship = self.load_internship_description(internship_path)
        print("🤖 Asking Gemini...")
        roadmap = self.generate_roadmap(profile, internship)
        print("\n" + "="*50 + "\nYOUR ROADMAP\n" + "="*50 + "\n" + roadmap)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: python career_filter_app.py my_profile.json internship.txt")
    else:
        app = CareerNoiseFilter()
        app.run(sys.argv[1], sys.argv[2])