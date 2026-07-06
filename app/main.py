from app.config import APP_NAME
from app.llm import ask_gemini
from app.logger import logger

def main():
    logger.info("Application started")
    print(f"Welcome to {APP_NAME}!")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("You: ")

        if prompt.lower() == "exit":
            print("Goodbye! 👋")
            logger.info("Application closed")
            break
        
        logger.info(f"User Prompt: {prompt}")
        
        try:
            response = ask_gemini(prompt)
            logger.info("Gemini response received")
            from app.utils import format_response
            print(format_response(response))

        except Exception as e:
            logger.error(f"Error: {e}")

        print("\nSomething went wrong while talking to Gemini.\n")


if __name__ == "__main__":
    main()