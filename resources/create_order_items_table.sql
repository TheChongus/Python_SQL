DROP TABLE IF EXISTS `order_items_test`;

CREATE TABLE `order_items_test` (
  `id` mediumint(8) unsigned NOT NULL auto_increment,
  `order_number` mediumint default NULL,
  `item_id` mediumint default NULL,
  `quantity` mediumint default NULL,
  `product` TEXT default NULL,
  `cost` varchar(100) default NULL,
  PRIMARY KEY (`id`)
) AUTO_INCREMENT=1;

INSERT INTO `order_items_test` (`order_number`,`item_id`,`quantity`,`product`,`cost`)
VALUES
  (7,249,2,"Oatmeal Wacky","$65.29"),
  (2,237,2,"Coaster Robot","$44.42"),
  (8,397,1,"Slippers Octopus","$71.66"),
  (5,99,5,"Spaghetti Slippers","$43.38"),
  (2,221,2,"Octopus Oatmeal","$91.04"),
  (1,43,1,"Umbrella Pickle","$45.79"),
  (6,90,9,"Umbrella Pickle","$69.90"),
  (2,211,5,"Watering Can","$69.55"),
  (4,171,3,"Banana Blaster","$31.07"),
  (10,476,5,"Slippers Octopus","$41.10");
INSERT INTO `order_items_test` (`order_number`,`item_id`,`quantity`,`product`,`cost`)
VALUES
  (9,49,7,"Toaster Llama","$60.67"),
  (4,245,1,"Cheese Coaster","$16.12"),
  (6,244,2,"Oatmeal Wacky","$78.50"),
  (6,25,1,"Slippers Octopus","$73.78"),
  (5,453,2,"Watering Can","$62.03"),
  (4,114,4,"Llama Luggage","$29.97"),
  (8,482,8,"Umbrella Pickle","$62.66"),
  (4,101,8,"Llama Luggage","$80.87"),
  (3,342,2,"Oatmeal Wacky","$16.65"),
  (5,469,8,"Luggage Spaghetti","$62.16");
INSERT INTO `order_items_test` (`order_number`,`item_id`,`quantity`,`product`,`cost`)
VALUES
  (5,377,2,"Pillow Disco","$31.41"),
  (6,56,8,"Pickle Pillow","$81.24"),
  (6,439,4,"Watering Can","$38.33"),
  (9,20,8,"Spaghetti Slippers","$54.16"),
  (1,240,4,"Luggage Spaghetti","$58.26"),
  (2,42,9,"Disco Toaster","$43.31"),
  (4,224,7,"Slippers Octopus","$61.80"),
  (9,60,1,"Slippers Octopus","$7.02"),
  (8,34,10,"Pickle Pillow","$54.59"),
  (5,222,3,"Blaster Cheese","$10.39");
INSERT INTO `order_items_test` (`order_number`,`item_id`,`quantity`,`product`,`cost`)
VALUES
  (3,458,10,"Blaster Cheese","$27.97"),
  (6,389,4,"Cheese Coaster","$75.05"),
  (6,407,2,"Watering Can","$4.58"),
  (0,157,9,"Luggage Spaghetti","$39.46"),
  (1,262,0,"Luggage Spaghetti","$27.32"),
  (5,52,7,"Luggage Spaghetti","$86.09"),
  (2,75,3,"Pillow Disco","$18.45"),
  (2,301,3,"Toaster Llama","$41.93"),
  (9,307,0,"Watering Can","$21.33"),
  (1,117,9,"Disco Toaster","$25.71");
INSERT INTO `order_items_test` (`order_number`,`item_id`,`quantity`,`product`,`cost`)
VALUES
  (1,486,6,"Robot Ravioli","$44.77"),
  (1,435,5,"Oatmeal Wacky","$67.26"),
  (7,490,3,"Watering Can","$49.83"),
  (4,249,5,"Wacky Watering","$54.40"),
  (1,303,2,"Robot Ravioli","$96.85"),
  (2,224,5,"Disco Toaster","$99.93"),
  (1,185,0,"Disco Toaster","$47.89"),
  (9,47,6,"Banana Blaster","$56.82"),
  (5,107,10,"Llama Luggage","$50.64"),
  (5,222,7,"Disco Toaster","$29.18");
