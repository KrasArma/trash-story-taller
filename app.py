from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import uuid
from typing import Dict
from services.module_gigachat import gigachat_service
from data_models.operation_models import UserSession

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")
game_sessions: Dict[str, UserSession] = {}

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/game/{game_mode}")
async def game_page(request: Request, game_mode: str, lang: str = 'en'):
    session_id = str(uuid.uuid4())
    session = UserSession(
        session_id=session_id,
        game_mode=game_mode,
        lang=lang
    )
    game_sessions[session_id] = session
    welcome_message = gigachat_service.generate_welcome_message(game_mode, session)
    background_image = '/static/home-pic.png'
    return templates.TemplateResponse(
        "base-game.html",
        {
            "request": request,
            "session_id": session_id,
            "game_mode": game_mode,
            "lang": lang,
            "welcome_message": welcome_message,
            "background_image": background_image
        }
    )

@app.post("/game/{game_mode}/response")
async def process_game_response(game_mode: str, request: Request):
    data = await request.json()
    session_id = data.get('session_id')
    player_response = data.get('response')
    if not session_id or session_id not in game_sessions:
        return JSONResponse({"error": "Session not found"})
    session = game_sessions[session_id]
    ai_response = gigachat_service.process_player_response(
        game_mode,
        player_response,
        session
    )
    session.messages.append(f"User: {player_response}")
    session.messages.append(f"AI: {ai_response}")
    return JSONResponse({"message": ai_response})

app.mount("/static", StaticFiles(directory="static"), name="static")