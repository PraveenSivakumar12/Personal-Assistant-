import requests

API_KEY = "bc_fda4728497a613f15d2c1e809257e2bc330d39baa0935d583c3ab1d1834a950b"

def ask_ai(question):

    try:

        response = requests.post(
            "https://api.bcworks.in.net/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "OIv2",
                "messages": [
                    {"role": "user", "content": question}
                ],
                "max_tokens": 150
            },
            timeout=30
        )

        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"].strip()

        return "I did not understand the question."

    except Exception as e:
        print("AI Error:", e)
        return "Sorry boss, AI server is not responding."