from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the conversation template
template = """
You are a helpful and knowledgeable assistant. Answer the question clearly and concisely.
Here is the Conversation History:
{context}

Question: {question}
Answer:
"""

# Initialize the model and prompt
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def summarize_context(context):
    if len(context.split()) > 500:  # Example threshold
        return summarize_text(context)
    return context

def handle_conversation():
    context = ""  # Initialize conversation history
    print("Welcome to nanoVoltz's ChatBot. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ").strip()  # Get user input
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        if not user_input:
            print("Bot: Please type something.")
            continue
        
        try:
            # Invoke the chain with current context and user input
            result = chain.invoke({"context": context, "question": user_input})
            print("Bot:", result)
            
            # Update and summarize context
            context += f"\nUser: {user_input}\nAI: {result}"
            context = summarize_context(context)
        except Exception as e:
            print(f"Bot: Sorry, an error occurred: {e}")

if __name__ == "__main__":
    handle_conversation()
