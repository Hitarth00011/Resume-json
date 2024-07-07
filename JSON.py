import pdfplumber
import re
import json

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def parse_resume_text(text):
    lines = text.split('\n')
    resume_data = {}
    
    # Parsing Contact Information
    resume_data["Name"] = lines[0].strip()
    resume_data["Degree"] = lines[1].strip()
    contact_info = {}
    contact_info["Phone"] = re.search(r'Ph: ([\+\d-]+)', text).group(1)
    contact_info["Email"] = re.search(r'Email: (\S+)', text).group(1)
    contact_info["Address"] = re.search(r'(Chengalpattu, Tamil Nadu, India - \d+)', text).group(1)
    contact_info["LinkedIn"] = re.search(r'(https://www.linkedin.com/in/\S+)', text).group(1)
    resume_data["Contact Information"] = contact_info
    
    # Parsing Brief Summary
    summary_index = lines.index("BRIEF SUMMARY") + 1
    resume_data["Summary"] = lines[summary_index].strip()
    
    # Parsing Key Expertise
    expertise_index = lines.index("KEY EXPERTISE") + 1
    expertise = []
    while lines[expertise_index].strip() != "":
        expertise.append(lines[expertise_index].strip())
        expertise_index += 1
    resume_data["Skills"] = expertise
    
    # Parsing Education
    education_index = lines.index("EDUCATION") + 1
    education = []
    while lines[education_index].strip() != "AWARDS AND SCHOLARSHIPS":
        institution = {}
        institution["Institution"] = lines[education_index].strip()
        education_index += 1
        institution["Degree"] = lines[education_index].split('|')[0].strip()
        institution["Period"] = lines[education_index].split('|')[1].strip()
        if "CGPA" in lines[education_index]:
            institution["CGPA"] = re.search(r'CGPA: (\S+)', lines[education_index]).group(1)
        if "Percentage" in lines[education_index]:
            institution["Percentage"] = re.search(r'Percentage: (\S+)', lines[education_index]).group(1)
        education.append(institution)
        education_index += 1
    resume_data["Education"] = education
    
    # Parsing Awards and Scholarships
    awards_index = lines.index("AWARDS AND SCHOLARSHIPS") + 1
    awards = []
    while lines[awards_index].strip() != "INTERNSHIPS":
        awards.append(lines[awards_index].strip())
        awards_index += 1
    resume_data["Awards and Scholarships"] = awards
    
    # Parsing Internships
    internships_index = lines.index("INTERNSHIPS") + 1
    internships = []
    while lines[internships_index].strip() != "PROJECTS":
        internship = {}
        internship["Period"] = lines[internships_index].strip()
        internships_index += 1
        internship["Company"] = lines[internships_index].strip()
        internships_index += 1
        internship["Role"] = lines[internships_index].strip()
        internships_index += 1
        skills = []
        while lines[internships_index].strip() != "":
            skills.append(lines[internships_index].strip())
            internships_index += 1
        internship["Key Skills"] = skills
        internships.append(internship)
        internships_index += 1
    resume_data["Experience"] = internships
    
    # Parsing Projects
    projects_index = lines.index("PROJECTS") + 1
    projects = []
    while lines[projects_index].strip() != "CERTIFICATIONS":
        project = {}
        project["Period"] = lines[projects_index].strip()
        projects_index += 1
        project["Title"] = lines[projects_index].strip()
        projects_index += 1
        skills = []
        while lines[projects_index].strip() != "Project Link:":
            skills.append(lines[projects_index].strip())
            projects_index += 1
        project["Key Skills"] = skills
        projects_index += 1
        project["Link"] = lines[projects_index].strip()
        projects.append(project)
        projects_index += 1
    resume_data["Projects"] = projects
    
    # Parsing Certifications
    certifications_index = lines.index("CERTIFICATIONS") + 1
    certifications = []
    while lines[certifications_index].strip() != "SEMINARS / TRAININGS / WORKSHOPS":
        certification = {}
        certification["Title"] = lines[certifications_index].strip()
        certifications_index += 1
        certification["Aggregate"] = re.search(r'Aggregate: (\S+)', lines[certifications_index]).group(1)
        skills = []
        while lines[certifications_index].strip() != "":
            skills.append(lines[certifications_index].strip())
            certifications_index += 1
        certification["Key Skills"] = skills
        certifications.append(certification)
        certifications_index += 1
    resume_data["Certifications"] = certifications
    
    # Parsing Workshops
    workshops_index = lines.index("SEMINARS / TRAININGS / WORKSHOPS") + 1
    workshops = []
    while lines[workshops_index].strip() != "CO-CURRICULAR ACTIVITIES":
        workshop = {}
        workshop["Period"] = lines[workshops_index].strip()
        workshops_index += 1
        workshop["Title"] = lines[workshops_index].strip()
        workshops_index += 1
        workshop["Institute"] = lines[workshops_index].strip()
        workshops_index += 1
        skills = []
        while lines[workshops_index].strip() != "":
            skills.append(lines[workshops_index].strip())
            workshops_index += 1
        workshop["Key Skills"] = skills
        workshops.append(workshop)
        workshops_index += 1
    resume_data["Workshops"] = workshops
    
    # Parsing Co-curricular Activities
    co_curricular_index = lines.index("CO-CURRICULAR ACTIVITIES") + 1
    co_curricular = []
    while lines[co_curricular_index].strip() != "EXTRA CURRICULAR ACTIVITIES":
        co_curricular.append(lines[co_curricular_index].strip())
        co_curricular_index += 1
    resume_data["Co-curricular Activities"] = co_curricular
    
    # Parsing Extra-curricular Activities
    extra_curricular_index = lines.index("EXTRA CURRICULAR ACTIVITIES") + 1
    extra_curricular = []
    while lines[extra_curricular_index].strip() != "PERSONAL INFORMATION":
        extra_curricular.append(lines[extra_curricular_index].strip())
        extra_curricular_index += 1
    resume_data["Extra-curricular Activities"] = extra_curricular
    
    # Parsing Personal Information
    personal_info_index = lines.index("PERSONAL INFORMATION") + 1
    personal_info = {}
    personal_info["Gender"] = re.search(r'Gender: (\w+)', text).group(1)
    personal_info["Marital Status"] = re.search(r'Marital Status: (\w+)', text).group(1)
    personal_info["Current Address"] = re.search(r'Current Address: (.+)', text).group(1)
    personal_info["Date of Birth"] = re.search(r'Date of Birth: (\d+ \w+, \d+)', text).group(1)
    personal_info["Known Languages"] = re.search(r'Known Languages: (.+)', text).group(1).split(', ')
    personal_info["Permanent Address"] = re.search(r'Permanent Address: (.+)', text).group(1)
    personal_info["Phone Numbers"] = re.findall(r'Phone Numbers: (\+\d+-\d+)', text)
    personal_info["Emails"] = re.findall(r'Emails: (\S+)', text)
    resume_data["Personal Information"] = personal_info
    
    return resume_data

def main():
    pdf_path = "/mnt/data/Hitarth 7th sem.pdf"
    resume_text = extract_text_from_pdf(pdf_path)
    resume_json = parse_resume_text(resume_text)
    print(json.dumps(resume_json, indent=4))

if __name__ == "__main__":
    main()









