-- -----------------------------------------------------
-- Schema medium_clone
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `medium_clone` ;

-- -----------------------------------------------------
-- Schema medium_clone
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `medium_clone` ;
USE `medium_clone` ;


-- -----------------------------------------------------
-- Table `medium_clone`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`user` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`users` (
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
    PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `medium_clone`.`topics`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`topics` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`topics` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NOT NULL,
    `update_at` DATETIME NULL,
    `name` VARCHAR(15) NOT NULL,
    `description` VARCHAR(45) NOT NULL,
    `topic_picture` TEXT NOT NULL,
    `slug` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `medium_clone`.`tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`tags` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`tags` (
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `create_at` DATETIME NOT NULL,
    `update_at` DATETIME NULL,
    `name` VARCHAR(30) NOT NULL,
    `slug` VARCHAR(100) NOT NULL,
    PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `medium_clone`.`posts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`posts` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`posts` (
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
    REFERENCES `medium_clone`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `medium_clone`.`bookmarks`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`bookmarks` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`bookmarks` (
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
    REFERENCES `medium_clone`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_bookmarked_post`
    FOREIGN KEY (`post_id`)
    REFERENCES `medium_clone`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `medium_clone`.`claps`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`claps` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`claps` (
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
    REFERENCES `medium_clone`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_user_claps_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `medium_clone`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `medium_clone`.`collections`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`collections` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`collections` (
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
    REFERENCES `medium_clone`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `medium_clone`.`collections_posts`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`collections_posts` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`collections_posts` (
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
    REFERENCES `medium_clone`.`collections` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_post_collections_id`
    FOREIGN KEY (`post_id`)
    REFERENCES `medium_clone`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `medium_clone`.`comments`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`comments` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`comments` (
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
    REFERENCES `medium_clone`.`users` (`id`)
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
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `medium_clone`.`posts_tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`posts_tags` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`posts_tags` (
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
    REFERENCES `medium_clone`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_tag_id`
    FOREIGN KEY (`tag_id`)
    REFERENCES `medium_clone`.`tags` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `medium_clone`.`followers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`followers` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`followers` (
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
    REFERENCES `medium_clone`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
    CONSTRAINT `fk_following_id`
    FOREIGN KEY (`following_user_id`)
    REFERENCES `medium_clone`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table `medium_clone`.`posts_topics`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `medium_clone`.`posts_topics` ;

CREATE TABLE IF NOT EXISTS `medium_clone`.`posts_topics` (
    `posts_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `topics_id` INT UNSIGNED NOT NULL,
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
    ON UPDATE NO ACTION);
