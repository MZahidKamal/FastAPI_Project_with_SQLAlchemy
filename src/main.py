from fastapi import FastAPI
from src.features.todos.router import router as todos_router
from src.db.base import Base
from src.db.session import engine
from src.features.todos import models

# Explanation: Here, 'FastAPI' is imported from 'fastapi' to create the web app instance; 'todos_router' is imported from
# 'src.features.todos.router' for routing; 'Base' is imported from 'src.db.base' for database metadata; 'engine' is
# imported from 'src.db.session' for database connectivity; and 'models' is imported from 'src.features.todos' to ensure
# SQLAlchemy registers the table models.
# বাংলা ব্যাখ্যা: এখানে, ওয়েব অ্যাপ ইনস্ট্যান্স তৈরির জন্য 'fastapi' থেকে 'FastAPI' ইমপোর্ট করা হয়েছে; রাউটিংয়ের জন্য 'src.features.todos.router'
# থেকে 'todos_router' ইমপোর্ট করা হয়েছে; ডাটাবেজ মেটাডেটার জন্য 'src.db.base' থেকে 'Base' ইমপোর্ট করা হয়েছে; কানেক্টিভিটির জন্য
# 'src.db.session' থেকে 'engine' ইমপোর্ট করা হয়েছে; এবং এসকিউএলএলকেমি যেন টেবিল মডেল রেজিস্টার করে তা নিশ্চিত করতে 'src.features.todos'
# থেকে 'models' ইমপোর্ট করা হয়েছে।



Base.metadata.create_all(bind=engine)

# Explanation: Here, 'Base.metadata.create_all(bind=engine)' uses the database 'engine' to automatically create all
# defined tables in the database if they do not already exist based on the metadata of 'Base'.
# বাংলা ব্যাখ্যা: এখানে, 'Base.metadata.create_all(bind=engine)' এর মাধ্যমে 'Base'-এর মেটাডেটা ব্যবহার করে ডাটাবেজে টেবিলগুলো আগে থেকে
# না থাকলে স্বয়ংক্রিয়ভাবে তৈরি করার জন্য ডাটাবেজ 'engine' বাইন্ড করা হয়েছে।



app = FastAPI(title="FastAPI_Project_with_SQLAlchemy")
app.include_router(todos_router)

# Explanation: Here, 'app = FastAPI(title="FastAPI_Project_with_SQLAlchemy")' initializes the main FastAPI application
# instance where 'title="FastAPI_Project_with_SQLAlchemy"' sets the project title for documentation, and
# 'app.include_router(todos_router)' registers all todo routes into the main app.
# বাংলা ব্যাখ্যা: এখানে, ডকুমেন্টেশনের জন্য প্রজেক্ট টাইটেল 'title="FastAPI_Project_with_SQLAlchemy"' দিয়ে মূল FastAPI অ্যাপ্লিকেশন ইনস্ট্যান্স
# 'app = FastAPI(...)' তৈরি করা হয়েছে এবং 'app.include_router(todos_router)' দিয়ে সমস্ত টডো রাউট মূল অ্যাপে রেজিস্টার করা হয়েছে।



@app.get("/")
async def root():
    return {"message": "FastAPI_Project_with_SQLAlchemy is running"}

# Explanation: Here, '@app.get("/")' registers an HTTP GET endpoint at the root path; async function 'root()' handles
# incoming requests asynchronously; and 'return {"message": "FastAPI_Project_with_SQLAlchemy is running"}' returns a
# JSON response confirming that the application is running successfully.
# বাংলা ব্যাখ্যা: এখানে, '@app.get("/")' রুট পাথে একটি এইচটিটিপি গেট এন্ডপয়েন্ট রেজিস্টার করে; অ্যাসিনক্রোনাস ফাংশন 'root()' রিকোয়েস্ট হ্যান্ডেল করে;
# এবং 'return {"message": "FastAPI_Project_with_SQLAlchemy is running"}' অ্যাপ্লিকেশন সফলভাবে চলার কনফার্মেশন সম্বলিত জেসন রেসপন্স
# রিটার্ন করে।

