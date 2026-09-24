from sqlalchemy.orm import declarative_base

# Explanation: Here, 'declarative_base' is imported from 'sqlalchemy.orm' to provide the structural foundation for
# defining database ORM models.
# বাংলা ব্যাখ্যা: এখানে, ডাটাবেজ ওআরএম মডেল ডিফাইন করার জন্য স্ট্রাকচারাল ভিত্তি প্রদান করতে 'sqlalchemy.orm' থেকে 'declarative_base'
# ইমপোর্ট করা হয়েছে।



Base = declarative_base()

# Explanation: Here, 'Base = declarative_base()' instantiates the base class assigned to variable 'Base', which acts as
# the foundational parent class for all SQLAlchemy database models in the project.
# বাংলা ব্যাখ্যা: এখানে, 'Base = declarative_base()' এর মাধ্যমে বেস ক্লাস ইনস্ট্যান্স তৈরি করে 'Base' ভ্যারিয়েবলে অ্যাসাইন করা হয়েছে, যা প্রজেক্টের
# সব SQLAlchemy ডাটাবেজ মডেলের মূল প্যারেন্ট ক্লাস হিসেবে কাজ করে।










"""
কেন এই ছোট file আলাদা করে লাগে:
Base: এটা একটা special class, যেটা SQLAlchemy-কে বলে "এখান থেকে যত class inherit করবে, প্রতিটাকেই একটা database table হিসেবে 
ধরো"। Step 7-এ আমরা Todo class বানাব যেটা Base-কে inherit করবে — তখনই এটা কাজে লাগবে।

আলাদা file কেন, session.py-তেই কেন লিখলাম না: 
বড় project-এ অনেক feature (todos, users, auth) থাকে, প্রতিটার নিজস্ব models.py থাকে। কিন্তু সবার একই Base ব্যবহার করা জরুরি, নাহলে 
SQLAlchemy table-গুলোকে ঠিকমতো চিনতে পারবে না। তাই Base একটা central, শেয়ার করা জায়গায় (db/base.py) রাখা হয়, যাতে প্রতিটা feature 
সেখান থেকে import করে ব্যবহার করে, নিজে নিজে নতুন Base না বানায়।
"""

