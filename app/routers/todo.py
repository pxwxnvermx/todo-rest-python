from typing import Any
from fastapi import status, HTTPException, APIRouter, Depends, Response
from sqlalchemy.orm import Session

from app import schemas, models
from app.database import get_db

router = APIRouter(prefix="/api/v1/todo", tags=['Todo'])

@router.get("/")
def get_todos(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    todos = db.query(models.Todo).offset(skip).limit(limit).all()
    return {"data": todos}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.TodoItemBase, db: Session = Depends(get_db)):
    new_todo_item = models.Todo(**todo.dict())

    db.add(new_todo_item)
    db.commit()
    db.refresh(new_todo_item)

    return {"data": new_todo_item}


@router.get("/{id}")
def get_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id: {id} was not found")

    return {"data": todo}


@router.put("/{id}")
def update_todo(id: int, updated_todo: schemas.TodoItemUpdate, db: Session = Depends(get_db)):
    todo_query = db.query(models.Todo).filter(models.Todo.id == id)
    todo = todo_query.first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id: {id} was not found")

    todo_query.update(updated_todo.dict(exclude_unset=True), synchronize_session=False)

    db.commit()
    db.refresh(todo)

    return {"data": todo}


@router.delete("/{id}")
def delete_todo(id: int, db: Session = Depends(get_db)):
    todo_query = db.query(models.Todo).filter(models.Todo.id == id)

    todo = todo_query.first()

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Todo with id: {id} was not found")

    todo_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
