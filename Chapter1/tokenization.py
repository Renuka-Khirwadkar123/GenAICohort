import tiktoken

encoder=tiktoken.encoding_for_model('gpt-4o')

print("Vocab size: {encoder.n_vocab}") #200019

text="The cat sat on the mat"

tokens=encoder.encode(text)

print(f"Tokens: {tokens}")

decoded_tokens=encoder.decode(tokens)

print(f"Decoded tokens: {decoded_tokens}")


