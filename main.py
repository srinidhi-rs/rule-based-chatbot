import gradio as gr

# Simple chatbot function using if-else and pattern matching
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hey there", "hi", "hello"]:
        return "Hello! How can I help you today?"
    elif "how's everything" in user_input or "how are you" in user_input:
        return "I'm doing great, thanks for asking! How about you?"
    elif "what should i call you" in user_input:
        return "You can call me your friendly assistant!"
    elif "who made you" in user_input:
        return "I was crafted by Srinidhi!"
    elif "what is your purpose" in user_input:
        return "I’m here to chat and provide you with any answers you need."
    elif "time" in user_input:
        return "I don’t have a clock, but you can check the time on your device."
    elif "tell me a joke" in user_input:
        return "Why did the computer go to the doctor? Because it had a virus!"
    elif "forecast" in user_input or "weather" in user_input:
        return "I don't have live weather updates, but I bet it’s sunny in the digital world!"
    elif "favorite color" in user_input or "favorite hue" in user_input:
        return "I like green—reminds me of fresh, clean code."
    elif user_input in ["goodbye", "see ya"]:
        return "Farewell! Have a fantastic day ahead!"
    elif "thank" in user_input:
        return "You're very welcome! It was a pleasure talking to you."
    elif "how old are you" in user_input:
        return "I'm ageless, just a program that stays up to date."
    elif "do you enjoy music" in user_input:
        return "Yes! I love all kinds of sounds—especially those that come from the keyboard."
    elif "where do you live" in user_input:
        return "I live in the cloud, far away from physical space!"
    elif "are you human" in user_input:
        return "No, but I’m designed to talk like one!"
    elif "feel" in user_input:
        return "I don't feel emotions, but I can understand them."
    elif "friend" in user_input:
        return "I’m always here for you. Yes, we can be friends!"
    elif "fun fact" in user_input:
        return "Did you know octopuses have three hearts? How cool is that!"
    elif "capital of japan" in user_input:
        return "Tokyo is the capital of Japan."
    elif "capital of canada" in user_input:
        return "Ottawa is the capital of Canada."
    elif "4 plus 6" in user_input:
        return "10"
    elif "10 minus 3" in user_input:
        return "7"
    elif "9 times 5" in user_input:
        return "45"
    elif "24 divided by 4" in user_input:
        return "6"
    else:
        return "Sorry, I don't understand that. Can you try asking something else?"

# Create Gradio interface
iface = gr.Interface(
    fn=chatbot_response,
    inputs="text",
    outputs="text",
    title="Simple Rule-Based Chatbot",
    description="Chat with a basic chatbot! Built by Srini."
)

# Launch the chatbot
iface.launch()
