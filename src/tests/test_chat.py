from larry.chat import Chat

def test_chat():

    def fn(context):
        return "hello world"
    
    chat = Chat(fn = fn)
    chat.launch()