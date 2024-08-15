from groq import Groq

client = Groq(
    api_key="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"
)

prompt = f"""
YOUR RESPONSE SHOULD ONLY BE JSON, NO ADDED TEXT BEFORE OR AFTER THE JSON... JUST JSON! THIS IS VERY IMPORTANT!
Based off the user input data, generate the most optimal exam reading schedule for this student in this format:
// Output
interface examSchedule {{
    exam_duration: number // Total days for exams
    schedule: reading [] // reading schedule
}}

interface courseSchedule {{
    course_name: string; // course name
    exam_date: Date; // exam date
    days_till_exam: number; // days til exam_date
    priority: number; // how important a course is
    difficulty: number; // how hard a course is
    percent_of_study_time: number // percentage of daily_study_time allocated
}}

interface reading {{
    day: number; // day number in the schedule
    courses: courseSchedule[]; // courses to be read on this day
    daily_study_time: number; // daily time (hours) spent studying
    inbetween_breaks: number; // amount of time taken (minutes) as breaks in between studying
}}
Generate as JSON
"""

def groq_reply(input):
    
    user_input = f"{input}"
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input,}
        ],
        model="llama3-70b-8192",
    )

    reply = chat_completion.choices[0].message.content
    print(reply)
    
    return reply