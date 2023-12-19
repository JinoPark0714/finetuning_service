import json

class GPTFineTuningGenerator:
    def __init__(self):
        self.is_system_constant = 'n'
        self.system_content = ""


    def write_json(self, system_content, user_content, assistant_content):
        message_form = {
            "messages" : [
                {
                    "role" : "system",
                    "content" : system_content
                },
                {
                    "role" : "user",
                    "content" : user_content
                },
                {
                    "role" : "assistant",
                    "content" : assistant_content
                }
            ]
        }

        with open("fine_tuning.jsonl", "a", encoding="UTF8") as file:
            json.dump(message_form, file, ensure_ascii=False)
            file.write(',\n')
            file.close()