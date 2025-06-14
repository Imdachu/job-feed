import json
from datetime import date

def get_daily_jobs():
    jobs = [
        {
            "date": date.today().isoformat(),
            "company": "TechOrbit Labs",
            "role": "Junior Full Stack Developer",
            "stack": "JavaScript, Node.js, MongoDB",
            "location": "Remote (India)",
            "teamSize": "150",
            "applyLink": "https://techorbitlabs.notion.site/Careers",
            "status": "To Apply"
        },
        {
            "date": date.today().isoformat(),
            "company": "AlgoAnalytics",
            "role": "AI Intern",
            "stack": "Python, OpenCV, FastAPI",
            "location": "Pune / Remote",
            "teamSize": "200",
            "applyLink": "https://algoanalytics.notion.site/jobs",
            "status": "To Apply"
        }
        # Add 8 more later if needed
    ]
    return {"jobs": jobs}

if __name__ == "__main__":
    with open("daily_jobs.json", "w") as f:
        json.dump(get_daily_jobs(), f, indent=2)
