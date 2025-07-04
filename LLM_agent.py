from langchain_ollama import ChatOllama

#initialising the model, running on local host
llm = ChatOllama(model='llama3.2:latest', base_url='http://localhost:11434')

def LLM_call(user_input):
    response = llm.invoke(f"what are the most relevant problems the user input {user_input} might have?")
    return response.content


