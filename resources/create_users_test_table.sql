DROP TABLE IF EXISTS `users_test_table`;

CREATE TABLE `user_test_table` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `first_name` varchar(255) default NULL,
  `last_name` varchar(255) default NULL,
  `phone` varchar(100) default NULL,
  `email` varchar(255) default NULL,
  `address` varchar(255) default NULL,
  `postalZip` varchar(10) default NULL,
  `country` varchar(100) default NULL,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

INSERT INTO `users_test_table` (`first_name`,`last_name`,`phone`,`email`,`address`,`postalZip`,`country`)
VALUES
  ("Nora","Mckay","1-744-546-8157","aliquam.nisl.nulla@aol.ca","P.O. Box 792, 4780 Velit. Road","47703","United States"),
  ("Charity","Mueller","1-424-743-5950","urna@icloud.ca","194-5091 Et Avenue","36932","United States"),
  ("McKenzie","Lang","1-622-232-6692","auctor.ullamcorper@yahoo.ca","Ap #315-7134 Penatibus Ave","38275","United States"),
  ("Sara","Fleming","1-278-761-9896","felis@icloud.ca","501-6215 Quis Av.","14764","United States"),
  ("Evelyn","Martinez","1-448-450-5690","sagittis.placerat@google.couk","3934 Risus Rd.","99912","United States"),
  ("Ayanna","Mccoy","1-722-789-3430","tristique@protonmail.edu","Ap #823-4676 Amet Ave","72852","United States"),
  ("Asher","Hoffman","1-113-847-3878","odio@hotmail.ca","9717 Ornare Rd.","94456","United States"),
  ("Mason","Harrison","1-649-601-7355","nec.urna@google.net","P.O. Box 859, 6021 Eget Ave","87614","United States"),
  ("Gregory","Horton","1-994-265-5164","ut.nisi@yahoo.net","Ap #982-1931 Quam. Av.","29348","United States"),
  ("Rinah","Hoffman","1-257-834-1514","sit.amet@aol.edu","723-4839 Convallis Avenue","39107","United States");
INSERT INTO `users_test_table` (`first_name`,`last_name`,`phone`,`email`,`address`,`postalZip`,`country`)
VALUES
  ("Damon","Porter","1-245-622-0391","scelerisque@aol.edu","Ap #332-8663 Sed Avenue","36488","United States"),
  ("Kieran","Santos","1-901-318-7642","at.fringilla@hotmail.couk","P.O. Box 188, 1914 Bibendum Avenue","74163","United States"),
  ("Thomas","Owens","1-893-715-2398","parturient.montes@icloud.couk","690-3936 Nibh Avenue","35822","United States"),
  ("Keiko","Hale","1-414-743-5789","proin.vel@outlook.couk","Ap #378-3570 Porttitor Avenue","87822","United States"),
  ("Valentine","Lawson","1-611-684-4416","commodo.at@outlook.org","258-5320 Gravida. Av.","13685","United States"),
  ("Sawyer","Bennett","1-832-442-7287","integer.in@protonmail.com","291-2101 Ac Ave","81186","United States"),
  ("Katelyn","Summers","1-405-376-6313","tincidunt.aliquam@google.com","Ap #848-2417 In, Rd.","62174","United States"),
  ("Giacomo","Dyer","1-277-578-6417","ultrices.mauris.ipsum@hotmail.ca","432-9668 Auctor Street","71571","United States"),
  ("Cassandra","Hendrix","1-685-258-9524","congue.a.aliquet@aol.com","Ap #653-6352 Facilisis, St.","88771","United States"),
  ("Castor","Porter","1-514-638-1043","tempus@outlook.edu","Ap #184-9906 Pharetra Av.","80139","United States");
