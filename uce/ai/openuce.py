import openai
from pydantic import BaseModel

openai.organization = 'org-jDmiW3xvXqaQ5QBPpToXtWif'
openai.api_key = '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'


class Document(BaseModel):
    item: str = 'pizza'
    id: str = '1'


def process_inference(user_prompt, user_id) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    print(user_prompt)
    print(user_id)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un chef que lista los ingredientes de los platillos que se te proporcionan.
        E.G
        pan
        Ingredientes:
        arina
        huevos
        agua
        azucar
        ...
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
