# Dependencies
import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")

# Setting up the model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

# Defining Conversation memory (We use the Conversation Buffer Memory for now)
memory = ConversationBufferMemory(return_messages = True)

# Defining the conversation chain
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)

# Conversation Simulation
while(True):
    prompt = input()
    if(prompt == "EXIT"):
        break
    else:
        print(conversation.predict(input = prompt))
