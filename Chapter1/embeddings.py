#from google import genai


#client=genai.Client(api_key="AIzaSyBNWKXz_dNHHMKjyXZG9g-lQTi3pShMQjw")

from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyBNWKXz_dNHHMKjyXZG9g-lQTi3pShMQjw",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


text="The Effile tower is in Paris"

#result=client.models.embed_content(
  #      model="gemini-embedding-exp-03-07",
 #       contents=text)

result = client.embeddings.create(
    input=text,
    model="gemini-embedding-exp-03-07"
)

print(result.data[0].embedding)