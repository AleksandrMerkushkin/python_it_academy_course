-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema game_admin
-- -----------------------------------------------------
-- my datebase - create from an ERD

-- -----------------------------------------------------
-- Schema game_admin
--
-- my datebase - create from an ERD
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `game_admin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `game_admin` ;

-- -----------------------------------------------------
-- Table `game_admin`.`Player`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `game_admin`.`Player` ;

CREATE TABLE IF NOT EXISTS `game_admin`.`Player` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `type` INT NOT NULL COMMENT '',
  `nickname` VARCHAR(20) NOT NULL COMMENT '',
  `email` VARCHAR(30) NOT NULL COMMENT '',
  `password` VARCHAR(25) NOT NULL COMMENT '',
  `created` DATETIME NULL COMMENT '',
  `updated` DATETIME NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `nickname_UNIQUE` (`nickname` ASC)  COMMENT '',
  UNIQUE INDEX `email_UNIQUE` (`email` ASC)  COMMENT '',
  UNIQUE INDEX `id_UNIQUE` (`id` ASC)  COMMENT '')
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `game_admin`.`Session`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `game_admin`.`Session` ;

CREATE TABLE IF NOT EXISTS `game_admin`.`Session` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `player_id` INT NOT NULL COMMENT '',
  `start_time` DATETIME NOT NULL COMMENT '',
  `finish_time` DATETIME NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `id_UNIQUE` (`id` ASC)  COMMENT '',
  INDEX `fk_Session_Player1_idx` (`player_id` ASC)  COMMENT '',
  CONSTRAINT `fk_Session_Player1`
    FOREIGN KEY (`player_id`)
    REFERENCES `game_admin`.`Player` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `game_admin`.`Money`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `game_admin`.`Money` ;

CREATE TABLE IF NOT EXISTS `game_admin`.`Money` (
  `id` INT NOT NULL AUTO_INCREMENT COMMENT '',
  `player_id` INT NOT NULL COMMENT '',
  `code` INT NOT NULL COMMENT '',
  `amount` INT NOT NULL COMMENT '',
  `created` DATETIME NULL COMMENT '',
  `updated` DATETIME NULL COMMENT '',
  PRIMARY KEY (`id`)  COMMENT '',
  UNIQUE INDEX `id_UNIQUE` (`id` ASC)  COMMENT '',
  INDEX `fk_Money_Player1_idx` (`player_id` ASC)  COMMENT '',
  CONSTRAINT `fk_Money_Player1`
    FOREIGN KEY (`player_id`)
    REFERENCES `game_admin`.`Player` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
