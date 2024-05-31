import os
from langchain_aws import BedrockLLM
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def Bedrock_llm():
    llm = BedrockLLM(
        credentials_profile_name="default",
        model_id="meta.llama2-70b-chat-v1",
        model_kwargs={
            "max_gen_len": 100,  # Set a limit on generation length
            "temperature": 0.5,  # Control randomness
            "top_p": 0.9         # Control the nucleus of response
            # You might also add "stop_sequences" if the API supports it
        }
    )
    return llm

def chat_memory():
    memory = ConversationBufferMemory(memory_key='history', max_token_limit=512)
    return memory

def reset_memory(memory):
    memory.clear()  # This method depends on the implementation of your memory class.


def chat_conversation(input_text, memory):
    llm_chain_data = Bedrock_llm()
    llm_conversation = ConversationChain(
        llm=llm_chain_data, 
        memory=memory, 
        verbose=True,
        # Remove the model_kwargs parameter
    )
    
    chat_reply = llm_conversation.invoke(input={"input": input_text})
    if 'response' in chat_reply:
        return chat_reply['response']
    else:
        return "No valid response received"



