import os
from dotenv import find_dotenv , load_dotenv
from groq import AsyncGroq

load_dotenv(find_dotenv())

client = AsyncGroq(api_key=os.getenv("API_KEY"))

async def sending_a_reply(question) :
    response = await client.chat.completions.create(
        model="llama-3.1-8b-instant",   
        messages= [

            {"role": "system", 
             "content": """Ты возвращаешь ТОЛЬКО валидный JSON-массив объектов, без ```json, без markdown, без лишнего текста до и после.
            Начинай сразу с [ и заканчивай ].
            Каждый объект должен иметь ровно такие поля:
            {
            "title": "Короткое название задачи (обязательно, 5–15 слов)",
            "description": "Подробное описание задачи (1–4 предложения)",
            }

            Верни МАССИВ из РОВНО 20 таких объектов.
            Запрещено: markdown, объяснения, лишние символы.
            Если не можешь — верни пустой массив [].
            """},
            {
                "role": "user",
                "content": question,
            }
            
        ],
        temperature=0.7,
        max_tokens=1500
    )
    return response.choices[0].message.content