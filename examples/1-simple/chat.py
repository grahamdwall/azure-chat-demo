#from dotenv import load_dotenv
#import os
#from os.path import dirname
#import semantic_kernel as sk
#from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

#current_dir = dirname(os.path.abspath(__file__))
#root_dir = dirname(dirname(current_dir))
#env_file = os.path.join(root_dir, '.env')

#async def main():
#    # Load the .env file. Replace the path with the path to your .env file.
#    load_dotenv(env_file)
#    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
#    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
#    api_key = os.environ["AZURE_OPENAI_API_KEY"]

#    kernel = sk.Kernel()

#    kernel.add_chat_service("dv", AzureChatCompletion(
#        deployment_name=deployment_name,
#        endpoint=endpoint,
#        api_key=api_key)
#    )

#    # Wrap your prompt in a function
#    prompt = kernel.create_semantic_function("""
#    I need to understand what are the variables involved in making outstanding espresso besides
#    a good machine. For example what is the combination of roast, grind, tamp, and water temperature.
#    Include 3 practical steps to practice and improve each variable.
#    """)

#    # Run your prompt
#    print(prompt())


# Run the main function
#if __name__ == "__main__":
#    import asyncio

#    asyncio.run(main())



import os
from openai import AzureOpenAI

openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")

endpoint = "https://graha-m8amde0y-eastus2.openai.azure.com/"
model_name = "gpt-4o"
deployment = "gpt-4o"

subscription_key = openai_api_key
api_version = "2024-02-15-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    model=model_name
)

print(response.choices[0].message.content)

