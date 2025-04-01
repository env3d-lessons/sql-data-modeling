import sqlite3
import pytest

def execute_sql_script(cursor, script):
    """Executes the given SQL script and ensures no errors occur."""
    try:
        cursor.executescript(script)
    except sqlite3.Error as e:
        pytest.fail(f"SQL execution failed: {e}")

@pytest.fixture(scope='session')
def cursor():
    """Creates an in-memory SQLite database and returns a connection."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    schema_script = open('answer.sql').read()
    execute_sql_script(cursor, schema_script)
    yield cursor
    conn.close()

def test_user_email(cursor):
    # Check Users table has an email field
    cursor.execute("PRAGMA table_info(Users);")
    users_columns = {col[1] for col in cursor.fetchall()}
    assert "email" in users_columns, "Users table should have an 'email' column"

def get_posts_pk(cursor):
    cursor.execute("PRAGMA index_list(Posts);")
    indexes = cursor.fetchall()    
    for index in indexes:                
        index_name = index[1]        
        if "pk" in index[3].lower():
            cursor.execute(f"PRAGMA index_info({index_name});")
            index_columns = [col[2] for col in cursor.fetchall()]            
            # Check if there is more than one column in the primary key (composite)
            if len(index_columns) > 1:
                return index_columns
    return []


def test_post_composite_index(cursor):
    assert len(get_posts_pk(cursor)) > 1, "Posts table should have a composite primary key"
    
def test_likes(cursor):
    posts_pk = get_posts_pk(cursor)
    # Check Likes table has an additional column
    cursor.execute("PRAGMA table_info(Likes);")
    likes_columns = {col[1] for col in cursor.fetchall()}
    assert len(likes_columns) > 2, "Likes table should have more than 2 columns"
    for col in posts_pk:
        assert col in likes_columns, "Likes table should have all the columns from the Posts composite key"

