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

# Answers to email
1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
    1. PHP: **content/html-css** (262)
    2. Java: **javascript-i/introduction/working-with-data-types-operators-and-variables** (7094)
    3. DS: **classification/overview** (1785)
    4. Front End: **content/html-css**
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
    - **Voyageurs: java-i/introduction-to-java** (447) - 3x the average - 22% higher than next cohort
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
    - **Yes**; PHP and Java students make up nearly all of bottom 100
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
    1. Unauthorized access: **No**, all events have associated user id
    2. Web scraping: **Probably**, there's lots of .html, .json, and .php requests
    3. Suspicious IP addresses: **I'd say no**, all events have associated user id
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
    1. Cross-Access: **Yes**, A user from Teddy (Java) accessed the DS Classification module twice in 2020
    2. Happen Before: **I don't know, the first DS cohort was mid-2019 and the ability changed in 2019**
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
    - Nearly all of top-referenced lessons are in the **Fundamentals module**
7. Which lessons are least accessed?
    - There are a lot of paths that seem to be lessons but only have one request- are they deprecated? I don't feel confident choosing any.
8. Anything else I should be aware of?
    - If you're focused on reducing student reference to the curriculum, let me know, I can look into that further.
    - If you're focused on identifying potential unauthorized access to the curriculum, let me know, I can look into that further.