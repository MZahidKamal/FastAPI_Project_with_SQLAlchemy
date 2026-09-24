from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from src.core.config import settings
from src.db.base import Base
from src.features.todos import models  # noqa: F401

# Explanation: Here, imports from 'logging.config', 'sqlalchemy', 'alembic', and custom configuration and model modules
# load necessary tools for Alembic database migration execution, logging setup, and metadata tracking.
# বাংলা ব্যাখ্যা: এখানে, 'logging.config', 'sqlalchemy', 'alembic' এবং কাস্টম কনফিগারেশন ও মডেল মডিউলগুলো থেকে ইমপোর্ট করার মাধ্যমে
# অ্যালেম্বিক ডাটাবেজ মাইগ্রেশন এক্সিকিউশন, লগিং সেটআপ এবং মেটাডেটা ট্র্যাক করার প্রয়োজনীয় টুলসগুলো লোড করা হয়েছে।



config = context.config

config.set_main_option("sqlalchemy.url", settings.sb_connection_string)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Explanation: Here, 'config = context.config' fetches the Alembic configuration context;
# 'config.set_main_option("sqlalchemy.url", settings.sb_connection_string)' dynamically sets the database connection
# string using 'settings.sb_connection_string' from environment settings; and the conditional block checks if
# 'config.config_file_name' is available to configure the logging environment using 'fileConfig(config.config_file_name)'.
# বাংলা ব্যাখ্যা: এখানে, 'config = context.config' দিয়ে অ্যালেম্বিক কনফিগারেশন কন্টেক্সট ফেচ করা হয়েছে;
# 'config.set_main_option("sqlalchemy.url", settings.sb_connection_string)' এর মাধ্যমে এনভায়রনমেন্ট সেটিংসের
# 'settings.sb_connection_string' ব্যবহার করে ডাইনামিকভাবে ডাটাবেজ কানেকশন স্ট্রিং সেট করা হয়েছে; এবং কন্ডিশনাল ব্লকে
# 'config.config_file_name' থাকলে 'fileConfig(config.config_file_name)' দিয়ে লগিং এনভায়রনমেন্ট কনফিগার করা হয়েছে।



target_metadata = Base.metadata

# Explanation: Here, 'target_metadata = Base.metadata' assigns the SQLAlchemy metadata object from 'Base', allowing
# Alembic to autogenerate migrations by tracking model schema definitions.
# বাংলা ব্যাখ্যা: এখানে, 'target_metadata = Base.metadata' এর মাধ্যমে 'Base' থেকে এসকিউএলএলকেমি মেটাডেটা অবজেক্ট অ্যাসাইন করা হয়েছে,
# যা অ্যালেম্বিককে মডেল স্কিমা ডেফিনিশন ট্র্যাক করে স্বয়ংক্রিয়ভাবে মাইগ্রেশন জেনারেট করার সুযোগ দেয়।



def run_migrations_offline() -> None:
    # Run migrations in 'offline' mode.
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Explanation: Here, 'def run_migrations_offline() -> None:' defines the function to execute migrations in offline mode
# without a live database connection; 'url = config.get_main_option("sqlalchemy.url")' gets the connection URI;
# 'context.configure(...)' sets up the offline parameters with 'literal_binds=True' for direct SQL generation and
# 'dialect_opts={"paramstyle": "named"}' for named parameter formatting; and the context manager executes the migration
# transaction.
# বাংলা ব্যাখ্যা: এখানে, লাইভ ডাটাবেজ কানেকশন ছাড়াই অফলাইন মোডে মাইগ্রেশন রান করার জন্য 'def run_migrations_offline() -> None:'
# ফাংশন ডিফাইন করা হয়েছে; 'url = config.get_main_option("sqlalchemy.url")' কানেকশন ইউআরআই নেয়; সরাসরি এসকিউএল জেনারেশনের জন্য
# 'literal_binds=True' এবং নেমড প্যারামিটার ফরম্যাটিংয়ের জন্য 'dialect_opts={"paramstyle": "named"}' দিয়ে 'context.configure(...)'
# অফলাইন প্যারামিটার সেটআপ করে; এবং কন্টেক্সট ম্যানেজার মাইগ্রেশন ট্রানজেকশন এক্সিকিউট করে।



def run_migrations_online() -> None:
    # Run migrations in 'online' mode.
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

# Explanation: Here, 'def run_migrations_online() -> None:' defines the function for online mode migrations using an
# active database connection; 'connectable = engine_from_config(...)' creates an engine using configuration sections
# where 'prefix="sqlalchemy."' filters config keys and 'poolclass=pool.NullPool' prevents connection pooling issues
# during migrations; and the connection context configures the live connection and target metadata to execute the
# migrations within a transaction block.
# বাংলা ব্যাখ্যা: এখানে, অ্যাক্টিভ ডাটাবেজ কানেকশন ব্যবহার করে অনলাইন মোডে মাইগ্রেশন রান করার জন্য 'def run_migrations_online() -> None:'
# ফাংশন ডিফাইন করা হয়েছে; 'connectable = engine_from_config(...)' কনফিগারেশন সেকশন ব্যবহার করে ইঞ্জিন তৈরি করে যেখানে
# 'prefix="sqlalchemy."' কনফিগার কি ফিল্টার করে এবং 'poolclass=pool.NullPool' মাইগ্রেশনের সময় কানেকশন পুলিং সমস্যা রোধ করে; এবং
# কানেকশন কন্টেক্সট লাইভ কানেকশন ও টার্গেট মেটাডেটা কনফিগার করে ট্রানজেকশন ব্লকের মধ্যে মাইগ্রেশন এক্সিকিউট করে।



if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

# Explanation: Here, the conditional check 'if context.is_offline_mode():' evaluates whether Alembic is running in
# offline mode, invoking 'run_migrations_offline()' if true, or else executing 'run_migrations_online()' to perform
# migrations against the live database server.
# বাংলা ব্যাখ্যা: এখানে, কন্ডিশনাল চেক 'if context.is_offline_mode():' যাচাই করে যে অ্যালেম্বিক অফলাইন মোডে চলছে কি না, সত্য হলে
# 'run_migrations_offline()' কল করে, অন্যথায় লাইভ ডাটাবেজ সার্ভারের সাপেক্ষে মাইগ্রেশন সম্পন্ন করতে 'run_migrations_online()' এক্সিকিউট
# করে।

