 def extract_business_units(self, input_text):
        conversation = [
            {"role": "system", "content": "You are an expert in extract Business Units from a given ODRL specification."}
        ]
        for example in self.training_examples:
            conversation.append({"role": "user", "content": "file01: " + example["input"]})
            conversation.append({"role": "assistant", "content": example["output"]})
            print('pássou')

        conversation.append({"role": "user", "content": "file01: " + input_text})

        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=conversation
        )
        
        output_text = completion.choices[0].message.content
        return output_text