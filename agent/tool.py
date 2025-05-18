from langchain_community.tools.tavily_search import TavilySearchResults

def grt_profile_url_tavily(name:str):
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res

if __name__=="__main__":
    print(grt_profile_url_tavily("Who won the last fifa world cup"))