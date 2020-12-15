from flask import Flask, request
from mysql import connector as mysql

# Insert your respective database authentications, just as in generate_db.py
HOST = "localhost"
DATABASE = "medium_clone"
USER = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"


app = Flask(__name__)


@app.route("/")
def hello_world():
    """Home route, this is the home root the default root your server respond"""
    routes = "users/id, users, topics, topics/id, posts, posts/id"
    return f"Welcome to my first API! These are the routes that this api responds to: {routes}"


@app.route("/users", methods=["GET"])
def get_users():
    """Users route. method = GET, this route will return all the user in existence"""

    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries in the database
    my_cursor = db_connection.cursor(dictionary=True)

    # Execute query
    my_cursor.execute("SELECT * FROM users")

    # Store all users retrieved
    all_users = my_cursor.fetchall()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    if all_users is None or len(all_users) == 0:
        res = {
            "status": 200,
            "message": "There are no users in the Database",
            "data": [],
        }
    else:
        # Return all the users
        res = {"status": 200, "data": all_users, "message": "successful"}

    return res


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Users route. method = GET, this route will return ONLY the user with the
    matching ID"""

    # Cleaning up the searched username
    clean_username = username[1:]

    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries to the database
    my_cursor = db_connection.cursor(dictionary=True, buffered=True)

    # Execute query
    query_user = "SELECT * FROM users WHERE username=%s"
    query_username = (clean_username,)
    my_cursor.execute(query_user, params=query_username)

    # Store the results of the executed query
    user = my_cursor.fetchone()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    if user is None or len(user) == 0:
        # Final API response. 404 status code means that the server don't found the resource
        res = {
            "status": 404,
            "message": "There is no users with that id in the database",
        }, 404
    else:
        # Return all the users
        res = {"status": 200, "response": "The selected user", "data": user}

    return res


@app.route("/users", methods=["POST"])
def create_user():
    """User route. method = POST, this route manage the creation of new users"""

    new_user = {
        "username": request.json["username"],
        "password": request.json["password"],
        "email": request.json["email"],
        "first_name": request.json["first_name"],
        "last_name": request.json["last_name"],
    }

    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries to the database
    my_cursor = db_connection.cursor(dictionary=True)

    # Execute query
    query_create_user = "INSERT INTO users (create_at,username,password,email,first_name,last_name) VALUES (now(), %s, %s, %s, %s, %s)"
    data = (
        new_user["username"],
        new_user["password"],
        new_user["email"],
        new_user["first_name"],
        new_user["last_name"],
    )
    my_cursor.execute(query_create_user, params=data)

    # Commit the changes to the database
    db_connection.commit()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    # return new user with a HTTP status code of 201
    res = {"message": "User successfully", "data": new_user, "status": 201}
    return res, 201


@app.route("/topics", methods=["POST"])
def create_topic():
    """Topics route. method = POST, this route manage the creation of new TOPIC"""

    new_topic = {
        "name": request.json["name"],
        "description": request.json["description"],
        "topic_picture": request.json["topic_picture"],
        "slug": request.json["slug"],
    }

    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries in the database
    my_cursor = db_connection.cursor(dictionary=True)

    # Execute query
    query_create_topic = "INSERT INTO topics (create_at,name,description,topic_picture,slug) VALUES (now(), %s, %s, %s, %s)"

    data = (
        new_topic["name"],
        new_topic["description"],
        new_topic["topic_picture"],
        new_topic["slug"],
    )

    my_cursor.execute(query_create_topic, params=data)

    # Commit the changes to the database
    db_connection.commit()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    # return new user with a HTTP status code of 201
    res = {"data": new_topic, "status": 201, "message": "Topic successfully created"}
    return res, 201


@app.route("/topics", methods=["GET"])
def get_topics():
    """Topics route. method = GET, this route will return all the topics in
    existence"""

    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries to the database
    my_cursor = db_connection.cursor(dictionary=True)

    # Execute query
    my_cursor.execute("SELECT * FROM topics")

    all_topics = my_cursor.fetchall()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    if all_topics is None or len(all_topics) == 0:
        res = {
            "status": 200,
            "message": "There is no topics in the database",
            "data": [],
        }
    else:
        # Return all the topics
        res = {"message": "All register topics", "data": all_topics, "status": 200}

    return res


@app.route("/topics/<int:id>", methods=["GET"])
def get_topic(id):
    """Topics route. method = GET, this route will return ONLY the topic with the matching ID"""

    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries in the database
    my_cursor = db_connection.cursor(dictionary=True)

    # Execute query
    query_topic = "SELECT * FROM topics WHERE id=%s"
    topic_id = (id,)
    my_cursor.execute(query_topic, params=topic_id)

    # Store the results of the executed query
    topic = my_cursor.fetchone()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    if topic is None or len(topic) == 0:
        # Final API  response. 404 status code means that the server don't found the resource
        res = {
            "response": "There is no topics with that id in the database",
            "status": 404,
        }, 404
    else:
        # Return all the topics
        res = {"status": 200, "response": "The selected topic", "data": topic}

    return res


@app.route("/posts", methods=["POST"])
def create_post():
    """Post route. method = POST, this route manage the creation of new POST"""

    new_post = {
        "post_title": request.json["post_title"],
        "post_image": request.json["post_image"],
        "short_description": request.json["short_description"],
        "body": request.json["body"],
        "user_id": request.json["user_id"],
        "topic_id": request.json["topic_id"],
    }

    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries in the database
    my_cursor = db_connection.cursor(dictionary=True)

    # Execute query
    query_create_post = "INSERT INTO posts (create_at,post_title,post_image,short_description,body,user_id,topic_id) VALUES (now(), %s, %s, %s, %s, %s, %s)"

    data = (
        new_post["post_title"],
        new_post["post_image"],
        new_post["short_description"],
        new_post["body"],
        new_post["user_id"],
        new_post["topic_id"],
    )

    my_cursor.execute(query_create_post, params=data)

    # Commit the changes to the database
    db_connection.commit()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    # return new post with a HTTP status code of 201
    res = {"data": new_post, "status": 201, "message": "Post successfully created"}
    return res, 201


@app.route("/posts", methods=["GET"])
def get_posts():
    """Post route. method = GET, this route will return all the posts in existence"""

    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries in the database
    my_cursor = db_connection.cursor(dictionary=True)

    # Execute query
    my_cursor.execute("SELECT * FROM posts")

    all_posts = my_cursor.fetchall()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    if all_posts is None or len(all_posts) == 0:
        res = {
            "status": 200,
            "response": "There is no posts in the database",
            "data": [],
        }
    else:
        # Return all the posts
        res = {"status": 200, "message": "All register posts", "data": all_posts}

    return res


@app.route("/posts/<int:id>", methods=["GET"])
def get_post(id):
    """Posts route. method = GET, this route will return ONLY the posts with the
    matching ID"""

    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries in the database
    my_cursor = db_connection.cursor(dictionary=True)

    # Execute query
    query_post = "SELECT * FROM posts WHERE id=%s"
    post_id = (id,)
    my_cursor.execute(query_post, params=post_id)

    # Store the results of the executed query
    post = my_cursor.fetchone()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    if post is None or len(post) == 0:
        # Final API  response. 404 status code means that the server don't found the resource
        res = {
            "status": 404,
            "message": "There is no post with that id in the database",
        }, 404
    else:
        # Return all the posts
        res = {"status": 200, "message": "The selected post", "data": post}

    return res


if __name__ == "__main__":
    app.run(debug=True)
