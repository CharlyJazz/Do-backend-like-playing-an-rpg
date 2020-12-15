# This script is here only to generate the database and tables we will be working with.
# Just add your credentials for your installation of mysql and run it on the terminal.
# On a side note, if you ever want to restart the data base from 0 just run it again.

from mysql import connector as mysql

# insert your respective MYSQL data here
HOST = "localhost"  # the host in which your database runs, shouldn't need to be changed
DATABASE = "medium_clone"  # the database name is up to you but this one is simplie and understable
USER = "YOUR USER"  # here goes your username to connect to MySQL
PASSWORD = "YOUR_PASSWORD"  # here goes the password you use to connect to MySQL


# connect to mysql
db_connection = mysql.connect(host=HOST, user=USER, password=PASSWORD)


# cursor mysql connection
my_cursor = db_connection.cursor()


# database statements
check_database = f"DROP DATABASE IF EXISTS `{DATABASE}`"
create_database = f"CREATE DATABASE IF NOT EXISTS `{DATABASE}`"


# helper to check the existence of the tables
def check_table(table):
    return f"DROP TABLE IF EXISTS `{DATABASE}`.`{table}`"


check_table_users = check_table("users")
create_table_users = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`users` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NOT NULL,
    `update_at` DATETIME NULL,
    `username` VARCHAR(20) UNIQUE NOT NULL,
    `password` VARCHAR(15) NOT NULL,
    `email` VARCHAR(255) UNIQUE NOT NULL,
    `first_name` VARCHAR(45) NOT NULL,
    `last_name` VARCHAR(45) NOT NULL,
    `bio` VARCHAR(80) NULL,
    `user_picture` TEXT NULL,
    `active` TINYINT NOT NULL DEFAULT 1,
    `token` VARCHAR(25) NULL,
    `toke_at` DATETIME NULL,
    PRIMARY KEY (`id`));"""


check_table_topics = check_table("topics")
create_table_topics = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`topics` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NOT NULL,
    `update_at` DATETIME NULL,
    `name` VARCHAR(15) NOT NULL,
    `description` VARCHAR(45) NOT NULL,
    `topic_picture` TEXT NOT NULL,
    `slug` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`id`));"""


