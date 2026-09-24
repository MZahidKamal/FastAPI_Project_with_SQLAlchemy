from pydantic_settings import BaseSettings, SettingsConfigDict

# Explanation: Here, 'BaseSettings' and 'SettingsConfigDict' are imported from 'pydantic_settings' to handle environment
# variable configuration, management, and validation.
# বাংলা ব্যাখ্যা: এখানে, এনভায়রনমেন্ট ভেরিয়েবল কনফিগারেশন, ম্যানেজমেন্ট এবং ভ্যালিডেশনের জন্য 'pydantic_settings' থেকে 'BaseSettings' এবং
# 'SettingsConfigDict' ক্লাস ইমপোর্ট করা হয়েছে।



class Settings(BaseSettings):
    sb_connection_string: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

# Explanation: Here, class 'Settings' inherits 'BaseSettings'; 'sb_connection_string: str' specifies a required string
# attribute for the database connection; and 'model_config = SettingsConfigDict(env_file=".env", extra="ignore")' configures
# Pydantic to read environment variables from '.env' file using 'env_file=".env"' while 'extra="ignore"' is set to safely
# ignore any extra unexpected variables without throwing errors.
# বাংলা ব্যাখ্যা: এখানে, 'Settings' ক্লাসটি 'BaseSettings' থেকে ইনহেরিট করেছে; 'sb_connection_string: str' ডাটাবেজ কানেকশনের জন্য একটি
# বাধ্যতামূলক স্ট্রিং অ্যাট্রিবিউট নির্ধারণ করে; এবং 'model_config = SettingsConfigDict(env_file=".env", extra="ignore")' এর মাধ্যমে '.env'
# ফাইল থেকে ভেরিয়েবল পড়তে 'env_file=".env"' ব্যবহার করা হয়েছে যেখানে 'extra="ignore"' অতিরিক্ত কোনো ভেরিয়েবল থাকলে সেটিতে কোনো এরর
# না দিয়ে সেগুলোকে নিরাপদে ইগনোর করার অনুমতি দেয়।



settings = Settings()

# Explanation: Here, 'settings = Settings()' instantiates the 'Settings' class, which automatically triggers loading,
# parsing, and validation of environment variables defined in the application configuration.
# বাংলা ব্যাখ্যা: এখানে, 'settings = Settings()' কোডের মাধ্যমে 'Settings' ক্লাসের একটি ইনস্ট্যান্স তৈরি করা হয়েছে, যা অ্যাপ্লিকেশনের কনফিগারেশনে
# ডিফাইন করা এনভায়রনমেন্ট ভেরিয়েবলগুলোকে স্বয়ংক্রিয়ভাবে লোড, পার্স এবং ভ্যালিডেশন করে।










"""
এখানে কী হচ্ছে
BaseSettings: Pydantic-এর special class, যেটা environment variable/.env file থেকে automatic data পড়ে। Pydantic Settings শুধু যেগুলো class-এ declare করা আছে সেগুলোই পড়ে, বাকিগুলো ignore করে।
sb_connection_string: str: বলছি .env-এ SB_CONNECTION_STRING নামে একটা variable থাকবে, সেটা string হবে। নাম মিলতে হবে (case-insensitive, তাই SB_CONNECTION_STRING আর sb_connection_string মিলে যায়)।
env_file = ".env": Pydantic-কে বলছি কোন file থেকে পড়তে হবে।
settings = Settings(): এই object-টা আমরা পরে db/session.py-তে import করে ব্যবহার করব।
"""

