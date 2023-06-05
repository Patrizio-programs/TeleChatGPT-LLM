import deep

question1 = "What is your name?"
req = deep.Completion.create(prompt=question1)
answer = req["text"]
message_id = req["parentMessageId"]


print(answer)
