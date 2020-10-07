#This script is here only to generate the database and tables we will be working with.
# just add your credentials to your installation of mysql and run it on the terminal.
# on a side  note if you ever want to restart the data base from 0 just run again this script

import mysql.connector as mysql

# insert your respective MYSQL data here
HOST = "localhost"
DATABASE = "medium_clone" #name is up to you but this name is simplier and understable
USER = "YOUR USER" #here goes your username to connecto to MYSQL
PASSWORD = "YOUR PASSWORD" #here goes your password


# connect to mysql
db_connection = mysql.connect(host=HOST, user=USER, password=PASSWORD)


# cursor mysql connection
mycursor = db_connection.cursor()


# database statements
check_database = "DROP DATABASE IF EXISTS `medium_clone`"
create_database = "CREATE DATABASE IF NOT EXISTS `medium_clone`"

check_table_user = "DROP TABLE IF EXISTS `medium_clone`.`user`"
create_table_user = """CREATE TABLE IF NOT EXISTS `medium_clone`.`user` (
	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`create_at` DATETIME NOT NULL,
	`update_at` DATETIME NULL,
	`username` VARCHAR(20) NOT NULL,
	`password` VARCHAR(15) NOT NULL,
	`email` VARCHAR(255) NOT NULL,
	`first_name` VARCHAR(45) NOT NULL,
	`last_name` VARCHAR(45) NOT NULL,
	`bio` VARCHAR(80) NULL,
	`user_picture` TEXT NULL,
	`token` VARCHAR(25) NULL,
	`toke_at` DATETIME NULL,
	`slug` VARCHAR(45) NOT NULL,
	PRIMARY KEY (`id`));"""


check_table_topics = "DROP TABLE IF EXISTS `medium_clone`.`topics`"
create_table_topics = """CREATE TABLE IF NOT EXISTS `medium_clone`.`topics` (
	`id` INT  UNSIGNED NOT NULL AUTO_INCREMENT,
	`create_at` DATETIME NOT NULL,
	`update_at` DATETIME NULL,
	`name` VARCHAR(15) NOT NULL,
	`description` VARCHAR(45) NOT NULL,
	`topic_picture` TEXT NOT NULL,
	`slug` VARCHAR(45) NOT NULL,
	PRIMARY KEY (`id`));"""


check_table_tags = "DROP TABLE IF EXISTS `medium_clone`.`tags`"
create_table_tags = """CREATE TABLE IF NOT EXISTS `medium_clone`.`tags` (
	`id` INT  UNSIGNED NOT NULL AUTO_INCREMENT,
	`create_at` DATETIME NOT NULL,
	`update_at` DATETIME NULL,
	`name` VARCHAR(30) NOT NULL,
	`slug` VARCHAR(100) NOT NULL,
	PRIMARY KEY (`id`));"""


