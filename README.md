### Data Modeling Exercises

**Objective:**

In this assignment, you will modify the data model to conform to the following requirements:

  1. Users can have only 1 email, and it is required (not NULLable)
  1. Make the `Posts` table a **weak entity** by using a composite primary key. 
  1. Update related tables and queries to accommodate this change.

Save the modified schema into a file called `answer.sql`

---

### **Current Data Model and Sample Data**

```sql
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL
);

CREATE TABLE Emails (
    user_id INTEGER NOT NULL,
    email TEXT NOT NULL,
    PRIMARY KEY (user_id, email),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Follows (
    user_id INTEGER NOT NULL,
    follower_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, follower_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (follower_id) REFERENCES Users(id)
);

CREATE TABLE Posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Likes (
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, post_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (post_id) REFERENCES Posts(id)
);

-- Insert Users
INSERT INTO Users (username) VALUES
('alice'),
('bob'),
('charlie'),
('dave');

-- Insert Emails
INSERT INTO Emails (user_id, email) VALUES
(1, 'alice@example.com'),
(2, 'bob@example.com'),
(3, 'charlie@example.com'),
(4, 'dave@example.com');

-- Insert Follows (who follows whom)
INSERT INTO Follows (user_id, follower_id) VALUES
(1, 2), -- Bob follows Alice
(1, 3), -- Charlie follows Alice
(2, 3), -- Charlie follows Bob
(3, 4); -- Dave follows Charlie

-- Insert Posts
INSERT INTO Posts (user_id, content) VALUES
(1, 'Hello world!'),
(1, 'Hello again!'),
(2, 'This is my first post!'),
(3, 'I love databases!'),
(3, 'I love JSON!'),
(4, 'SQL is awesome!');

-- Insert Likes (who likes which post)
INSERT INTO Likes (user_id, post_id) VALUES
(2, 1), -- Bob likes Alice's post
(3, 1), -- Charlie likes Alice's post
(3, 2), -- Charlie likes Bob's post
(4, 3); -- Dave likes Charlie's post
```
### Submit Assignment

Test your solution by executing the following command on the bash terminal:

```shell
$ pytest
```

When you are satisified, execute the following commands to submit:

```shell
$ git add -A
$ git commit -m 'submit'
$ git push
```
