from openai import AzureOpenAI

# 이 "..." 부분을 채워 Azure OpenAI를 코드와 연결하세요
AZURE_OPENAI_ENDPOINT="https://....openai.azure.com/"
AZURE_OPENAI_API_KEY="....."
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="gpt-4o"
AZURE_OPENAI_API_VERSION="2023-12-01-preview"

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    base_url=f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_OPENAI_CHAT_DEPLOYMENT_NAME}"
)

print("Chatbot: 안녕하세요! 무엇을 도와드릴까요? 종료하려면 'exit'를 입력하세요.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: 대화를 종료합니다. 좋은 하루 보내세요!")
        break
    response = client.chat.completions.create(
        model=AZURE_OPENAI_MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=200
    )
    print("Chatbot:", response.choices[0].message.content.strip())



