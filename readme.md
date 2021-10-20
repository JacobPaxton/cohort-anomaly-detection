# Project Overview
Answer specific analytic questions from an email regarding Codeup's online curriculum traffic.

# Email Verbatim
"Hello, I have some questions for you that I need to be answered before the board meeting Friday afternoon. I need to be able to speak to the following questions. I also need a single slide that I can incorporate into my existing presentation (Google Slides) that summarizes the most important points. My questions are listed below; however, if you discover anything else important that I didn’t think to ask, please include that as well.

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed?
8. Anything else I should be aware of?"

# Project Plan
1. Acquire data from the SQL database
    * Use an acquire.py script to automate acquisition
2. Anonymize IP addresses in the data by turning last three digits into zeroes
3. Build a dataframe for each question (each contains only the columns of interest)
    * Use a prepare.py script to automate this isolation
4. Answer each question
    * Include visualizations in the final notebook for each question
5. Create, solidify all deliverables
6. With extra time, explore the data further for additional insights
7. With extra time, add the new insights to the deliverables
8. Send off the email containing everything as requested