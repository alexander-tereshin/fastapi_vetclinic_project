from enum import Enum
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime
from typing import List, Dict, Optional

app = FastAPI()


class DogType(str, Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Dog(BaseModel):
    name: str
    pk: int
    kind: DogType


class Timestamp(BaseModel):
    id: int
    timestamp: int


dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]


def get_db_post() -> List[Timestamp]:
    return post_db


def get_db_dogs() -> Dict[int, Dog]:
    return dogs_db


@app.get("/", summary="Root", operation_id='root__get')
async def root():
    """
    Root endpoint that returns a greeting message.

    Returns:
        dict: A dictionary with a greeting message.
    """
    return {"message": "Hello, User!"}


@app.post("/post", summary="Get Post", operation_id='get_post_post_post', response_model=Timestamp)
async def add_item(db=Depends(get_db_post)) -> Timestamp:
    """
    Create and return a new Timestamp.

    Args:
        db (List[Timestamp]): The list of Timestamp items.

    Returns:
        Timestamp: The newly created Timestamp.
    """
    max_id = max([i.id for i in db])
    dt = datetime.now()
    ts = int(datetime.timestamp(dt))
    new_timestamp = Timestamp(id=max_id + 1, timestamp=ts)
    db.append(new_timestamp)
    return new_timestamp


@app.get('/dog', response_model=List[Dog], summary='Get Dogs', operation_id='get_dogs_dog_get')
async def get_dogs(kind: Optional[DogType] = None, db=Depends(get_db_dogs)) -> list[Dog]:
    """
    Get a list of Dog items filtered by kind.

    Args:
        kind (Optional[DogType]): The kind of Dog to filter by.
        db (Dict[int, Dog]): The database of Dog items.

    Returns:
        list[Dog]: A list of Dog items.
    """
    if kind:
        return list(filter(lambda x: x.kind == kind, db.values()))
    return list(db.values())


@app.post('/dog', response_model=Dog, summary='Create Dog', operation_id='create_dog_dog_post')
async def create_dogs(dog: Dog, db=Depends(get_db_dogs)) -> Dog:
    """
    Create and return a new Dog item.

    Args:
        dog (Dog): The Dog item to create.
        db (Dict[int, Dog]): The database of Dog items.

    Returns:
        Dog: The newly created Dog item.
    """
    if db.get(dog.pk):
        raise HTTPException(status_code=422, detail="pk already exists")
    db[dog.pk] = dog
    return dog


@app.get('/dog/{pk}', response_model=Dog, summary='Get Dog By Pk', operation_id='get_dog_by_pk_dog__pk__get')
async def get_dog_by_pk(pk: int, db=Depends(get_db_dogs)) -> Dog:
    """
    Get a Dog item by its primary key (pk).

    Args:
        pk (int): The primary key of the Dog item to retrieve.
        db (Dict[int, Dog]): The database of Dog items.

    Returns:
        Dog: The retrieved Dog item.
    """
    if not db.get(pk):
        raise HTTPException(status_code=422, detail="pk does not exists")
    return db.get(pk)


@app.patch('/dog/{pk}', response_model=Dog, summary='Update Dog', operation_id='update_dog_dog__pk__patch')
async def update_dog_by_pk(pk: int, dog: Dog, db=Depends(get_db_dogs)) -> Dog:
    """
    Update a Dog item by its primary key (pk).

    Args:
        pk (int): The primary key of the Dog item to update.
        dog (Dog): The new Dog item data.
        db (Dict[int, Dog]): The database of Dog items.

    Returns:
        Dog: The updated Dog item.
    """
    if not db.get(pk):
        raise HTTPException(status_code=422, detail="pk does not exists")
    db[pk] = dog
    return dog
