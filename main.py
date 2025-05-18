from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain_core.output_parsers import StrOutputParser

from thirdparty.linkedin import scrape_linkedin_profile
from output_parsers import summary_parser
from agent.linkedin_agent import lookup

def summarize(name:str)->str:
    linkedin_username = lookup(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_URL=linkedin_username,Trial=False)
    summary_template = """
        given the LinkedIn information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them.
        
        \n{format_instructions}
    """
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        google_api_key = os.environ['GOOGLE_API_KEY'],
        )
    
    summary_prompt_template= PromptTemplate(
        input_variables=["information"],template=summary_template,
        partial_variables={
            "format_instructions":summary_parser.get_format_instructions()
        }
    )
    
    chain = summary_prompt_template | llm | summary_parser
    res = chain.invoke(input={"information":linkedin_data})
    print(res)

if __name__=='__main__':
   summarize(name="subham kumar singh")


