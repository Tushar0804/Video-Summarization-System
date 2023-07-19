import openai

class Summariser:
    def __init__(self, textFileName):
        self.textFileName = textFileName
        self.apiKey = ""
    
    def summarise(self):
        openai.api_key = self.apiKey
        # getting the text
        text_file = open(self.textFileName)
        text = text_file.read()

        summary = ""

        word_count = 0
        prompt_text = ""
        count = 0

        for word in text.split():
            word_count += 1
            prompt_text += word + " "

            if (count == 0 and word_count == 3000):
                pr = prompt_text + "\n\nSummarize the above text extracted from a video in around 200 words: \n\nThe video"

                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=pr,
                    max_tokens=500,
                    temperature=0.6,
                    stop="\n\n\n"
                )
                summary += "The video" +  response["choices"][0]["text"] + "\n"

                word_count = 0
                prompt_text = ""
                count += 1    
            elif (word_count == 3000):
                pr = prompt_text + "\n\nSummarize the above text extracted from a video in around 200 words: \n\n"

                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=pr,
                    max_tokens=500,
                    temperature=0.6,
                    stop="\n\n\n"
                )
                summary += " " +  response["choices"][0]["text"] + "\n"

                word_count = 0
                prompt_text = ""

        if (count == 0 and word_count != 0):
                pr = prompt_text + "\n\nSummarize the above text extracted from a video in around 150 words: \n\nThe video"

                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=pr,
                    max_tokens=500,
                    temperature=0.6,
                    stop="\n\n\n"
                )
                summary += "The video" +  response["choices"][0]["text"] + "\n"

                count += 1
        elif (word_count != 0):
                pr = prompt_text + "\n\nSummarize the above text extracted from a video in around 150 words: \n\n"

                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=pr,
                    max_tokens=500,
                    temperature=0.6,
                    stop="\n\n\n"
                )
                summary += " " +  response["choices"][0]["text"] + "\n"

        return summary
