from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.features.todos.schemas import TodoCreate, TodoResponse
from src.features.todos.models import Todo
from src.db.session import get_db

# Explanation: Here, 'APIRouter', 'HTTPException', and 'Depends' are imported from 'fastapi' to handle routing, error
# response raising, and dependency injection; 'Session' is imported from 'sqlalchemy.orm' for typing database sessions;
# 'TodoCreate' and 'TodoResponse' schemas are imported from 'src.features.todos.schemas' for request and response validation;
# 'Todo' model is imported from 'src.features.todos.models' representing the database table; and 'get_db' is imported
# from 'src.db.session' to inject active database sessions.
# বাংলা ব্যাখ্যা: এখানে, রাউটিং, এরর রেইজ এবং ডিপেন্ডেন্সি ইনজেকশনের জন্য 'fastapi' থেকে 'APIRouter', 'HTTPException' ও 'Depends' ইমপোর্ট
# করা হয়েছে; ডাটাবেজ সেশন টাইপিংয়ের জন্য 'sqlalchemy.orm' থেকে 'Session' ইমপোর্ট করা হয়েছে; রিকোয়েস্ট ও রেসপন্স ভ্যালিডেশনের জন্য
# 'src.features.todos.schemas' থেকে 'TodoCreate' ও 'TodoResponse' স্কিমা ইমপোর্ট করা হয়েছে; ডাটাবেজ টেবিল নির্দেশ করতে
# 'src.features.todos.models' থেকে 'Todo' মডেল ইমপোর্ট করা হয়েছে; এবং সেশন ইনজেক্ট করার জন্য 'src.db.session' থেকে 'get_db'
# ইমপোর্ট করা হয়েছে।



router = APIRouter(prefix="/todos", tags=["todos"])

# Explanation: Here, 'router = APIRouter(prefix="/todos", tags=["todos"])' instantiates an 'APIRouter' where 'prefix="/todos"'
# sets the base URL path for all child endpoints, and 'tags=["todos"]' organizes and groups the endpoints neatly under the
# 'todos' section in the auto-generated Swagger/OpenAPI documentation UI.
# বাংলা ব্যাখ্যা: এখানে, 'router = APIRouter(prefix="/todos", tags=["todos"])' দিয়ে একটি 'APIRouter' ইনস্ট্যান্স তৈরি করা হয়েছে যেখানে
# 'prefix="/todos"' সমস্ত চাইল্ড এন্ডপয়েন্টের জন্য বেস ইউআরএল পাথ সেট করে এবং 'tags=["todos"]' স্বয়ংক্রিয়ভাবে তৈরি হওয়া সোয়াগার/ওপেনএপিআই
# ডকুমেন্টেশনে এন্ডপয়েন্টগুলোকে সুন্দরভাবে 'todos' সেকশন হিসেবে গ্রুপ করে।



