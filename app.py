from agent import create_agent
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
    
@cl.on_message
async def main(message: str):
    # Your custom logic goes here...

    # Send a response back to the user
    from agent import texts
    filing_content = texts[0]
    output = agent_chain.run(filing_content)

    await cl.Message(
        content=f"Xinyu says: {output}",
    ).send()
