from fastapi import FastAPI, Depends, Request, Form, status
from fastapi.responses import HTMLResponse

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


@app.get("/get_year")
def year(request: Request, year: str, db: Session = Depends(get_db)):
    filters = {"year": year}
    dumas = db.query(models.Duma).filter_by(**filters).all()
    return templates.TemplateResponse("base.html",
                                      {"request": request, "duma_list": dumas})



@app.get("/get_name")
def name(request: Request, sp_name: str, db: Session = Depends(get_db)):
    filters=sp_name
    #dumas = db.query(models.Duma).filter(models.Duma.name.like('name%')).all()
    dumas = db.query(models.Duma).filter(models.Duma.name.startswith(filters)).all()
    return templates.TemplateResponse("base.html",
                                      {"request": request, "duma_list": dumas})




@app.post("/add")
def add(request: Request, text: str = Form(...), db: Session = Depends(get_db)):
    new_duma = models.Duma(text=text)
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
    return {"Hi, my name is Roman. this is my project. This project describes the process shiftings in the objects and themes discussed during the sessions of the State Duma of the Russian Federation in different time periods. In this work transcripts of meetings from 1994 to 2022 were analyzed. This paper considered relevant studies, further a corpus of speeches was compiled. A statistical analysis of the texts was carried out. For each year LDA models were created. In this work sentiment analysis process of each statement were described. Data analysis is accompanied by data visualization graphs. For sentiment analysis of texts, a recurrent neural network of two LSTM layers was created and trained. The paper presents an interpretation of the shiftings in the objects and themes discussed during the sessions of the State Duma, as well as attempts to identify their possible causes."}