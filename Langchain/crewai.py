from crewai import Agent, Crew, Process, Task

from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()

# Enable debug logging for LLM calls

import litellm

litellm._turn_on_debug()

blog_outline_generator = Agent(

    role="Blog Outline Generator",

    goal="Given a title: {blog_title}, generate a short blog outline which is only 100 words and only 5 subheadings which will be used to write a blog post with 2000 words",

    backstory="You are a blog outline generator"

)

generate_blog_outline_task = Task(

    description="Given a title: {blog_title}, generate a short blog outline which is only 100 words and only 5 subheadings which will be used to write a blog post with 2000 words",

    expected_output="A blog outline",

    agent=blog_outline_generator,

)

blog_writer = Agent(

    role="Blog Writer",

    goal="Given a blog outline for the title: {blog_title}, write a blog post with 2000 words",

    backstory="You are a blog writer"

)   

write_blog_task = Task(

    description="Given a blog outline for the title: {blog_title}, write a blog post with 2000 words",

    expected_output="A blog post, make sure to include main points from blog outline which you have received in the context in the blog post as subheadings",

    agent=blog_writer,

    context=[generate_blog_outline_task]

)

crew = Crew(

    agents=[blog_outline_generator, blog_writer],

    tasks=[generate_blog_outline_task, write_blog_task],

    process=Process.sequential,

    verbose=True

)

result = crew.kickoff(inputs={'blog_title': "Violence in movies"})
print(result)