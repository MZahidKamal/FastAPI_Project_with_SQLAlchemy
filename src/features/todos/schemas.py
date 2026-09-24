from pydantic import BaseModel
from datetime import datetime

# Explanation: Here, 'BaseModel' is imported from 'pydantic' for defining data validation schemas, and 'datetime' is
# imported from 'datetime' module to handle date and time values.
# বাংলা ব্যাখ্যা: এখানে, ডাটা ভ্যালিডেশন স্কিমা ডিফাইন করার জন্য 'pydantic' থেকে 'BaseModel' এবং তারিখ ও সময় ম্যানেজ করার জন্য 'datetime'
# মডিউল থেকে 'datetime' ইমপোর্ট করা হয়েছে।



class TodoBase(BaseModel):
    title: str
    description: str | None = None
    priority: int = 1
    completed: bool = False

# Explanation: Here, class 'TodoBase' inherits 'BaseModel'; attribute 'title: str' is a required string;
# 'description: str | None = None' is an optional string defaulting to 'None'; 'priority: int = 1' is an integer
# defaulting to '1' for task priority; and 'completed: bool = False' is a boolean defaulting to 'False' so new tasks are
# marked incomplete.
# বাংলা ব্যাখ্যা: এখানে, 'TodoBase' ক্লাসটি 'BaseModel' থেকে ইনহেরিট করেছে; 'title: str' একটি বাধ্যতামূলক স্ট্রিং; 'description: str | None = None'
# একটি অপশনাল স্ট্রিং যার ডিফল্ট মান 'None'; 'priority: int = 1' হলো টাস্ক প্রাইওরিটির জন্য যার ডিফল্ট মান '1'; এবং 'completed: bool = False'
# হলো বুলিয়ান যার ডিফল্ট মান 'False' যাতে নতুন টাস্কগুলো অসম্পূর্ণ থাকে।



class TodoCreate(TodoBase):
    pass

# Explanation: Here, class 'TodoCreate' inherits from 'TodoBase' using keyword 'pass' without adding new fields, designed
# specifically for incoming creation payloads.
# বাংলা ব্যাখ্যা: এখানে, নতুন কোনো ফিল্ড যোগ না করে 'pass' কিওয়ার্ড ব্যবহার করে 'TodoCreate' ক্লাসটি 'TodoBase' থেকে ইনহেরিট করা হয়েছে, যা
# ইনকামিং ক্রিয়েশন পে-লোডের জন্য ব্যবহৃত হয়।



class TodoResponse(TodoBase):
    id: int
    created_at: datetime

# Explanation: Here, class 'TodoResponse' inherits from 'TodoBase' and adds 'id: int' for the database identifier and
# 'created_at: datetime' for the timestamp to represent outgoing response payloads.
# বাংলা ব্যাখ্যা: এখানে, 'TodoResponse' ক্লাসটি 'TodoBase' থেকে ইনহেরিট করে ডাটাবেজ আইডেন্টিফায়ারের জন্য 'id: int' এবং টাইমস্ট্যাম্পের জন্য
# 'created_at: datetime' যোগ করেছে যা আউটগোয়িং রেসপন্স পে-লোডের জন্য ব্যবহৃত হয়।










"""
Type-এর সিদ্ধান্তগুলো কেন এমন

- **`title: str`**: বাধ্যতামূলক, `default` নেই।
- **`description: str | None = None`**: সবাই description লিখবে না, তাই `Optional`। `str | None` মানে হয় `string` হবে, নাহলে `None`। `default = None` দেওয়ায় এই field না দিলেও চলবে।
- **`priority: int = 1`**: আপাতত simple `int` রাখলাম (যেমন `1`, `2`, `3`)। এটা পরে চাইলে `Enum` (`low`/`medium`/`high`) দিয়ে ভালোভাবে লেখা যায়, কিন্তু সেটা একটা নতুন concept, তাই এখন শুধু `int` দিয়ে শুরু করছি।
- **`completed: bool = False`**: নতুন `todo` তৈরি হলে default-ভাবে অসম্পূর্ণ থাকবে।

## একটা জিনিস খেয়াল করুন
`str | None` syntax কাজ করতে Python `3.10+` লাগে। আপনার `.venv`-এ Python `3.14` আছে (আগের screenshot-এ দেখেছিলাম), তাই সমস্যা হবে না।

লিখে ফেলুন, তারপর জানান কোনো লাল দাগ/error আছে কি না। এরপর Step 4-এ `TodoCreate` আর `TodoResponse` বানিয়ে বোঝাব `id` কেন আলাদাভাবে যোগ হয়।
"""


"""
## কেন দুটো আলাদা class লাগে
- **`TodoCreate(TodoBase)`**: user যখন নতুন `todo` বানাতে `POST` করবে, তখন `request body`-তে এই shape লাগবে। এখানে `TodoBase`-এর সব field-ই আছে, নতুন কিছু নেই, তাই শুধু `pass` লিখে বলছি হুবহু `TodoBase`-এর মতোই"। আলাদা class কেন বানালাম যদি হুবহু একই? কারণ ভবিষ্যতে `create`-এর সময় আলাদা কোনো rule লাগলে (যেমন `title` অন্তত ৩ অক্ষর) শুধু এই class-এ বদলাব, `TodoBase` বা `TodoResponse` ছোঁব না।
- **`TodoResponse(TodoBase)`**: `database` থেকে `todo` ফেরত পাঠানোর সময় এই shape ব্যবহার হবে। এখানে `TodoBase`-এর সব field + নতুন `id: int`। আগে বলেছিলাম, `id` user দেয় না, `database` বানায়, তাই এটা শুধু `response`-এ থাকে, `create`-এ না।
"""

