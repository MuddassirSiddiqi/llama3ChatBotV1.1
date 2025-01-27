# Llama3 ChatBot V1.1

Welcome to the Llama3 ChatBot V1.1 repository! This chatbot is built using **LangChain** and **Ollama**, leveraging the powerful **Llama3** model to provide conversational AI capabilities. Below, you'll find instructions on how to set up and run the chatbot on your local machine.

---

## Repository Link
[https://github.com/MuddassirSiddiqi/llama3ChatBotV1.1](https://github.com/MuddassirSiddiqi/llama3ChatBotV1.1)

---

## Prerequisites

Before running the chatbot, ensure you have the following installed:

1. **Python 3.8 or higher**: The code is written in Python, so you'll need Python installed on your system.
2. **Ollama**: The chatbot uses the Ollama framework to interact with the Llama3 model. Make sure Ollama is installed and running on your machine. You can find installation instructions [here](https://ollama.ai/).

---

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/MuddassirSiddiqi/llama3ChatBotV1.1.git
cd llama3ChatBotV1.1
```

### 2. Create a Virtual Environment
It's recommended to use a virtual environment to manage dependencies. Run the following commands to create and activate a virtual environment:

- **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

### 3. Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install langchain-ollama langchain-core
```

---

## Running the ChatBot

Once the setup is complete, you can run the chatbot by executing the following command:
```bash
python chatbot.py
```

### How It Works
1. The chatbot will greet you with a welcome message.
2. Type your question or input, and the chatbot will respond.
3. To exit the chatbot, type `exit`.

---

## Code Overview

The chatbot is built using the following components:

### 1. **OllamaLLM**
   - This is the wrapper for the **Llama3** model, which is used to generate responses to user inputs.

### 2. **ChatPromptTemplate**
   - Defines the structure of the conversation. It includes a template that provides context and a placeholder for the user's question.

### 3. **Conversation History**
   - The chatbot maintains a history of the conversation to provide context for future responses. If the conversation becomes too long, it is summarized to avoid exceeding token limits.

### Key Functions

#### `summarize_context(context)`
   - This function checks if the conversation history exceeds a certain length (e.g., 500 words). If it does, the history is summarized to keep it concise.

#### `handle_conversation()`
   - This is the main function that handles the conversation loop. It:
     1. Initializes the conversation history.
     2. Takes user input.
     3. Invokes the LangChain pipeline to generate a response.
     4. Updates the conversation history with the new interaction.
     5. Summarizes the history if necessary.

---

## Code

Here is the complete code for the chatbot:

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
```

---

## Dependencies
The following Python packages are required:
- `langchain-ollama`: For integrating Ollama with LangChain.
- `langchain-core`: Core components for building LangChain applications.

---

## Troubleshooting
- **Ollama Not Running**: Ensure Ollama is installed and running on your machine. You can test it by running `ollama serve` in your terminal.
- **Dependency Issues**: If you encounter issues with dependencies, try reinstalling them using `pip install -r requirements.txt` (if a `requirements.txt` file is provided).

---

## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Your feedback and improvements are welcome!

---

## License
This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Enjoy chatting with Llama3 ChatBot V1.1! 🚀
