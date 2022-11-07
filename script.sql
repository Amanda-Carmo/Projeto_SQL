SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema projetoSQL
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema projetoSQL
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `projetoSQL` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `projetoSQL` ;


CREATE TABLE IF NOT EXISTS `projetoSQL`.`Book` (
  `book_name` VARCHAR(80) NOT NULL,
  `genre` VARCHAR(36) NOT NULL,
  `author_name` VARCHAR(50),
  `price` NUMERIC NULL,
  `amount` INT NULL,
  PRIMARY KEY (`book_name`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;



CREATE TABLE IF NOT EXISTS `projetoSQL`.`Order` (
    `order_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    `book_name` VARCHAR(80) NOT NULL,
    `amount` INT NULL,
    `order_date` DATE NULL,
    PRIMARY KEY (`order_id`),
    INDEX `fk_order_book_idx` (`book_name` ASC) VISIBLE,
    CONSTRAINT `fk_order_book`
        FOREIGN KEY (`book_name`)
        REFERENCES `projetoSQL`.`Book` (`book_name`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS `projetoSQL`.`Purchase` (
    `purchase_id` INT NOT NULL AUTO_INCREMENT,
    `user_id` INT NOT NULL,
    `book_name` VARCHAR(80) NOT NULL,
    `amount` INT NULL,
    `purchase_date` DATE NULL,
    PRIMARY KEY (`purchase_id`),
    INDEX `fk_purchase_order_idx` (`order_id` ASC) VISIBLE,
    INDEX `fk_purchase_book_idx` (`book_name` ASC) VISIBLE,
    CONSTRAINT `fk_purchase_book`
        FOREIGN KEY (`book_name`)
        REFERENCES `projetoSQL`.`Book` (`book_name`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
