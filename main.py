from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

if __name__=='__main__':
    print("hello")
    information = """
    Ronaldo made his international debut for Portugal in 2003 at the age of 18 and has earned more than 200 caps, making him history's most-capped male player.[8] Ronaldo has played in eleven major tournaments and scored in ten; he scored his first international goal at Euro 2004, where he helped Portugal reach the final and subsequently made the team of the tournament. In the 2006 FIFA World Cup, his first World Cup, he was a focal part to Portugal ultimately finishing in fourth place. He assumed captaincy of the national team in July 2008 ahead of Euro 2008; four years later, at Euro 2012, he was named to the team of the tournament. In 2015, Ronaldo was named the best Portuguese player of all time by the Portuguese Football Federation. The following year, he led Portugal to their first major tournament title at Euro 2016, being named in the team of the tournament for the third time and receiving the Silver Boot as the second-highest goalscorer of the tournament. This achievement saw him receive his fourth Ballon d'Or. In 2018, Ronaldo had his most prolific World Cup campaign and was voted in the Fan Dream Team. He led his country to victory in the inaugural UEFA Nations League in 2019, receiving the top scorer award in the finals, and also received the Golden Boot as top scorer of Euro 2020. In the 2022 World Cup, he became the first player to score at five World Cups.
    """
    
    summary_template = """
        given the information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them.
    """
    prompt_template = PromptTemplate(
        input_variables=["information"],template=summary_template
    )
    
    llm = ChatOllama(model="llama3")
    # llm = ChatOllama(model="mistral")
    chain = prompt_template | llm | StrOutputParser()
    
    res =chain.invoke(input={"information": information})
    
    print(res)
    
    


