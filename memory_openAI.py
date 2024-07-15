from openai import OpenAI

class Chatbot:
    def __init__(self):
        self.client = OpenAI()
        self.message_history = [
            {
                "role": "system",
                "content": "You are a helpful assistant. You must answer in Korean.",
            }
        ]

    def ask(self, question):
        # 사용자 질문 추가
        self.message_history.append(
            {
                "role": "user",
                "content": question,
            }
        )

        # GPT에 질문을 전달하여 답변을 생성
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.message_history,
            stream=True
        )

        # 사용자 질문에 대한 답변을 추가
        assistant_response = completion.choices[0].message.content
        print(assistant_response)
        self.message_history.append(
            {
                "role": "assistant", 
                "content": assistant_response
            }
        )

        return assistant_response