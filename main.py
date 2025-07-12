from message_translator import MessageTranslation
from Test.morse_test_variables import *
from art import display_art



if __name__ == "__main__":

    display_art()
    translator = MessageTranslation()

    is_encode = input("Type E to encode, D to decode:  ").upper().startswith('E')
    message = input("What is the message: ")
    translator.translate_message(
        in_stream=message, 
        encode=is_encode, 
        standard='american'
        )
    
    