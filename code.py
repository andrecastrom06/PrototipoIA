from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)
