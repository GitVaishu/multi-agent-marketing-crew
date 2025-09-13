from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

load_dotenv()

# Simple LLM config
llm = LLM(
    model="groq/llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3,
    max_tokens=2000
)


class Content(BaseModel):
    topic: str = Field(..., description="The topic of the content")
    content: str = Field(..., description="The content itself")


@CrewBase
class TheMarketingCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.config = self.load_config(self.agents_config)
        self.tasks_config_obj = self.load_config(self.tasks_config)

    @staticmethod
    def load_config(config_path):
        import yaml
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_config_path = os.path.join(current_dir, config_path)
        with open(full_config_path, 'r') as file:
            return yaml.safe_load(file)

    # ALL AGENTS - NO TOOLS for now (to avoid errors)
    @agent
    def head_of_marketing(self) -> Agent:
        return Agent(
            role="Head of Marketing",
            goal="Lead marketing strategy and research",
            backstory="Experienced marketing professional with strategic planning skills",
            llm=llm,
            allow_delegation=True,
            max_delegation_rounds=1,
            max_iter=2,
            verbose=True
        )

    @agent
    def content_creator_social_media(self) -> Agent:
        return Agent(
            role="Social Media Content Creator",
            goal="Create engaging social media content",
            backstory="Creative professional skilled at social media content",
            llm=llm,
            max_iter=2,
            verbose=True,
            allow_delegation = False,
        )

    @agent
    def content_writer_blogs(self) -> Agent:
        return Agent(
            role="Blog Content Writer",
            goal="Write informative blog content",
            backstory="Skilled writer with SEO knowledge",
            llm=llm,
            max_iter=2,
            verbose=True,
            allow_delegation=False,
        )

    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            role="SEO Specialist",
            goal="Optimize content for search engines",
            backstory="Expert in SEO and content optimization",
            llm=llm,
            max_iter=2,
            verbose=True
        )

    @agent
    def content_writer_social_media(self) -> Agent:
        return Agent(
            role="Social Media Writer",
            goal="Write platform-specific social content",
            backstory="Writer who understands social media trends",
            llm=llm,
            max_iter=2,
            verbose=True,
            allow_delegation=False,
        )

    # SIMPLIFIED TASKS
    @task
    def market_research(self) -> Task:
        return Task(
            description="""Conduct market research on multi-agent intelligence trends. 
                You may ask the Blog Content Writer ONE question about current trends if needed, 
                but complete the majority of the research yourself.

                Product: {product_name}
                Audience: {target_audience}
                """,
            expected_output="Standalone market research report with key findings ",
            agent=self.head_of_marketing(),
            output_file="market_research.md" , # This will save to file!
            context=[]
        )

    @task
    def create_content_strategy(self) -> Task:
        return Task(
            description="Develop content strategy based on research",
            expected_output="Content strategy document",
            agent=self.head_of_marketing(),
            output_file="content_strategy.md"  # This will save to file!
        )

    @task
    def write_blog_post(self) -> Task:
        return Task(
            description="Write a blog post about multi-agent intelligence",
            expected_output="Well-written blog post",
            agent=self.content_writer_blogs(),
            output_file="blog_post.md"  # This will save to file!
        )

    @task
    def create_social_media_post(self) -> Task:
        return Task(
            description="Create social media content about the topic",
            expected_output="Engaging social media post",
            agent=self.content_creator_social_media(),
            output_file="social_media_post.md"  # This will save to file!
        )

    @task
    def optimize_seo(self) -> Task:
        return Task(
            description="Optimize the blog post for SEO",
            expected_output="SEO-optimized content",
            agent=self.seo_specialist(),
            output_file="seo_optimized_blog.md"  # This will save to file!
        )

    @crew
    def marketing_crew(self) -> Crew:
        """Creates the complete Marketing crew"""
        # ALL AGENTS
        agents = [
            self.head_of_marketing(),
            #self.content_creator_social_media(),
            self.content_writer_blogs(),
            #self.seo_specialist(),
            #self.content_writer_social_media()
        ]

        # ALL TASKS
        tasks = [
            self.market_research(),
            #self.create_content_strategy(),
            self.write_blog_post(),
            #sself.create_social_media_post(),
            #self.optimize_seo()
        ]

        return Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential,
            verbose=True,
            max_rpm=2,

        )