# from langchain.schema import SystemMessage, HumanMessage
# from langchain.prompts import ChatPromptTemplate
# from langchain.schema.runnable import RunnableMap
# from langserve import RemoteRunnable
# import asyncio


# openai =  RemoteRunnable("http://localhost:8000/openai/")
# anthropic = RemoteRunnable("http://localhost:8000/anthropic/")
# joke_chain = RemoteRunnable("http://localhost:8000/joke/")

# response = joke_chain.invoke({"topic": "parrots"})
# print(response)

# prompt = [
#     SystemMessage(content='Act like either a cat or a parrot.'),
#     HumanMessage(content='Hello!')
# ]

# # Supports astream
# async def test():
#     async for msg in anthropic.astream(prompt):
#         print(msg, end="", flush=True)



# asyncio.run(test())



import requests
response = requests.post(
    "http://localhost:8000/joke/invoke",
    json={'input': {'topic': 'cats'}}
)
print(response.json())
