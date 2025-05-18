from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

from thirdparty.linkedin import scrape_linkedin_profile
from agent.tool import grt_profile_url_tavily
if __name__=='__main__':
    # print("hello")
   
    
    # summary_template = """
    #     given the LinkedIn information {information} about a person I want you to create:
    #     1. A short summary
    #     2. two interesting facts about them.
    # """
    # prompt_template = PromptTemplate(
    #     input_variables=["information"],template=summary_template
    # )
    
    # llm = ChatOllama(model="llama3")
    # # llm = ChatOllama(model="mistral")
    # chain = prompt_template | llm | StrOutputParser()
    
    # linkedIn_data = scrape_linkedin_profile('https://www.linkedin.com/in/subham-kumar-singh-bb03001a0',1)
    
    # res =chain.invoke(input={"information": linkedIn_data})
    
    # print(res)
    


    linkedin_url = lookup(name="Subham Kumar Singh")
    print(linkedin_url)