INSERT INTO `order_items_test` (`order_number`,`item_id`,`quantity`,`product`,`cost`)
VALUES
  (2,102,5,"Pillow Disco","$38.93"),
  (9,137,4,"Wacky Watering","$8.65"),
  (0,355,1,"Unicorn Umbrella","$5.28"),
  (6,457,1,"Disco Toaster","$36.87"),
  (9,445,0,"Spaghetti Slippers","$79.84"),
  (9,178,2,"Pickle Pillow","$28.20"),
  (2,166,9,"Ravioli Unicorn","$11.69"),
  (2,16,5,"Umbrella Pickle","$67.27"),
  (8,338,1,"Umbrella Pickle","$63.33"),
  (2,63,2,"Slippers Octopus","$36.62");
INSERT INTO `order_items_test` (`order_number`,`item_id`,`quantity`,`product`,`cost`)
VALUES
  (10,91,5,"Disco Toaster","$96.14"),
  (5,162,5,"Slippers Octopus","$27.41"),
  (6,21,2,"Pickle Pillow","$52.77"),
  (5,132,7,"Unicorn Umbrella","$26.18"),
  (4,212,4,"Umbrella Pickle","$49.57"),
  (9,483,0,"Toaster Llama","$21.92"),
  (4,176,3,"Blaster Cheese","$83.32"),
  (5,125,3,"Oatmeal Wacky","$67.85"),
  (2,386,10,"Octopus Oatmeal","$3.44"),
  (4,69,3,"Umbrella Pickle","$71.33");
INSERT INTO `order_items_test` (`order_number`,`item_id`,`quantity`,`product`,`cost`)
VALUES
  (5,280,4,"Oatmeal Wacky","$17.26"),
  (7,358,6,"Wacky Watering","$60.45"),
  (6,61,1,"Pickle Pillow","$7.04"),
  (3,110,8,"Slippers Octopus","$47.58"),
  (8,17,4,"Slippers Octopus","$24.30"),
  (5,352,0,"Coaster Robot","$74.31"),
  (0,94,4,"Cheese Coaster","$1.23"),
  (9,403,6,"Octopus Oatmeal","$17.10"),
  (0,408,1,"Llama Luggage","$99.72"),
  (3,119,9,"Umbrella Pickle","$43.83");
INSERT INTO `order_items_test` (`order_number`,`item_id`,`quantity`,`product`,`cost`)
VALUES
  (4,416,5,"Robot Ravioli","$81.90"),
  (1,353,2,"Luggage Spaghetti","$93.53"),
  (1,278,8,"Robot Ravioli","$98.59"),
  (4,200,3,"Cheese Coaster","$12.58"),
  (1,408,10,"Wacky Watering","$99.75"),
  (5,386,8,"Umbrella Pickle","$7.96"),
  (9,125,4,"Disco Toaster","$15.70"),
  (3,360,9,"Octopus Oatmeal","$52.29"),
  (4,31,10,"Cheese Coaster","$6.90"),
  (2,488,6,"Spaghetti Slippers","$85.30");
INSERT INTO `order_items_test` (`order_number`,`item_id`,`quantity`,`product`,`cost`)
VALUES
  (4,51,10,"Robot Ravioli","$79.79"),
  (4,414,6,"Disco Toaster","$81.55"),
  (4,484,6,"Pickle Pillow","$3.73"),
  (9,180,7,"Disco Toaster","$74.89"),
  (8,127,1,"Umbrella Pickle","$86.38"),
  (4,417,8,"Coaster Robot","$72.15"),
  (2,203,7,"Ravioli Unicorn","$65.25"),
  (7,390,9,"Llama Luggage","$55.79"),
  (4,344,5,"Toaster Llama","$64.35"),
  (6,165,7,"Spaghetti Slippers","$81.55");