check_table_tags = check_table("tags")
create_table_tags = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`tags` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NOT NULL,
    `update_at` DATETIME NULL,
    `name` VARCHAR(30) NOT NULL,
    `slug` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`id`));"""


check_table_posts = check_table("posts")
create_table_posts = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`posts` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NOT NULL,
    `update_at` DATETIME NULL,
    `post_title` VARCHAR(100) NOT NULL,
    `post_image` TEXT NOT NULL,
    `short_description` VARCHAR(200) NOT NULL,
    `body` TEXT NOT NULL,
    `user_id` INT UNSIGNED NOT NULL,
    `topic_id` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `fk_user_idx` (`user_id` ASC) VISIBLE,
    CONSTRAINT `fk_user_post_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `{DATABASE}`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_bookmarks = check_table("bookmarks")
create_table_bookmarks = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`bookmarks` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NOT NULL,
    `update_at` DATETIME NULL,
    `user_id` INT UNSIGNED NOT NULL,
    `post_id` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `fk_user_idx` (`user_id` ASC) VISIBLE,
    INDEX `fk_post_idx` (`post_id` ASC) VISIBLE,
    CONSTRAINT `fk_user_bookmars`
    FOREIGN KEY (`user_id`)
    REFERENCES `{DATABASE}`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_bookmarked_post`
    FOREIGN KEY (`post_id`)
    REFERENCES `{DATABASE}`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_claps = check_table("claps")
create_table_claps = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`claps` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NOT NULL,
    `update_at` DATETIME NULL,
    `total_count` INT UNSIGNED NULL,
    `post_id` INT UNSIGNED NOT NULL,
    `user_id` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `fk_posts_idx` (`post_id` ASC) VISIBLE,
    INDEX `fk_user_id_idx` (`user_id` ASC) VISIBLE,
    CONSTRAINT `fk_clapped_post_id`
    FOREIGN KEY (`post_id`)
    REFERENCES `{DATABASE}`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_user_claps_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `{DATABASE}`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_collections = check_table("collections")
create_table_collections = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`collections` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NOT NULL,
    `update_at` DATETIME NULL,
    `title` VARCHAR(200) NOT NULL,
    `collection_image` TEXT NULL,
    `slug` VARCHAR(100) NOT NULL,
    `user_id` INT UNSIGNED NOT NULL ,
    PRIMARY KEY (`id`),
    INDEX `fk_user_idx` (`user_id` ASC) VISIBLE,
    CONSTRAINT `fk_user_collection_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `{DATABASE}`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_collections_posts = check_table("collections_posts")
create_table_collections_posts = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`collections_posts` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NOT NULL,
    `update_at` DATETIME NULL,
    `post_id` INT UNSIGNED NOT NULL,
    `collections_id` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `fk_collections_idx` (`collections_id` ASC) VISIBLE,
    INDEX `fk_post_idx` (`post_id` ASC) VISIBLE,
    CONSTRAINT `fk_collections_id`
    FOREIGN KEY (`collections_id`)
    REFERENCES `{DATABASE}`.`collections` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_post_collections_id`
    FOREIGN KEY (`post_id`)
    REFERENCES `{DATABASE}`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_comments = check_table("comments")
create_table_comments = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`comments` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NOT NULL,
    `update_at` DATETIME NULL,
    `post_id` INT UNSIGNED NULL,
    `body` TEXT(255) NOT NULL,
    `parent_id` INT UNSIGNED NULL,
    `user_id` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `fk_parent_idx` (`parent_id` ASC) VISIBLE,
    INDEX `fk_user_idx` (`user_id` ASC) VISIBLE,
    INDEX `fk_post_id_idx` (`post_id` ASC) VISIBLE,
    CONSTRAINT `fk_user_comment`
    FOREIGN KEY (`user_id`)
    REFERENCES `{DATABASE}`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_parent_comment`
    FOREIGN KEY (`parent_id`)
    REFERENCES `{DATABASE}`.`comments` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_comment_post_id`
    FOREIGN KEY (`post_id`)
    REFERENCES `{DATABASE}`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_posts_tags = check_table("posts_tags")
create_table_posts_tags = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`posts_tags` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NULL,
    `update_at` DATETIME NULL,
    `post_id` INT UNSIGNED NOT NULL,
    `tag_id` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`id`),
    INDEX `fk_post_id_idx` (`post_id` ASC) VISIBLE,
    INDEX `fk_tag_id_idx` (`tag_id` ASC) VISIBLE,
    CONSTRAINT `fk_post_tag_id`
    FOREIGN KEY (`post_id`)
    REFERENCES `{DATABASE}`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_tag_id`
    FOREIGN KEY (`tag_id`)
    REFERENCES `{DATABASE}`.`tags` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_followers = check_table("followers")
create_table_followers = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`followers` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NULL,
    `update_at` DATETIME NULL,
    `following_user_id` INT UNSIGNED NOT NULL,
    `followed_user_id` INT UNSIGNED NOT NULL,
    `unfollowed_date` DATETIME NULL,
    PRIMARY KEY (`id`),
    INDEX `fk_followed_id_idx` (`followed_user_id` ASC) VISIBLE,
    INDEX `fk_following_id_idx` (`following_user_id` ASC) VISIBLE,
    CONSTRAINT `fk_followed_id`
    FOREIGN KEY (`followed_user_id`)
    REFERENCES `{DATABASE}`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_following_id`
    FOREIGN KEY (`following_user_id`)
    REFERENCES `{DATABASE}`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_posts_topics = check_table("posts_topics")
create_table_posts_topics = f"""CREATE TABLE IF NOT EXISTS `{DATABASE}`.`posts_topics` (
    `posts_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `topics_id` INT UNSIGNED NOT NULL,
    PRIMARY KEY (`posts_id`, `topics_id`),
    INDEX `fk_posts_has_topics_topics1_idx` (`topics_id` ASC) VISIBLE,
    INDEX `fk_posts_has_topics_posts1_idx` (`posts_id` ASC) VISIBLE,
    CONSTRAINT `fk_post_id`
    FOREIGN KEY (`posts_id`)
    REFERENCES `{DATABASE}`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_post_topic_id`
    FOREIGN KEY (`topics_id`)
    REFERENCES `{DATABASE}`.`topics` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


statement_list = [
    check_database,
    create_database,
    check_table_users,
    create_table_users,
    check_table_topics,
    create_table_topics,
    check_table_tags,
    create_table_tags,
    check_table_posts,
    create_table_posts,
    check_table_bookmarks,
    create_table_bookmarks,
    check_table_claps,
    create_table_claps,
    check_table_collections,
    create_table_collections,
    check_table_collections_posts,
    create_table_collections_posts,
    check_table_comments,
    create_table_comments,
    check_table_posts_tags,
    create_table_posts_tags,
    check_table_followers,
    create_table_followers,
    check_table_posts_topics,
    create_table_posts_topics,
]

for statement in statement_list:
    my_cursor.execute(statement)