check_table_posts = "DROP TABLE IF EXISTS `medium_clone`.`posts`"
create_table_posts = """CREATE TABLE IF NOT EXISTS `medium_clone`.`posts` (
	`id` INT  UNSIGNED NOT NULL,
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
    REFERENCES `medium_clone`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_bookmarks = "DROP TABLE IF EXISTS `medium_clone`.`bookmarks`"
create_table_bookmarks = """CREATE TABLE IF NOT EXISTS `medium_clone`.`bookmarks` (
	`id` INT  UNSIGNED NOT NULL AUTO_INCREMENT,
	`create_at` DATETIME NOT NULL,
	`update_at` DATETIME NULL,
	`user_id` INT UNSIGNED NOT NULL,
	`post_id` INT UNSIGNED NOT NULL,
	PRIMARY KEY (`id`),
	INDEX `fk_user_idx` (`user_id` ASC) VISIBLE,
	INDEX `fk_post_idx` (`post_id` ASC) VISIBLE,
	CONSTRAINT `fk_user_bookmars`
    FOREIGN KEY (`user_id`)
    REFERENCES `medium_clone`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	CONSTRAINT `fk_bookmarked_post`
    FOREIGN KEY (`post_id`)
    REFERENCES `medium_clone`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_claps = "DROP TABLE IF EXISTS `medium_clone`.`claps`"
create_table_claps = """CREATE TABLE IF NOT EXISTS `medium_clone`.`claps` (
	`id` INT  UNSIGNED NOT NULL AUTO_INCREMENT,
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
    REFERENCES `medium_clone`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	CONSTRAINT `fk_user_claps_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `medium_clone`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_collections = "DROP TABLE IF EXISTS `medium_clone`.`collections`"
create_table_collections = """CREATE TABLE IF NOT EXISTS `medium_clone`.`collections` (
	`id` INT  UNSIGNED NOT NULL AUTO_INCREMENT,
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
    REFERENCES `medium_clone`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_collections_posts = (
    "DROP TABLE IF EXISTS `medium_clone`.`collentions_posts`"
)
create_table_collections_posts = """CREATE TABLE IF NOT EXISTS `medium_clone`.`collections_posts` (
	`id` INT  UNSIGNED NOT NULL AUTO_INCREMENT,
	`create_at` DATETIME NOT NULL,
	`update_at` DATETIME NULL,
	`post_id` INT UNSIGNED NOT NULL,
	`collections_id` INT UNSIGNED NOT NULL,
	PRIMARY KEY (`id`),
	INDEX `fk_collections_idx` (`collections_id` ASC) VISIBLE,
	INDEX `fk_post_idx` (`post_id` ASC) VISIBLE,
	CONSTRAINT `fk_collections_id`
    FOREIGN KEY (`collections_id`)
    REFERENCES `medium_clone`.`collections` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	CONSTRAINT `fk_post_collections_id`
    FOREIGN KEY (`post_id`)
    REFERENCES `medium_clone`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_comments = "DROP TABLE IF EXISTS `medium_clone`.`comments`"
create_table_comments = """CREATE TABLE IF NOT EXISTS `medium_clone`.`comments` (
	`id` INT  UNSIGNED NOT NULL AUTO_INCREMENT,
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
    REFERENCES `medium_clone`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	CONSTRAINT `fk_parent_comment`
    FOREIGN KEY (`parent_id`)
    REFERENCES `medium_clone`.`comments` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION,
	CONSTRAINT `fk_comment_post_id`
    FOREIGN KEY (`post_id`)
    REFERENCES `medium_clone`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_posts_tags = "DROP TABLE IF EXISTS `medium_clone`.`posts_tags`"
create_table_posts_tags = """CREATE TABLE IF NOT EXISTS `medium_clone`.`followers` (
	`id` INT  UNSIGNED NOT NULL AUTO_INCREMENT,
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
    REFERENCES `medium_clone`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	CONSTRAINT `fk_following_id`
    FOREIGN KEY (`following_user_id`)
    REFERENCES `medium_clone`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);;"""


check_table_followers = "DROP TABLE IF EXISTS `medium_clone`.`followers` "
create_table_followers = """CREATE TABLE IF NOT EXISTS `medium_clone`.`followers` (
	`id` INT  UNSIGNED NOT NULL AUTO_INCREMENT,
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
    REFERENCES `medium_clone`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	CONSTRAINT `fk_following_id`
    FOREIGN KEY (`following_user_id`)
    REFERENCES `medium_clone`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


check_table_posts_topics = "DROP TABLE IF EXISTS `medium_clone`.`posts_topics` "
create_table_posts_topics = """CREATE TABLE IF NOT EXISTS `medium_clone`.`posts_topics` (
	`posts_id` INT  UNSIGNED NOT NULL AUTO_INCREMENT,
	`topics_id` INT  UNSIGNED NOT NULL,
	PRIMARY KEY (`posts_id`, `topics_id`),
	INDEX `fk_posts_has_topics_topics1_idx` (`topics_id` ASC) VISIBLE,
	INDEX `fk_posts_has_topics_posts1_idx` (`posts_id` ASC) VISIBLE,
	CONSTRAINT `fk_post_id`
    FOREIGN KEY (`posts_id`)
    REFERENCES `medium_clone`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
	CONSTRAINT `fk_post_topic_id`
    FOREIGN KEY (`topics_id`)
    REFERENCES `medium_clone`.`topics` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);"""


statements_lists = [
    check_database,
    create_database,
    check_table_user,
    create_table_user,
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

for statements in statements_lists:
    mycursor.execute(statements)
