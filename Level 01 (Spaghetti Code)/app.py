from flask import Flask, request
import mysql.connector as mysql

# Insert your respective database authentications same has in generate_db.py
HOST = "localhost"
DATABASE = "medium_clone"
USER = "YOUR_USER"
PASSWORD = "YOUR_PASSWORD"


app = Flask(__name__)


# Home route, this is the home root the default root your server respond
@app.route("/")
def hello_world():
    routes = "get-users/id, create-user, create-topic, get-topics/id,create-post, get-posts/id"
    return f"Welcome to my first API! This are the routes that this api receives to {routes}"


# Users route. method = GET, this route will return all the user in existence
@app.route("/get-users", methods=["GET"])
def get_users():
    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries to the database
    my_cursor = db_connection.cursor()

    # Execute query
    my_cursor.execute("SELECT * FROM users")

    all_users = my_cursor.fetchall()

    if len(all_users) == 0:
        return {"response": "There is no users in the database"}
    else:
        # Commit the changes to the database
        db_connection.commit()

        # Close database connections
        my_cursor.close()
        db_connection.close()

        # Return all the users
        return {"response": "All register users", "users": all_users}


# Users route. method = GET, this route will return ONLY the user with the matching ID
@app.route("/get-users/<int:id>", methods=["GET"])
def get_user(id):
    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries to the database
    my_cursor = db_connection.cursor()

    # Execute query
    my_cursor.execute(f"SELECT * FROM users WHERE id='{id}'")

    # Store the results of the executed query
    user = my_cursor.fetchall()

    if len(user) == 0:
        # return if there its not users in DB
        return {"response": "There is no users with that id in the database"}
    else:
        # Commit the changes to the database
        db_connection.commit()

        # Close database connections
        my_cursor.close()
        db_connection.close()

        # Return all the users
        return {"response": "The selected user", "user": user}


# User route. method = POST, this route manage the creation of new users
@app.route("/create-user", methods=["POST"])
def create_user():
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
    my_cursor = db_connection.cursor()

    # Execute query
    my_cursor.execute(
        f"INSERT INTO users (create_at,username,password,email,first_name,last_name) VALUES (now(),'{new_user['username']}','{new_user['password']}','{new_user['email']}','{new_user['first_name']}','{new_user['last_name']}')"
    )

    # Commit the changes to the database
    db_connection.commit()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    # return new user with a HTTP status code of 201
    return new_user, 201


# Topics route. method = POST, this route manage the creation of new TOPIC
@app.route("/create-topic", methods=["POST"])
def create_topic():
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

    # Create 'Cursor' to execute queries to the database
    my_cursor = db_connection.cursor()

    # Execute query
    my_cursor.execute(
        f"INSERT INTO topics (create_at,name,description,topic_picture,slug) VALUES (now(),'{new_topic['name']}','{new_topic['description']}','{new_topic['topic_picture']}','{new_topic['slug']}')"
    )

    # Commit the changes to the database
    db_connection.commit()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    # return new user with a HTTP status code of 201
    return new_topic, 201


# Topics route. method = GET, this route will return all the topics in existence
@app.route("/get-topics", methods=["GET"])
def get_topics():
    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries to the database
    my_cursor = db_connection.cursor()

    # Execute query
    my_cursor.execute("SELECT * FROM topics")

    all_topics = my_cursor.fetchall()

    if len(all_topics) == 0:
        return {"response": "There is no topics in the database"}
    else:
        # Commit the changes to the database
        db_connection.commit()

        # Close database connections
        my_cursor.close()
        db_connection.close()

        # Return all the topics
        return {"response": "All register topics", "topics": all_topics}


# Topics route. method = GET, this route will return ONLY the topic with the matching ID
@app.route("/get-topics/<int:id>", methods=["GET"])
def get_topic(id):
    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries to the database
    my_cursor = db_connection.cursor()

    # Execute query
    my_cursor.execute(f"SELECT * FROM topics WHERE id='{id}'")

    # Store the results of the executed query
    topic = my_cursor.fetchall()

    if len(topic) == 0:
        # return if there its not users in DB
        return {"response": "There is no topics with that id in the database"}
    else:
        # Commit the changes to the database
        db_connection.commit()

        # Close database connections
        my_cursor.close()
        db_connection.close()

        # Return all the topics
        return {"response": "The selected topic", "topic": topic}


# Post route. method = POST, this route manage the creation of new POST
@app.route("/create-post", methods=["POST"])
def create_post():
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

    # Create 'Cursor' to execute queries to the database
    my_cursor = db_connection.cursor()

    # Execute query
    my_cursor.execute(
        f"INSERT INTO posts (create_at,post_title,post_image,short_description,body,user_id,topic_id) VALUES (now(),'{new_post['post_title']}','{new_post['post_image']}','{new_post['short_description']}','{new_post['body']}','{new_post['user_id']}','{new_post['topic_id']}')"
    )

    # Commit the changes to the database
    db_connection.commit()

    # Close database connections
    my_cursor.close()
    db_connection.close()

    # return new post with a HTTP status code of 201
    return new_post, 201


# Post route. method = GET, this route will return all the posts in existence
@app.route("/get-posts", methods=["GET"])
def get_posts():
    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries to the database
    my_cursor = db_connection.cursor()

    # Execute query
    my_cursor.execute("SELECT * FROM posts")

    all_posts = my_cursor.fetchall()

    if len(all_posts) == 0:
        return {"response": "There is no posts in the database"}
    else:
        # Commit the changes to the database
        db_connection.commit()

        # Close database connections
        my_cursor.close()
        db_connection.close()

        # Return all the posts
        return {"response": "All register posts", "posts": all_posts}


# Posts route. method = GET, this route will return ONLY the posts with the matching ID
@app.route("/get-posts/<int:id>", methods=["GET"])
def get_post(id):
    # Connect to mysql Database
    db_connection = mysql.connect(
        host=HOST, database=DATABASE, user=USER, password=PASSWORD
    )

    # Create 'Cursor' to execute queries to the database
    my_cursor = db_connection.cursor()

    # Execute query
    my_cursor.execute(f"SELECT * FROM posts WHERE id='{id}'")

    # Store the results of the executed query
    post = my_cursor.fetchall()

    if len(post) == 0:
        # return if there its not users in DB
        return {"response": "There is no post with that id in the database"}
    else:
        # Commit the changes to the database
        db_connection.commit()

        # Close database connections
        my_cursor.close()
        db_connection.close()

        # Return all the posts
        return {"response": "The selected post", "post": post}


if __name__ == "__main__":
    app.run(debug=True)