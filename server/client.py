import asyncio
from langchain_openai import AzureChatOpenAI 
from dotenv import load_dotenv
from mcp_use import MCPAgent, MCPClient
import os


# client = AzureOpenAI(
#     azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
#     api_key=os.getenv("AZURE_OPENAI_API_KEY"),
#     api_version=os.getenv("AZURE_OPENAI_API_VERSION")
# )

# response = client.chat.completions.create(
#     model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
#     messages=[{"role": "user", "content": "Hello from Azure!"}]
# )

# print(response.choices[0].message.content)


async def run_memory_chat():
    """Run a chat using MCPAgent's built-in conversation memory."""
    load_dotenv()
    # os.environ('AZURE_OPENAI_API_KEY') = os.get_env('AZURE_OPENAI_API_KEY')
    # os.environ('OPENAI_API_VERSION') = os.get_env('AZURE_OPENAI_API_VERSION')
    # os.environ('AZURE_OPENAI_ENDPOINT') = os.get_env('AZURE_OPENAI_ENDPOINT')
    

    # MCP config file
    config_file = "server/weather.json"

    print("Initializing chat....")

    # Create MCP client and Agent with memory enabled
    client = MCPClient.from_config_file(config_file)

    llm = AzureChatOpenAI(azure_deployment='gpt-4o')

    agent = MCPAgent(
        llm=llm,
        client=client,
        memory_enabled=True,
        max_steps=15
    )


    print("\n=========== Interactive MCP Chat ===========")
    print("\nType 'exit' or 'quit' to end the conversation")
    print("\nType 'clear' to clear the conversation hitory")
    print("\n============================================")



    try:
        # Main chat loop
        while True:
            # Get user input
            user_input = input("\nYou:")

            # Check for exit command
            if user_input.lower() in ['exit', 'quit']:
                print("Ending conversation...")
                break

            # Check if clear command
            if user_input.lower() == 'clear':
                agent.clear_conversation_history()
                print("\nConversation history cleared.")
                continue

            # Get response form agent
            print("\nAssistant", end=" ", flush=True)

            try:
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"Error: {e}")

    finally:
        # Clear up
        if client and client.sessions:
            await client.close_all_sessions()


if __name__ == "__main__":
    asyncio.run(run_memory_chat())




    