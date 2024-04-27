from typing import List, Union
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from fastapi.middleware.cors import CORSMiddleware
from langserve.pydantic_v1 import BaseModel, Field
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai",
)


add_routes(
    app,
    ChatAnthropic(
        model_name="claude-3-opus-20240229"
    ),
    path="/anthropic",
)


model = ChatAnthropic(
     model_name="claude-3-opus-20240229"
)
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
add_routes(
    app,
    prompt | model,
    path="/joke",
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful, professional assistant named Ayyaz."),
        MessagesPlaceholder(variable_name="messages"),
    ]
)
chain = prompt | ChatAnthropic(model="claude-3-opus-20240229")


class InputChat(BaseModel):
    """Input for the chat endpoint."""

    messages: List[Union[HumanMessage, AIMessage, SystemMessage]] = Field(
        ...,
        description="The chat messages representing the current conversation.",
    )



add_routes(
    app,
    chain.with_types(input_type=InputChat),
    enable_feedback_endpoint=True,
    enable_public_trace_link_endpoint=True,
    playground_type="chat",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
