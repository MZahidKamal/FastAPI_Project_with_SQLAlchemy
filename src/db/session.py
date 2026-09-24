from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import settings

# Explanation: Here, 'create_engine' and 'sessionmaker' are imported from 'sqlalchemy' and 'sqlalchemy.orm' for database
# connection setup and session management, while 'settings' is imported from 'src.core.config' to load environment
# configurations.
# বাংলা ব্যাখ্যা: এখানে, ডাটাবেজ কানেকশন সেটআপ ও সেশন ম্যানেজমেন্টের জন্য 'sqlalchemy' এবং 'sqlalchemy.orm' থেকে 'create_engine' ও
# 'sessionmaker' ইমপোর্ট করা হয়েছে, আর এনভায়রনমেন্ট কনফিগারেশন লোড করার জন্য 'src.core.config' থেকে 'settings' ইমপোর্ট করা হয়েছে।



engine = create_engine(settings.sb_connection_string)

# Explanation: Here, 'engine = create_engine(settings.sb_connection_string)' initializes the database connection engine
# using 'settings.sb_connection_string' as the database URI.
# বাংলা ব্যাখ্যা: এখানে, ডাটাবেজ ইউআরআই হিসেবে 'settings.sb_connection_string' ব্যবহার করে ডাটাবেজ কানেকশন ইঞ্জিন
# 'engine = create_engine(settings.sb_connection_string)' তৈরি করা হয়েছে।



SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Explanation: Here, 'SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)' configures a session
# factory bound to 'engine'; 'autocommit=False' is set for manual transaction safety, 'autoflush=False' is set to prevent
# premature flushing of changes, and 'bind=engine' connects sessions to the database engine.
# বাংলা ব্যাখ্যা: এখানে, 'SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)' দিয়ে ইঞ্জিনের সাথে যুক্ত সেশন
# ফ্যাক্টরি কনফিগার করা হয়েছে; ম্যানুয়াল ট্রানজেকশন সেফটির জন্য 'autocommit=False', পরিবর্তনের প্রিম্যাচিউর ফ্লুশ রোধ করতে 'autoflush=False' এবং
# ডাটাবেজ ইঞ্জিনের সাথে সেশন বাইন্ড করতে 'bind=engine' ব্যবহার করা হয়েছে।



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Explanation: Here, 'def get_db():' defines a generator function to supply database sessions; 'db = SessionLocal()'
# creates a new session instance; 'try: yield db' safely provides the session to endpoints; and 'finally: db.close()'
# guarantees that the session closes to prevent connection leaks.
# বাংলা ব্যাখ্যা: এখানে, 'def get_db():' দিয়ে ডাটাবেজ সেশন সাপ্লাই করার জন্য একটি জেনারেটর ফাংশন ডিফাইন করা হয়েছে; 'db = SessionLocal()'
# নতুন সেশন ইনস্ট্যান্স তৈরি করে; 'try: yield db' এন্ডপয়েন্টে নিরাপদে সেশন সরবরাহ করে; এবং 'finally: db.close()' কানেকশন লিক রোধ করতে
# সেশন ক্লোজ করা নিশ্চিত করে।











"""
প্রতিটা লাইন কেন:
create_engine(...): engine হলো SQLAlchemy-র সেই object যেটা আসলে database-এর সাথে network-level connection চালায়। এটা একবারই বানানো হয়, পুরো app জুড়ে reuse হয়।
settings.sb_connection_string: এখানেই আগের config.py-এর কাজে লাগল — password code-এ hardcode না করে নিরাপদে আসছে।
sessionmaker(...): SessionLocal একটা factory — মানে SessionLocal() call করলেই একটা নতুন session (database-এর সাথে কথা বলার একটা "conversation") তৈরি হয়। প্রতিটা API request-এর জন্য আলাদা session লাগবে, এই কারণেই factory বানিয়ে রাখা হয়, সরাসরি একটা single session না।
autocommit=False: মানে আমরা নিজে বলার আগে কোনো change database-এ সরাসরি save (commit) হবে না — এটা ইচ্ছাকৃত নিয়ন্ত্রণ রাখার জন্য, ভুল data accidentally save হওয়া থেকে বাঁচায়।
autoflush=False: SQLAlchemy-কে বলছি প্রতিটা query-এর আগে নিজে থেকে pending change পাঠিয়ে না দিতে। এটাও আমাদের নিয়ন্ত্রণে রাখে কখন data পাঠানো হবে।
এই file-এ যা এখনো নেই, ইচ্ছাকৃতভাবে

get_db() নামে একটা dependency function লাগবে যেটা router.py-তে প্রতিটা endpoint-এ session সরবরাহ করবে। সেটা এখনই যোগ করছি না, কারণ আগে models.py বানিয়ে table কেমন হবে সেটা ঠিক করে নেওয়া ভালো, তারপর get_db()-এর ব্যবহার একসাথে বোঝা সহজ হবে।
"""

