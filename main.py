# ==============================
# ENV SETUP
# ==============================
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


# ==============================
# IMPORTS
# ==============================
from crewai import Agent, Task, Crew, Process
from crewai_tools import YoutubeChannelSearchTool
from langchain_google_genai import ChatGoogleGenerativeAI

# ==============================
# LLM SETUP (Gemini 2.5 Flash)
# ==============================
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4
)

# ==============================
# TOOL SETUP
# ==============================
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='@krishnaik06'
)

# ==============================
# AGENTS
# ==============================

blog_researcher = Agent(
    role="Blog Researcher from Youtube Videos",
    goal="Get relevant video transcription for the topic {topic} from the provided YouTube channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos related to AI, Data Science, "
        "Machine Learning, Deep Learning and Generative AI."
    ),
    tools=[yt_tool],
    llm=llm,               # ✅ Gemini attached
    allow_delegation=True
)

blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from YouTube",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate."
    ),
    tools=[yt_tool],
    llm=llm,               # ✅ Gemini attached
    allow_delegation=False
)

# ==============================
# TASKS
# ==============================

research_task = Task(
    description=(
        "Identify the video related to {topic}. "
        "Extract detailed and relevant information from the YouTube channel."
    ),
    expected_output=(
        "A comprehensive 3-paragraph research report based on the video content."
    ),
    agent=blog_researcher,
)

write_task = Task(
    description=(
        "Use the researched content and create a well-structured blog post "
        "about {topic}."
    ),
    expected_output=(
        "A clear, engaging, and informative blog post summarizing the YouTube video."
    ),
    agent=blog_writer,
    output_file="new-blog-post.md"
)

# ==============================
# CREW
# ==============================

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=60
)

# ==============================
# RUN
# ==============================

if __name__ == "__main__":
    result = crew.kickoff(
        inputs={"topic": "AI vs ML vs DL vs Data Science"}
    )
    print(result)
