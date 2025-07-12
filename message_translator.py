from morse_code import morse_code, WORD_PACKING, LETTER_PACKING, INTERNATIONAL


class MessageTranslation:
    """Morse Code Translator"""
    def __init__(self):
        pass

    def translate_message(self, in_stream:str, out_stream:str="default.txt", encode:bool=False, standard:str=INTERNATIONAL, is_file:bool=False) -> None:
        """Translates from plaintext to morse code and vice versa.

        :params str in_stream: the text file or string of characters to encode to morse or decode to plaintext
        :params str out_stream: the name of the output file with | without path provided (used only when writing to a file)
        :params bool encode: a flag for turning encoding on, turning plaintext into morse code
        :params str standard: the standard encoding for morse ['international' (default), 'american', 'continental']
        :params bool is_file: determines whether a file or string is being used for translation

        """
        if is_file:
            file = self._read_file(filename=in_stream)
            message = self._message_stream(file, encode, standard)
            self._write_file(message, out_stream)
        else:
            message = self._message_stream(in_stream, encode, standard)
            print(message)

    def _message_stream(self, message, encode:bool, standard:str):
        """Determines encoding or decoding the message
        
        :params str | file message: can be passed a string of character or opened file
        :params bool encode: a flag to determine whether the message will be encoded or decoded
        :params str standard: the standard encoding for morse ('international', 'american', 'continental')

        :returns message: the encoded | decoded message as a string
        """
        if encode:
            new_message = self._encode_message(message, standard)
        else:
            new_message  = self._decode_message(message, standard)
        return new_message 

    def _write_file(message, filename) -> None:
        """A file write operation for outputing the encoded | decoded file
        
        :params message: the stream of morse or string of characters
        :params filename: the name of the output file
        """
        with open(filename, 'w') as file:
            file.write(message)

    def _read_file(filename):
        """Reads in a file whether written in morse code or plaintext
        
        :params str filename: the filename with current path 

        :returns file: the encoded | decoded text from the file
        """
        with open(filename, 'rt') as file:
            return file.read().replace('\n', ' ')
        
    def _encode_message(self, message:str, standard:str):
        """Encodes the plaintext message into morse code
        
        :params str message: plaintext used to create the encoded message
        :params str standard: the standard encoding for morse ('international', 'american', 'continental')

        :returns encoded_message: the morse code from the specified standard
        """
        encoded_message = ''
        for letter in message.upper():
            if letter == ' ':
                code = WORD_PACKING
            else:
                code = morse_code[standard][letter] + LETTER_PACKING
            encoded_message+=code
        return encoded_message
    
    def _decode_message(self, code:str, standard:str):
        """Decodes morse code into plaintext
        
        :params str code: morse code used to create the decoded message
        :params str standard: the standard encoding for morse ('international', 'american', 'continental')

        :returns decoded_message: the plaintext equivelant from the specified standard
        """
        message = ""
        code = [word.split(LETTER_PACKING) for word in code.split(WORD_PACKING)]   
        for word in range(len(code)):
            for val in code[word]:
                for k, v in morse_code[standard].items():
                    if v == val:
                        message+=k
                    else:
                        continue
            message+=" "
        return message
