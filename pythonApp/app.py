from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    dumas = db.query(models.Duma).all()
    return templates.TemplateResponse("base.html",
                                      {"request": request, "duma_list": dumas})

@app.post("/add")
def add(request: Request, speach: str = Form(...), db: Session = Depends(get_db)):
    new_duma = models.Duma(speach=speach)
    db.add(new_duma)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)


@app.get("/delete/{duma_id}")
def delete(request: Request, duma_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Duma).filter(models.Duma.id == duma_id).first()
    db.delete(todo)
    db.commit()

    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_302_FOUND)

@app.get("/easterEgg")
async def root():
    return {"The python language is one of the most accessible programming languages available because it has simplified syntax and not complicated, which gives more emphasis on natural language. Due to its ease of learning and usage, python codes can be easily written and executed much faster than other programming languages."}