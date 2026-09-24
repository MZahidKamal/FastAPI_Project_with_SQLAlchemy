from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from src.db.base import Base

# Explanation: Here, 'Column', 'Integer', 'String', 'Boolean', 'DateTime', and 'func' are imported from 'sqlalchemy' to
# define database table columns and functions, while 'Base' is imported from 'src.db.base' to act as the declarative base
# class for the ORM models.
# বাংলা ব্যাখ্যা: এখানে, ডাটাবেজ টেবিল কলাম ও ফাংশন ডিফাইন করার জন্য 'sqlalchemy' থেকে 'Column', 'Integer', 'String', 'Boolean',
# 'DateTime' এবং 'func' ইমপোর্ট করা হয়েছে, আর ওআরএম মডেলের ডিক্লারেটিভ বেস ক্লাস হিসেবে কাজ করার জন্য 'src.db.base' থেকে 'Base'
# ইমপোর্ট করা হয়েছে।



class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    priority = Column(Integer, default=1, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

# Explanation: Here, class 'Todo' inherits 'Base' to define the database table model; '__tablename__ = "todos"' sets the
#  table name to 'todos'; 'id = Column(Integer, primary_key=True, index=True)' creates an integer primary key with an
#  index enabled for fast lookups; 'title = Column(String, nullable=False)' creates a mandatory string column;
#  'description = Column(String, nullable=True)' creates an optional string column;
#  'priority = Column(Integer, default=1, nullable=False)' sets an integer column with a default value of '1' and a
#  non-null constraint; 'completed = Column(Boolean, default=False, nullable=False)' sets a boolean column defaulting to
#  'False' with a non-null constraint; and 'created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)'
#  automatically generates a timezone-aware timestamp at the database server level using 'func.now()'.
# বাংলা ব্যাখ্যা: এখানে, ডাটাবেজ টেবিল মডেল ডিফাইন করতে 'Base' থেকে 'Todo' ক্লাস ইনহেরিট করা হয়েছে; '__tablename__ = "todos"' টেবিলের নাম
#  'todos' সেট করে; 'id = Column(Integer, primary_key=True, index=True)' দ্রুত খোঁজার জন্য ইনডেক্সসহ ইন্টিজার প্রাইমারি কি তৈরি করে;
#  'title = Column(String, nullable=False)' একটি বাধ্যতামূলক স্ট্রিং কলাম তৈরি করে; 'description = Column(String, nullable=True)'
#  একটি অপশনাল স্ট্রিং কলাম তৈরি করে; 'priority = Column(Integer, default=1, nullable=False)' ডিফল্ট মান '1' এবং নন-নাল কনস্ট্রেইন্টসহ
#  ইন্টিজার কলাম সেট করে; 'completed = Column(Boolean, default=False, nullable=False)' ডিফল্ট মান 'False' এবং নন-নাল কনস্ট্রেইন্টসহ
#  বুলিয়ান কলাম সেট করে; এবং 'created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)' ডাটাবেজ
#  সার্ভার লেভেলে 'func.now()' ব্যবহার করে টাইমজোনসহ টাইমস্ট্যাম্প স্বয়ংক্রিয়ভাবে তৈরি করে।



created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

# Explanation: Here, 'created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)' defines a
# standalone column statement utilizing timezone-aware datetime, database-level default function 'func.now()', and
# non-null constraint 'nullable=False'.
# বাংলা ব্যাখ্যা: এখানে, 'created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)' দিয়ে টাইমজোনসহ
# ডেটটাইম, ডাটাবেজ-লেভেল ডিফল্ট ফাংশন 'func.now()' এবং নন-নাল কনস্ট্রেইন্ট 'nullable=False' সংবলিত একটি স্ট্যান্ডঅ্যালোন কলাম স্টেটমেন্ট ডিফাইন
# করা হয়েছে।










"""
প্রতিটা অংশ কেন:
class Todo(Base):: আগের db/base.py-এর Base inherit করছে, তাই SQLAlchemy এটাকে একটা table হিসেবে ধরে নেবে।
__tablename__ = "todos": Database-এ আসল table-এর নাম। Supabase-এ গেলে এই নামেই table দেখতে পাবেন।
id = Column(Integer, primary_key=True, index=True): primary_key=True মানে এটাই প্রতিটা row-এর unique identifier। index=True দিলে id দিয়ে খোঁজা দ্রুত হয় (Step 4/7-এর for loop-এর কাজটা এখন database নিজে efficiently করবে)।
nullable=False বনাম nullable=True: title-এর ক্ষেত্রে False মানে database-স্তরেই খালি রাখা যাবে না (আগে schemas.py-তে Pydantic-ও এটা check করত, এখন database-ও করবে — দুই স্তরে সুরক্ষা)। description-এ True কারণ এটা optional, schemas.py-এর সাথে মিলিয়ে।
default=1 / default=False: নতুন row বানানোর সময় value না দিলে database নিজে এই default বসাবে। এটা schemas.py-এর default-এর মতোই ধারণা, কিন্তু এখানে database-level-এ।

লক্ষ্য করার বিষয়: schemas.py বনাম models.py, দুটো আলাদা জিনিস, একই রকম দেখতে:
schemas.py (Pydantic): API-এর input/output shape ঠিক করে।
models.py (SQLAlchemy): আসল database table-এর structure ঠিক করে।

এগুলো field-নাম মিলিয়ে রাখা হয় (title, description, priority, completed) যাতে একটা থেকে আরেকটায় data সহজে রূপান্তর করা যায়, কিন্তু technically এরা সম্পূর্ণ আলাদা class, আলাদা library থেকে এসেছে।
"""

