CREATE TABLE IF NOT EXISTS `P5`.`Registred_products` (
  `name` VARCHAR(90) NULL,
  `id` INT NOT NULL,
  `Categories_id` INT NOT NULL,
  `description` MEDIUMTEXT NULL,
  `shop` VARCHAR(90) NULL,
  `url` VARCHAR(90) NOT NULL,
  `substitut_url` VARCHAR(90) NULL,
  `nutrition_grade` VARCHAR(1) NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_Registred_products_Categories1`
    FOREIGN KEY (`Categories_id`)
    REFERENCES `P5`.`Categories` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;