# nanoVoltz's ChatBot

This is an interactive chatbot built using `langchain_ollama` and `llama3` model for handling conversations in a natural way. The chatbot can process user input, maintain conversation history, and provide helpful responses.

## Features

- **Improved Conversation Template**: The chatbot responds clearly and concisely to the user's question while taking into account the conversation history.
- **Context Summarization**: If the conversation history exceeds a certain word threshold (500 words), the context is summarized to improve efficiency and avoid overloading the model.
- **Input Validation**: The chatbot checks for empty inputs and prompts the user to provide valid input.
- **Error Handling**: If any error occurs during the execution, the chatbot gracefully handles it and provides an error message.

## Code Explanation

### Conversation Flow

1. **Template Setup**: The conversation template is defined with placeholders for the context (previous conversation history) and the current question from the user.
2. **Model and Prompt Initialization**: The `OllamaLLM` model (with "llama3") is initialized along with a prompt that is created from the defined template.
3. **Context Summarization**: The `summarize_context` function checks if the conversation history exceeds a threshold (500 words). If so, it triggers the `summarize_text` function to reduce the length of the context, which helps in maintaining the efficiency of the conversation.
4. **Main Loop**: The bot prompts the user for input, processes the input, and displays the response while maintaining and updating the conversation history.

### Code

```python
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
