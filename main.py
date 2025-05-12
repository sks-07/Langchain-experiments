# from langchain_core.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI

# if __name__=='__main__':
#     print("hello")
#     print(os.environ['OPENAI_API_KEY'])

from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
)

chat = ChatHuggingFace(llm=llm, verbose=True)
messages = [
    ("system", "You are a helpful translator. Translate the usersentence to French."),
    ("human", "I love programming."),
]

chat(...).invoke(messages)
