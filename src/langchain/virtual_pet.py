import pygame
import os
import uuid
import time
import threading
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
import math

# ---------------- CONFIG ----------------
load_dotenv()

WIDTH, HEIGHT = 400, 500
BG_COLOR = (245, 245, 250)
TEXT_COLOR = (50, 50, 60)

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

SYSTEM_PROMPT = """
Role: You are "Kirby", a virtual pet for CCDS Hackathon 2026.
Personality: Playful, warm, encouraging.
Goal: Support hackathon participants.
Response: Concise (2–3 sentences max).
"""

# ---------------- LLM Setup ----------------
try:
    llm = AzureChatOpenAI(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        deployment_name=AZURE_OPENAI_DEPLOYMENT,
    )
except Exception as e:
    print(f"LLM Setup Error: {e}")
    llm = None

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

chain = prompt | llm if llm else None
_STORE = {}

def get_history(session_id: str):
    if session_id not in _STORE:
        _STORE[session_id] = ChatMessageHistory()
    return _STORE[session_id]

chat_runner = RunnableWithMessageHistory(
    chain,
    get_history,
    input_messages_key="input",
    history_messages_key="history",
) if chain else None

# ---------------- PET STATE ----------------
pet_state = {
    "name": "Kirby", 
    "mood": "happy",
    "hunger": 2,
    "energy": 3,
    "last_response": "Hello! I'm Kirby 🐾",
}

session_id = str(uuid.uuid4())
chat_lock = threading.Lock()
is_thinking = False

# ---------------- HELPERS ----------------
def clamp(v: int) -> int:
    return max(0, min(5, v))

def handle_command(text: str) -> str | None:
    t = text.strip().lower()
    if t == "/feed":
        pet_state["hunger"] = clamp(pet_state["hunger"] + 2)
        pet_state["mood"] = "happy"
        return "*nom nom* That was tasty! 💕"
    if t == "/play":
        pet_state["energy"] = clamp(pet_state["energy"] - 2)
        pet_state["mood"] = "excited"
        return "*zoomies!* That was fun! ✨"
    if t == "/rest":
        pet_state["energy"] = clamp(pet_state["energy"] + 3)
        pet_state["mood"] = "sleepy"
        return "*yawn* Feeling refreshed… 😴"
    return None

# ---------------- LLM WORKER ----------------
def llm_worker(user_input: str):
    global is_thinking
    try:
        local_msg = handle_command(user_input)
        if local_msg:
            with chat_lock:
                pet_state["last_response"] = local_msg
            return
        if chat_runner:
            result = chat_runner.invoke(
                {"input": user_input},
                config={"configurable": {"session_id": session_id}},
            )
            with chat_lock:
                pet_state["last_response"] = result.content
        else:
            pet_state["last_response"] = "My brain is offline right now… 💤"
    except Exception as e:
        pet_state["last_response"] = f"Ouch… error: {e}"
    finally:
        is_thinking = False

# ---------------- UI ----------------
def run_gui(pet_state, get_response, is_thinking_flag):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("CCDS Hackathon 2026")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)
    input_text = ""  
    input_active = False  # Track whether the input box is active (clicked)
    
    # Load the Kirby image and scale it larger
    kirby_image = pygame.image.load("images/kirby.png")
    kirby_image = pygame.transform.scale(kirby_image, (120, 120))  # Increased size

    cursor_blink_time = 0
    cursor_visible = True

    while True:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the input box is clicked
                if bar.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
            if event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        if input_text and not is_thinking_flag():
                            get_response(input_text)
                            input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        # Cursor blink effect
        current_time = pygame.time.get_ticks()
        if current_time - cursor_blink_time > 500:  # Blink every 500 ms
            cursor_blink_time = current_time
            cursor_visible = not cursor_visible

        # Floating effect for Kirby
        t = time.time()
        float_y = 200 + int(15 * math.sin(t * 2)) 

        # Display the Kirby image at the center 
        screen.blit(kirby_image, (WIDTH // 2 - 60, float_y))

        # Speech Bubble
        text = "Thinking..." if is_thinking_flag() else pet_state["last_response"]
        draw_speech_bubble(screen, text, font, WIDTH // 2, 180)

        # Input bar
        bar = pygame.Rect(40, HEIGHT - 55, WIDTH - 80, 36)
        pygame.draw.rect(screen, (255, 255, 255), bar, border_radius=18)
        pygame.draw.rect(screen, (180, 180, 180), bar, 2, border_radius=18)

        # Set the text based on whether the input field is active or not
        if input_active:
            text_surface = font.render(input_text, True, TEXT_COLOR)
        else:
            text_surface = font.render(input_text, True, TEXT_COLOR)
        
        screen.blit(text_surface, (bar.x + 14, bar.y + 9))

        # If the input field is active and the cursor is visible, draw a cursor
        if input_active and cursor_visible:
            cursor_x = bar.x + 14 + text_surface.get_width()
            pygame.draw.line(screen, TEXT_COLOR, (cursor_x, bar.y + 9), (cursor_x, bar.y + 9 + font.get_height()), 2)

        pygame.display.flip()
        clock.tick(30)

def draw_speech_bubble(screen, text, font, x, y):
    padding = 10
    max_width = 260

    words = text.split(" ")
    lines, line = [], []
    for w in words:
        test = line + [w]
        if font.size(" ".join(test))[0] <= max_width:
            line.append(w)
        else:
            lines.append(" ".join(line))
            line = [w]
    lines.append(" ".join(line))

    bubble_w = max(font.size(l)[0] for l in lines) + padding * 2
    bubble_h = len(lines) * font.get_height() + padding * 2

    rect = pygame.Rect(x - bubble_w // 2, y - bubble_h - 20, bubble_w, bubble_h)
    pygame.draw.rect(screen, (255, 255, 255), rect, border_radius=14)
    pygame.draw.rect(screen, (180, 180, 180), rect, 2, border_radius=14)

    pygame.draw.polygon(screen, (255, 255, 255), [(x - 10, y - 20), (x + 10, y - 20), (x, y - 5)])

    ty = rect.y + padding
    for l in lines:
        surf = font.render(l, True, TEXT_COLOR)
        screen.blit(surf, (rect.centerx - surf.get_width() // 2, ty))
        ty += font.get_height()

def send_user_input(text: str):
    global is_thinking
    if is_thinking:
        return
    is_thinking = True
    threading.Thread(target=llm_worker, args=(text,), daemon=True).start()

def thinking() -> bool:
    return is_thinking

if __name__ == "__main__":
    run_gui(pet_state=pet_state, get_response=send_user_input, is_thinking_flag=thinking)
