import json
from datetime import date

def get_daily_jobs():
    jobs = [
  {
    "company": "Intechive Systems",
    "role": "Junior Software Engineer",
    "location": "Yelahanka, Bengaluru",
    "experience": "0–1 yr",
    "skills": "Python, JavaScript, Java, Go",
    "apply_link": "https://internshala.com/job/detail/fresher-junior-software-engineer-job-in-bangalore-at-intechive-systems1748333267",
    "source": "Internshala"
  },
  {
    "company": "The Scalers",
    "role": "Junior Software Developer",
    "location": "Bengaluru",
    "experience": "0–1 yr",
    "skills": "Full-stack (Ruby, JS, Java, Python)",
    "apply_link": "https://in.indeed.com/q-junior-software-developer-fresher-l-bengaluru",
    "source": "Indeed"
  },
  {
    "company": "Aertrip Pvt Ltd",
    "role": "Junior Backend Developer",
    "location": "Koramangala, Bengaluru",
    "experience": "0–1 yr",
    "skills": "Unix, Windows environments, Backend dev",
    "apply_link": "https://in.indeed.com/q-junior-backend-developer-fresher-l-bengaluru",
    "source": "Indeed"
  },
  {
    "company": "AIRDIT Software Services",
    "role": "Trainee Software Engineer",
    "location": "Bengaluru / Lucknow",
    "experience": "0–1 yr",
    "skills": "Java, Advanced Java, OOP, DBMS",
    "apply_link": "https://in.indeed.com/q-airdit-software-jobs.html",
    "source": "Indeed"
  },
  {
    "company": "Canonical (Ubuntu)",
    "role": "Software Engineer",
    "location": "Remote / Bengaluru",
    "experience": "Entry-level",
    "skills": "Python, Go, DevOps, Infrastructure",
    "apply_link": "https://jobseekersconnect.com/software-engineer-canonical-bangalore/",
    "source": "JobSeekersConnect"
  }
]

    return {"jobs": jobs}

if __name__ == "__main__":
    with open("daily_jobs.json", "w") as f:
        json.dump(get_daily_jobs(), f, indent=2)
