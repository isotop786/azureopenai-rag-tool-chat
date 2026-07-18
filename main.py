import os
import glob
from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

def main():
    os.system("cls" if os.name =="nt" else "clear")

    try:
        load_dotenv(override=True)

        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")

        # Initialize
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(),
            "https://ai.azure.com/.default",
        )

        openai_client = OpenAI(
            base_url=azure_openai_endpoint,
            api_key=token_provider
        )

        ## Create vector store and upload files
        print("Creating vector store and uploading files...")

        vector_store = openai_client.vector_stores.create(
            name="travel-brochures",
        )

        file_streams = [open(f,"rb") for f in glob.glob("Brochures/*.pdf")]

        if not file_streams:
            print("No Brochures files found.")
            return
        file_batch = openai_client.vector_stores.file_batches.upload_and_poll(
            vector_store_id=vector_store.id,
            files=file_streams
        )

        for f in file_streams:
            f.close()

        print(f"Vectore store created with {file_batch.file_counts.completed} files.")

        # Track conversation state
        last_response_id = None

        # Loop until the user wants to quit
        while True:
            input_text = input("*****ENTER A QUESTION (or Type 'quit' to exit):'): ")
            if input_text.lower() == "quit":
                break
            if len(input_text.strip()) == 0:
                print("Please enter a question.")
                continue

            # Get a response using tools
            response = openai_client.responses.create(
                model=model_deployment,
                instructions="""You are a travel assitant that provides information on travel services and answer
                question about services offered by Margie's Travel using the provided documents and search the web
                for general information about destination or current travel""",
                input=input_text,
                previous_response_id=last_response_id,
                tools=[
                    {
                        "type": "file_search",
                        "vector_store_ids": [vector_store.id],
                    },
                    {
                        "type":"web_search",
                    }
                ]
            )

            print(response.output_text)
            last_response_id=response.id

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()