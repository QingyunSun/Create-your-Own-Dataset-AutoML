from agent import create_agent, get_pickle_files, get_text
import chainlit as cl

agent_chain = create_agent()

# @cl.langchain_factory(use_async=False)
# def main():
#     return agent_chain 

# @cl.langchain_run
# async def run(agent, input_str):
#     from agent import texts
#     input_str = texts[0]
#     res = await cl.make_async(agent)(input_str, callbacks=[cl.ChainlitCallbackHandler()])
#     await cl.Message(content=res["output"]).send()

pickle_dict = get_pickle_files('./data')
print("loaded the pickle dict: ", pickle_dict)
    
@cl.on_message
async def main(message: str):
    print(message)
    # Your custom logic goes here...
    filename, section = message.split(' ')
    print("filename session: ", filename, section)
    # Send a response back to the user
    filing_content = get_text(pickle_dict, filename, section)
    output = agent_chain.run(filing_content)

    await cl.Message(
        content=f"Xinyu says: {output}",
    ).send()