@router.post("/", response_model=TodoResponse)
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = Todo(**todo.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# Explanation: Here, '@router.post("/", response_model=TodoResponse)' registers an HTTP POST endpoint at the root path
# with 'TodoResponse' as the response model; 'create_todo' asynchronous function takes 'todo: TodoCreate' payload and
# 'db: Session = Depends(get_db)' session dependency; 'new_todo = Todo(**todo.model_dump())' unpacks the Pydantic
# dictionary to initialize the 'Todo' ORM model; 'db.add(new_todo)' stages the instance in the session; 'db.commit()'
# persists the transaction to the database; 'db.refresh(new_todo)' reloads instance attributes like database-generated
# identifiers; and 'return new_todo' sends the created object back.
# বাংলা ব্যাখ্যা: এখানে, '@router.post("/", response_model=TodoResponse)' রেসপন্স মডেল হিসেবে 'TodoResponse' সহ রুট পাথে একটি
# এইচটিটিপি পোস্ট এন্ডপয়েন্ট রেজিস্টার করে; অ্যাসিনক্রোনাস ফাংশন 'create_todo' পে-লোড 'todo: TodoCreate' এবং সেশন ডিপেন্ডেন্সি
# 'db: Session = Depends(get_db)' গ্রহণ করে; 'new_todo = Todo(**todo.model_dump())' পাইডান্টিক ডিকশনারি আনপ্যাক করে 'Todo'
# ওআরএম মডেল ইনস্ট্যান্স তৈরি করে; 'db.add(new_todo)' ইনস্ট্যান্সটিকে সেশনে যুক্ত করে; 'db.commit()' ট্রানজেকশন ডেটাবেজে সেভ করে;
# 'db.refresh(new_todo)' ডেটাবেজ-জেনারেটেড আইডি সহ অন্যান্য অ্যাট্রিবিউট রিফ্রেশ করে; এবং 'return new_todo' তৈরি হওয়া অবজেক্টটি রিটার্ন করে।



@router.get("/", response_model=list[TodoResponse])
async def get_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

# Explanation: Here, '@router.get("/", response_model=list[TodoResponse])' registers an HTTP GET endpoint returning a
# list of 'TodoResponse' models; 'get_todos' asynchronous function accepts the injected database session
# 'db: Session = Depends(get_db)'; and 'return db.query(Todo).all()' executes a query to fetch all records from the
# 'Todo' table and returns them as a collection.
# বাংলা ব্যাখ্যা: এখানে, '@router.get("/", response_model=list[TodoResponse])' একটি লিস্ট রেসপন্স মডেলসহ এইচটিটিপি গেট এন্ডপয়েন্ট রেজিস্টার
# করে; অ্যাসিনক্রোনাস ফাংশন 'get_todos' ইনজেক্ট করা সেশন 'db: Session = Depends(get_db)' গ্রহণ করে; এবং 'return db.query(Todo).all()'
# কুয়েরির মাধ্যমে 'Todo' টেবিলের সব রেকর্ড ফেচ করে রিটার্ন করে।



@router.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo Not found")
    return todo

# Explanation: Here, '@router.get("/{todo_id}", response_model=TodoResponse)' registers an HTTP GET endpoint with path
# parameter 'todo_id: int'; 'todo = db.query(Todo).filter(Todo.id == todo_id).first()' queries the database where
# 'Todo.id == todo_id' matches and retrieves the first record; if 'todo is None', 'raise HTTPException(status_code=404,
# detail="Todo Not found")' triggers a 404 Not Found error with detail 'Todo Not found'; otherwise, it returns the found
# 'todo' object.
# বাংলা ব্যাখ্যা: এখানে, '@router.get("/{todo_id}", response_model=TodoResponse)' পাথ প্যারামিটার 'todo_id: int' সহ একটি এইচটিটিপি
# গেট এন্ডপয়েন্ট রেজিস্টার করে; 'todo = db.query(Todo).filter(Todo.id == todo_id).first()' কুয়েরি চালিয়ে 'Todo.id == todo_id' মিলে
# যাওয়া প্রথম রেকর্ডটি খুঁজে আনে; যদি 'todo is None' হয়, তবে 'raise HTTPException(status_code=404, detail="Todo Not found")'
# এর মাধ্যমে '404 Not Found' এরর রেইজ হয়; অন্যথায় পাওয়া 'todo' অবজেক্টটি রিটার্ন করা হয়।



@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: int, updated_todo: TodoCreate, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo Not found")

    for key, value in updated_todo.model_dump().items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    return todo

# Explanation: Here, '@router.put("/{todo_id}", response_model=TodoResponse)' registers an HTTP PUT endpoint for updates;
# it queries and fetches the target 'todo' by 'todo_id'; if not found, raises a 404 error; the loop 'for key, value in
# updated_todo.model_dump().items(): setattr(todo, key, value)' dynamically updates each attribute of the 'todo' instance
# using 'setattr()'; 'db.commit()' saves the updates to the database; 'db.refresh(todo)' updates the instance state;
# and 'return todo' returns the modified object.
# বাংলা ব্যাখ্যা: এখানে, '@router.put("/{todo_id}", response_model=TodoResponse)' আপডেটের জন্য একটি এইচটিটিপি পুট এন্ডপয়েন্ট রেজিস্টার
# করে; এটি 'todo_id' দিয়ে টার্গেট 'todo' খুঁজে আনে এবং না পেলে '404' এরর রেইজ করে; লুপ 'for key, value in
# updated_todo.model_dump().items(): setattr(todo, key, value)' এর মাধ্যমে 'setattr()' ব্যবহার করে ডাইনামিকভাবে ইন্সট্যান্সের
# অ্যাট্রিবিউটগুলো আপডেট করা হয়; 'db.commit()' পরিবর্তনগুলো ডেটাবেজে সেভ করে; 'db.refresh(todo)' ইন্সট্যান্স স্টেট আপডেট করে; এবং
# 'return todo' মডিফাইড অবজেক্টটি রিটার্ন করে।



@router.delete("/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo Not found")

    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted successfully!"}



# Explanation: Here, '@router.delete("/{todo_id}")' registers an HTTP DELETE endpoint; it queries the target 'todo' by
# 'todo_id' and raises a 404 error if it does not exist; 'db.delete(todo)' marks the record for deletion in the session;
# 'db.commit()' executes the removal from the database; and 'return {"message": "Todo deleted successfully!"}' returns
# a success confirmation dictionary.
# বাংলা ব্যাখ্যা: এখানে, '@router.delete("/{todo_id}")' একটি এইচটিটিপি ডিলিট এন্ডপয়েন্ট রেজিস্টার করে; এটি 'todo_id' দিয়ে টার্গেট 'todo' খুঁজে
# আনে এবং না থাকলে '404' এরর রেইজ করে; 'db.delete(todo)' রেকর্ডটি সেশনে ডিলিটের জন্য মার্ক করে; 'db.commit()' ডেটাবেজ থেকে মুছে ফেলা
# নিশ্চিত করে; এবং 'return {"message": "Todo deleted successfully!"}' সফলতার কনফার্মেশন ডিকশনারি রিটার্ন করে।

