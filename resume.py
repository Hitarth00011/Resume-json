

import json

resume_text = """
HITARTH RATHOD
Software Engineer/ IOS App Developer/ Web Developer
+91 -7984613236
https://www.linkedin.com/in/hitarth-rathod-75b138236/
https://github.com/Hitarth00011
Chennai, Tamil Nadu
SUMMARY
Leveraging a strong foundation in programming, algorithm design, and software development skills. Proficient in languages, excelling in web and app development. Eager to apply expertise in software engineering, iOS development, and graphic design.
EDUCATION
Bachelor of Science, Computer Science
09/2021 – 06/2025
SRM Institute Of Science & Technology ( Deemed University)
Chennai, Tamil Nadu
CGPA
9.01
INTERNSHIP EXPERIENCE
IOS APP DEVELOPER
04/2024 – 05/2024
Infosys
Mysore, Karnataka
Completed an internship at Infosys in Mysuru as an iOS App Developer from April 14th to May 10th, engaging in Agile methodologies and utilizing tools like JIRA.
Contributed to the development of a cutting-edge iOS app, gaining hands-on experience and enhancing technical skills in mobile app development.
Collaborated with a dynamic team, learning to navigate mobile app development intricacies and adhering to Agile principles for efficient project management.
Gained invaluable industry exposure and practical experience, furthering passion for iOS development and technology innovation while being mentored by industry experts.
Android Developer
07/2023 – 08/2023
CodeClause
Pune, Maharashtra
Collaborated with a team of 5 developers, enhancing technical skills and deepening understanding of the Android ecosystem.
Upgraded the system for automated image optimisation, achieving a 4-second load time and reducing the bounce rate by 70%.
Implemented advanced automation, reducing development time by 30%, saving 100+ hours per week.
PROJECTS
Pustak (iOS App)
https://github.com/LMS–Team-8/Pustak
Pustak is a library management app built with SwiftUI and Firebase. It features personalized recommendations, book reservations, barcode scanning, fine management, and an analytics dashboard. The app adheres to Apple's design principles and ensures secure, real-time data synchronization.
Mystic Deck (Educational IOS Games)
https://github.com/Hitarth00011/Mystic-Deck
"Revolutionizing Indian education through engaging card games: fun, inclusive, and cost-effective, bridging learning gaps with interactive, localized content."
Transforming Indian education with interactive card games: enjoyable, inclusive, economical, and culturally relevant, effectively addressing educational challenges.
Stockiment
https://github.com/Hitarth00011/Stockiment.git
In this project, I utilized sentiment analysis and two machine learning models—Random Forest and Support Vector Regression (SVR)—to investigate the relationship between Twitter tweets and the stock market movements of a company. Sentiment analysis was performed on daily and hourly Twitter data to evaluate its impact on stock market predictions. The models were assessed and compared using RMSE (root mean squared error) values to measure their predictive accuracy.
SKILLS
Technical Skills
Python
Swift UI
UI/UX Design
Jira
HTML
React
Soft Skills
Project Management
Leadership
Cross domain function
Team building
CERTIFICATIONS
IOS Application Development
Infosys
Oracle Certified Foundations Associate
ORACLE
Fortinet Certified Associate in Cybersecurity
FORTINET Training Institute
TRAINING / COURSES
Cloud Computing
IBM – Coursera
Matlab Onramp
MathWorks
Advances In Remote Sensing Techniques For Geological Applications
ISRO
"""

# Parsing the resume text into a structured JSON format
resume_json = {
    "name": "Hitarth Rathod",
    "title": "Software Engineer/ IOS App Developer/ Web Developer",
    "contact": {
        "phone": "+91 -7984613236",
        "linkedin": "https://www.linkedin.com/in/hitarth-rathod-75b138236/",
        "github": "https://github.com/Hitarth00011",
        "location": "Chennai, Tamil Nadu"
    },
    "summary": "Leveraging a strong foundation in programming, algorithm design, and software development skills. Proficient in languages, excelling in web and app development. Eager to apply expertise in software engineering, iOS development, and graphic design.",
    "education": {
        "degree": "Bachelor of Science, Computer Science",
        "duration": "09/2021 – 06/2025",
        "institution": "SRM Institute Of Science & Technology (Deemed University)",
        "location": "Chennai, Tamil Nadu",
        "cgpa": 9.01
    },
    "internship_experience": [
        {
            "title": "IOS APP DEVELOPER",
            "duration": "04/2024 – 05/2024",
            "company": "Infosys",
            "location": "Mysore, Karnataka",
            "details": [
                "Completed an internship at Infosys in Mysuru as an iOS App Developer from April 14th to May 10th, engaging in Agile methodologies and utilizing tools like JIRA.",
                "Contributed to the development of a cutting-edge iOS app, gaining hands-on experience and enhancing technical skills in mobile app development.",
                "Collaborated with a dynamic team, learning to navigate mobile app development intricacies and adhering to Agile principles for efficient project management.",
                "Gained invaluable industry exposure and practical experience, furthering passion for iOS development and technology innovation while being mentored by industry experts."
            ]
        },
        {
            "title": "Android Developer",
            "duration": "07/2023 – 08/2023",
            "company": "CodeClause",
            "location": "Pune, Maharashtra",
            "details": [
                "Collaborated with a team of 5 developers, enhancing technical skills and deepening understanding of the Android ecosystem.",
                "Upgraded the system for automated image optimisation, achieving a 4-second load time and reducing the bounce rate by 70%.",
                "Implemented advanced automation, reducing development time by 30%, saving 100+ hours per week."
            ]
        }
    ],
    "projects": [
        {
            "name": "Pustak (iOS App)",
            "link": "https://github.com/LMS–Team-8/Pustak",
            "description": "Pustak is a library management app built with SwiftUI and Firebase. It features personalized recommendations, book reservations, barcode scanning, fine management, and an analytics dashboard. The app adheres to Apple's design principles and ensures secure, real-time data synchronization."
        },
        {
            "name": "Mystic Deck (Educational IOS Games)",
            "link": "https://github.com/Hitarth00011/Mystic-Deck",
            "description": "Revolutionizing Indian education through engaging card games: fun, inclusive, and cost-effective, bridging learning gaps with interactive, localized content. Transforming Indian education with interactive card games: enjoyable, inclusive, economical, and culturally relevant, effectively addressing educational challenges."
        },
        {
            "name": "Stockiment",
            "link": "https://github.com/Hitarth00011/Stockiment.git",
            "description": "In this project, I utilized sentiment analysis and two machine learning models—Random Forest and Support Vector Regression (SVR)—to investigate the relationship between Twitter tweets and the stock market movements of a company. Sentiment analysis was performed on daily and hourly Twitter data to evaluate its impact on stock market predictions. The models were assessed and compared using RMSE (root mean squared error) values to measure their predictive accuracy."
        }
    ],
    "skills": {
        "technical": ["Python", "Swift UI", "UI/UX Design", "Jira", "HTML", "React"],
        "soft": ["Project Management", "Leadership", "Cross domain function", "Team building"]
    },
    "certifications": [
        "IOS Application Development - Infosys",
        "Oracle Certified Foundations Associate - ORACLE",
        "Fortinet Certified Associate in Cybersecurity - FORTINET Training Institute"
    ],
    "training_courses": [
        "Cloud Computing - IBM – Coursera",
        "Matlab Onramp - MathWorks",
        "Advances In Remote Sensing Techniques For Geological Applications - ISRO"
    ]
}

# Output the JSON
resume_json_string = json.dumps(resume_json, indent=4)
print(resume_json_string)





