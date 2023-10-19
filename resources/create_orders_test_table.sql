-- Drop the 'orders' table if it already exists
DROP TABLE IF EXISTS `orders_test_table`;

-- Create the 'orders_test_table' table
CREATE TABLE `orders_test_table` (
  `order_id` mediumint(8) unsigned NOT NULL auto_increment,
  `user_id` mediumint(8) unsigned NOT NULL,
  `order_date` DATE,
  `total_amount` DECIMAL(10, 2),
  PRIMARY KEY (`order_id`),
  FOREIGN KEY (`user_id`) REFERENCES `users_test_table`(`id`)
) AUTO_INCREMENT=1;

-- Insert sample orders for users with unique `order_id`
INSERT INTO `orders_test_table` (`user_id`, `order_id`, `order_date`, `total_amount`) VALUES
(1, 1, '2023-10-17', 50.00),
(2, 2, '2023-10-18', 35.00),
(3, 3, '2023-10-19', 60.00),
(4, 4, '2023-10-20', 45.00),
(5, 5, '2023-10-21', 90.00),
(6, 6, '2023-10-22', 70.00),
(7, 7, '2023-10-23', 40.00),
(8, 8, '2023-10-24', 75.00),
(9, 9, '2023-10-25', 110.00),
(10, 10, '2023-10-26', 48.00),
(1, 11, '2023-10-27', 65.00),
(2, 12, '2023-10-28', 38.00),
(3, 13, '2023-10-29', 50.00),
(4, 14, '2023-10-30', 55.00),
(5, 15, '2023-10-31', 70.00),
(6, 16, '2023-11-01', 40.00),
(7, 17, '2023-11-02', 85.00),
(8, 18, '2023-11-03', 63.00),
(9, 19, '2023-11-04', 45.00),
(10, 20, '2023-11-05', 70.00);