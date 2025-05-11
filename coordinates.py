import pyautogui
import pyperclip
import time

# Step 1: Click on the icon (e.g., to focus the app)
icon_position = (1019, 1048)  # Replace with your actual icon coordinates
pyautogui.moveTo(icon_position)
pyautogui.click()
time.sleep(0.5)

# Step 2: Drag to select the text
start_pos = (713, 174)  # Start of the text
end_pos = (1850, 911)    # End of the text (horizontally or vertically as needed)

pyautogui.moveTo(start_pos)
pyautogui.mouseDown()
pyautogui.moveTo(end_pos, duration=0.5)
pyautogui.mouseUp()

# Step 3: Copy selected text (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Wait for clipboard to update
pyautogui.click(750,174)

# Step 4: Store copied text in a variable
copied_text = pyperclip.paste()



