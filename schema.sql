CREATE TABLE users (
  `id` int not null auto_increment PRIMARY KEY,
  `name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `profile_pic` TEXT NOT NULL,
  `created_on` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_deleted` tinyint(1) DEFAULT 0
);
