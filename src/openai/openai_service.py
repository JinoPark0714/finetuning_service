from src.openai.openai_config import get_openai_object

def get_ai_response(message):
    try:
        response = get_openai_object().chat.completions.create(
            model="gpt-3.5-turbo-1106", 
            messages=[*message],
            temperature=0.9,
            max_tokens=300,
            top_p=0.8,
            frequency_penalty=1,
            presence_penalty=0.4
        )
        message = response.choices[0].message.content
        return message
    except Exception as e:
        print(f"An error occurred: {e}")
        raise "An error occurred while processing your request."

def print_response(message):
    try:
        response = get_openai_object().chat.completions.create(
            model="gpt-3.5-turbo-1106", 
            messages=[*message],
            temperature=0.9,
            max_tokens=300,
            stream=True
        )
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
        print("")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise "An error occurred while processing your request."