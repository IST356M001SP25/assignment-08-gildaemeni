# Reflection

Student Name:  Gilda Emeni
Sudent Email:  gemeni@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

**Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 

**Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
This was one of the most hands-on assignments we’ve done and it really helped me understand how data transformation connects directly to visualization. I used to think that once a dataset is “clean,” you can immediately visualize it, but I now see that even clean datasets often require another level of shaping. For example, the part in `etl.py` where we had to group by location and filter only those above $1,000 helped me get more comfortable with aggregation logic in pandas.

One part I struggled with at first was understanding why there were three different output files and what each was meant for. I kept mixing up the purpose of the `top_locations_mappable.csv` versus the one with all the individual tickets. After reviewing the tests and looking again at the instructions, it finally made sense that each file supported a different aspect of the dashboard. This kind of problem-solving taught me to slow down and connect what I’m writing to the bigger picture of the dashboard functionality.

Another challenge I faced was with the final dashboard using Streamlit. I originally used a different layout and color scheme from the solution and although it worked, it didn’t fully match the expected visual outcome. After reviewing the example screenshot, I adjusted my layout and styling while keeping the structure of my code different so I could maintain originality. This process helped me better understand how frontend presentation and backend logic work together in data apps.

Something that really clicked during this assignment was how valuable good column naming and structure can be. In my earlier projects, I didn’t think much about how I named variables or how I structured my code blocks, but when building dashboards that others might use or grade, clarity really matters. 

I feel more confident working with pandas, Streamlit, and charts now, and I want to keep practicing how to organize ETL pipelines and front-end dashboards together. My next goal is to explore interactivity in Streamlit more deeply and get more comfortable with customizing visuals without relying on defaults.
