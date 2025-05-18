import os
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain_core.prompts import PromptTemplate

from langchain_core.tools import Tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain_google_genai import ChatGoogleGenerativeAI

def grt_profile_url_tavily(name:str):
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res

def lookup(name:str)->str:
    # llm =  ChatOllama(model="llama3")
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key = os.environ['GOOGLE_API_KEY'],
)
    
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                          Your answer should contain only a URL"""
                          
    prompt_template = PromptTemplate(
        template=template,input_variables=["name_of_person"]
    )
    
    agents_tool = [
        Tool(
            name = "Crawl Google 4 linkedin profile page",
            func= grt_profile_url_tavily,
            description="useful for when you need get the LinkedIn Page URL"
        )
    ]
    
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm,tools =agents_tool,prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent,tools= agents_tool,verbose=True)
    
    result = agent_executor.invoke(
        input={"input":prompt_template.format_prompt(name_of_person=name)}
    )
    
    linkedin_profile =result["output"]
    return linkedin_profile

if __name__=="__main__":
    linkedin_url = lookup(name="Subham Kumar Singh")
    # x= os.environ["GOOGLE_API_KEY"]
    print(linkedin_url)
    # print(x)
