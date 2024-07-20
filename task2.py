import nltk
from nltk.chat.util import Chat, reflections
from introduction import introduction_pairs  # Import pairs from the separate file
from science import science_pairs
from sports import sports_pairs
from trivia import trivia_pairs

# Create a chatbot instance
conversations = trivia_pairs + science_pairs + sports_pairs + introduction_pairs

chatbot = Chat(conversations, reflections) 

# Start the conversation
print("HELLO ")
print("I am a Chatbot")
print("How can I help you?")
print("To exit, type 'quit' ")
chatbot.converse()