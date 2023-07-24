CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
	  FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
	  FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` NUMERIC(4,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL, 
    `price` NUMERIC(5,2) NOT NULL
);




INSERT INTO Metals VALUES (null, 'Gold', 1500.00);
INSERT INTO Metals VALUES (null, 'Silver', 800.00);
INSERT INTO Metals VALUES (null, 'Platinum', 2500.00);
INSERT INTO Metals VALUES (null, 'Rose Gold', 1800.00);


INSERT INTO Orders VALUES (null, 1, 2, 3);
INSERT INTO Orders VALUES (null, 2, 1, 4);
INSERT INTO Orders VALUES (null, 3, 4, 2);
INSERT INTO Orders VALUES (null, 4, 3, 1);
INSERT INTO Orders VALUES (null, 3, 2, 1);
INSERT INTO Orders VALUES (null, 2, 1, 3);


INSERT INTO Sizes VALUES (null, 1.50, 1200.00);
INSERT INTO Sizes VALUES (null, 2.00, 1500.00);
INSERT INTO Sizes VALUES (null, 1.25, 1000.00);
INSERT INTO Sizes VALUES (null, 1.75, 1300.00);


INSERT INTO Styles VALUES (null, 'Round', 1000.00);
INSERT INTO Styles VALUES (null, 'Princess', 900.00);
INSERT INTO Styles VALUES (null, 'Oval', 950.00);
INSERT INTO Styles VALUES (null, 'Emerald', 1100.00);

ALTER TABLE Orders ADD COLUMN timestamp INTEGER;
