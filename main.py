import pyautogui
import pyperclip
import time
from openai import OpenAI


def should_respond(chat_history: str) -> bool:
        lines = [line.strip() for line in chat_history.strip().split('\n') if line.strip()]
        
        if not lines:
            return False  # Empty chat

        last_line = lines[-1]

        try:
            name_and_msg = last_line.split('2025]')[-1].strip()
            name = name_and_msg.split(':')[0].strip()
            return name.startswith("") # Enter the name of user to reply
        except Exception:
            return False
    
    
icon_position = (1019, 1048)  # Replace with your actual icon coordinates
pyautogui.moveTo(icon_position)
pyautogui.click()
time.sleep(0.5)

while True:

    start_pos = (699, 180)  # Start of the text
    end_pos = (730, 950)    # End of the text

    pyautogui.moveTo(start_pos)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_pos, duration=0.5)
    pyautogui.mouseUp()

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.click(750,174)

    chat_history = pyperclip.paste()

# I've used openrouter's free available llama model, you can use any depending upon what type of response you want.
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="API Key", # Replace with your Api keys
    )

    if should_respond(chat_history):
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct", # You can use any model depending upon type of response you want.
            messages=[
                {
                    "role": "You are a person named Aaditya who speakes english. He is a stuent.",
                    "content": str({chat_history})
                }
            ],
        )
        
        response = completion.choices[0].message.content
        print(response)
        pyperclip.copy(response)


        pyautogui.moveTo(799, 969)
        pyautogui.click()
        time.sleep(0.2)

        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        pyautogui.press('enter') 
