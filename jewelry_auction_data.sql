-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: jewelry_auction
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add auction',7,'add_auction'),(26,'Can change auction',7,'change_auction'),(27,'Can delete auction',7,'delete_auction'),(28,'Can view auction',7,'view_auction'),(29,'Can add jewelry',8,'add_jewelry'),(30,'Can change jewelry',8,'change_jewelry'),(31,'Can delete jewelry',8,'delete_jewelry'),(32,'Can view jewelry',8,'view_jewelry'),(33,'Can add user',9,'add_user'),(34,'Can change user',9,'change_user'),(35,'Can delete user',9,'delete_user'),(36,'Can view user',9,'view_user'),(37,'Can add transaction',10,'add_transaction'),(38,'Can change transaction',10,'change_transaction'),(39,'Can delete transaction',10,'delete_transaction'),(40,'Can view transaction',10,'view_transaction'),(41,'Can add request',11,'add_request'),(42,'Can change request',11,'change_request'),(43,'Can delete request',11,'delete_request'),(44,'Can view request',11,'view_request'),(45,'Can add blog',12,'add_blog'),(46,'Can change blog',12,'change_blog'),(47,'Can delete blog',12,'delete_blog'),(48,'Can view blog',12,'view_blog'),(49,'Can add bid',13,'add_bid'),(50,'Can change bid',13,'change_bid'),(51,'Can delete bid',13,'delete_bid'),(52,'Can view bid',13,'view_bid');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES (1,'pbkdf2_sha256$600000$rioo5Gum3FVpxEuXFl6x01$WSYgRrjZeMUHzl4y4GHQyJu2PfGORRVtmBFC3OhcUTw=','2024-12-19 17:08:01.373011',1,'nhom9','','','nhom9@gmail.com',1,1,'2024-12-19 15:55:23.057541'),(2,'pbkdf2_sha256$600000$uBfsKva8eRAmyDa0lRITvh$i9jB/nHBtmdzC5iVh0xk2Ti/POvbminAv8GQFmXW/MM=','2024-12-19 16:46:02.403881',1,'phh','','','phamhiangg2710@gmail.com',1,1,'2024-12-19 15:55:57.153183');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_auction`
--

DROP TABLE IF EXISTS `core_auction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_auction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `jewelry_id` bigint DEFAULT NULL,
  `manager_id` bigint DEFAULT NULL,
  `staff_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_auction_jewelry_id_ca22daea_fk_core_jewelry_id` (`jewelry_id`),
  KEY `core_auction_manager_id_7c0a9bd0_fk_core_user_id` (`manager_id`),
  KEY `core_auction_staff_id_aace6e43_fk_core_user_id` (`staff_id`),
  CONSTRAINT `core_auction_jewelry_id_ca22daea_fk_core_jewelry_id` FOREIGN KEY (`jewelry_id`) REFERENCES `core_jewelry` (`id`),
  CONSTRAINT `core_auction_manager_id_7c0a9bd0_fk_core_user_id` FOREIGN KEY (`manager_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `core_auction_staff_id_aace6e43_fk_core_user_id` FOREIGN KEY (`staff_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_auction`
--

LOCK TABLES `core_auction` WRITE;
/*!40000 ALTER TABLE `core_auction` DISABLE KEYS */;
INSERT INTO `core_auction` (`id`, `start_time`, `end_time`, `status`, `jewelry_id`, `manager_id`, `staff_id`) VALUES (1,'2024-12-19 16:31:02.688649','2024-12-26 16:31:02.688653','open',1,1,NULL);
/*!40000 ALTER TABLE `core_auction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_bid`
--

DROP TABLE IF EXISTS `core_bid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_bid` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `auction_id` bigint NOT NULL,
  `bidder_id` bigint NOT NULL,
  `jewelry_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_bid_auction_id_7ec39da5_fk_core_auction_id` (`auction_id`),
  KEY `core_bid_bidder_id_e4ca1418_fk_core_user_id` (`bidder_id`),
  KEY `core_bid_jewelry_id_9e2df97a_fk_core_jewelry_id` (`jewelry_id`),
  CONSTRAINT `core_bid_auction_id_7ec39da5_fk_core_auction_id` FOREIGN KEY (`auction_id`) REFERENCES `core_auction` (`id`),
  CONSTRAINT `core_bid_bidder_id_e4ca1418_fk_core_user_id` FOREIGN KEY (`bidder_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `core_bid_jewelry_id_9e2df97a_fk_core_jewelry_id` FOREIGN KEY (`jewelry_id`) REFERENCES `core_jewelry` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_bid`
--

LOCK TABLES `core_bid` WRITE;
/*!40000 ALTER TABLE `core_bid` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_bid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_blog`
--

DROP TABLE IF EXISTS `core_blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_blog` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` longtext NOT NULL,
  `publication_date` datetime(6) NOT NULL,
  `author_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_blog_author_id_1575e3e5_fk_core_user_id` (`author_id`),
  CONSTRAINT `core_blog_author_id_1575e3e5_fk_core_user_id` FOREIGN KEY (`author_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_blog`
--

LOCK TABLES `core_blog` WRITE;
/*!40000 ALTER TABLE `core_blog` DISABLE KEYS */;
INSERT INTO `core_blog` (`id`, `title`, `content`, `publication_date`, `author_id`) VALUES (1,'Blog Post 1','Nội dung blog post 1','2024-12-19 16:31:02.692350',1),(2,'Blog Post 2','Nội dung blog post 2','2024-12-19 16:31:02.695870',1);
/*!40000 ALTER TABLE `core_blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_jewelry`
--

DROP TABLE IF EXISTS `core_jewelry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_jewelry` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `initial_price` decimal(10,2) DEFAULT NULL,
  `preliminary_price` decimal(10,2) DEFAULT NULL,
  `final_price` decimal(10,2) DEFAULT NULL,
  `image_1` varchar(100) DEFAULT NULL,
  `image_2` varchar(100) DEFAULT NULL,
  `image_3` varchar(100) DEFAULT NULL,
  `status` varchar(20) NOT NULL,
  `seller_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_jewelry_seller_id_c1c7d54b_fk_core_user_id` (`seller_id`),
  CONSTRAINT `core_jewelry_seller_id_c1c7d54b_fk_core_user_id` FOREIGN KEY (`seller_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_jewelry`
--

LOCK TABLES `core_jewelry` WRITE;
/*!40000 ALTER TABLE `core_jewelry` DISABLE KEYS */;
INSERT INTO `core_jewelry` (`id`, `name`, `description`, `initial_price`, `preliminary_price`, `final_price`, `image_1`, `image_2`, `image_3`, `status`, `seller_id`) VALUES (1,'Nhẫn kim cương','Nhẫn kim cương tuyệt đẹp',1000.00,NULL,NULL,'jewelry_images/ring.jpg','','','approved',2);
/*!40000 ALTER TABLE `core_jewelry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_request`
--

DROP TABLE IF EXISTS `core_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_request` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` varchar(30) NOT NULL,
  `preliminary_price` decimal(10,2) DEFAULT NULL,
  `final_price` decimal(10,2) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `jewelry_id` bigint NOT NULL,
  `seller_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_request_jewelry_id_8d39601a_fk_core_jewelry_id` (`jewelry_id`),
  KEY `core_request_seller_id_f349cde9_fk_core_user_id` (`seller_id`),
  CONSTRAINT `core_request_jewelry_id_8d39601a_fk_core_jewelry_id` FOREIGN KEY (`jewelry_id`) REFERENCES `core_jewelry` (`id`),
  CONSTRAINT `core_request_seller_id_f349cde9_fk_core_user_id` FOREIGN KEY (`seller_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_request`
--

LOCK TABLES `core_request` WRITE;
/*!40000 ALTER TABLE `core_request` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_transaction`
--

DROP TABLE IF EXISTS `core_transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_transaction` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` decimal(10,2) NOT NULL,
  `fee` decimal(10,2) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `auction_id` bigint DEFAULT NULL,
  `buyer_id` bigint DEFAULT NULL,
  `seller_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auction_id` (`auction_id`),
  KEY `core_transaction_buyer_id_3b9aa6d7_fk_core_user_id` (`buyer_id`),
  KEY `core_transaction_seller_id_a82e96a9_fk_core_user_id` (`seller_id`),
  CONSTRAINT `core_transaction_auction_id_ef0247b2_fk_core_auction_id` FOREIGN KEY (`auction_id`) REFERENCES `core_auction` (`id`),
  CONSTRAINT `core_transaction_buyer_id_3b9aa6d7_fk_core_user_id` FOREIGN KEY (`buyer_id`) REFERENCES `core_user` (`id`),
  CONSTRAINT `core_transaction_seller_id_a82e96a9_fk_core_user_id` FOREIGN KEY (`seller_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_transaction`
--

LOCK TABLES `core_transaction` WRITE;
/*!40000 ALTER TABLE `core_transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user`
--

DROP TABLE IF EXISTS `core_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `role` varchar(10) NOT NULL,
  `email` varchar(254) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `registration_date` datetime(6) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `jcoin_balance` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user`
--

LOCK TABLES `core_user` WRITE;
/*!40000 ALTER TABLE `core_user` DISABLE KEYS */;
INSERT INTO `core_user` (`id`, `password`, `is_superuser`, `username`, `is_staff`, `is_active`, `date_joined`, `role`, `email`, `first_name`, `last_name`, `registration_date`, `last_login`, `profile_picture`, `jcoin_balance`) VALUES (1,'pbkdf2_sha256$600000$27lOGrg8f9LvqQxeJ4jGzA$Kcoj7Kq8Ma6Jgh3ZPBqvkOYgRTIuGnWDAHdAMOel7uQ=',1,'nhom9',1,1,'2024-12-19 16:31:02.092003','guest','nhom9@example.com','','','2024-12-19 16:31:02.092010',NULL,'',0.00),(2,'pbkdf2_sha256$600000$gaoP69Ldyb54FPctpjLlNm$uEH3oxpPfQYd/RXAjE3o/paoxWMxN9Wd++0YhjKo+jE=',0,'testuser',0,1,'2024-12-19 16:31:02.287626','member','test@example.com','','','2024-12-19 16:31:02.287630',NULL,'',0.00),(3,'pbkdf2_sha256$600000$Anj2YTZKLyd7qnG0hOEihc$kMnNxxXUmPbsRzn/Z/ymOc95iv8S6h8kVJIVPFxZv5M=',0,'staffuser',0,1,'2024-12-19 16:31:02.481678','staff','staff@example.com','','','2024-12-19 16:31:02.481683',NULL,'',0.00),(4,'pbkdf2_sha256$600000$e6g8lFVFgTfUx0FnWQVGpj$FDGp8wv1jEKRbHQH+jME6o93Gh/FpvLZ1+3kOlq/ErM=',0,'SvHieu123',0,1,'2024-12-19 17:06:54.508000','member','SvHieu@gmail.com','','','2024-12-19 17:06:54.508011','2024-12-19 17:06:54.882919','',0.00);
/*!40000 ALTER TABLE `core_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user_groups`
--

DROP TABLE IF EXISTS `core_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_groups_user_id_group_id_c82fcad1_uniq` (`user_id`,`group_id`),
  KEY `core_user_groups_group_id_fe8c697f_fk_auth_group_id` (`group_id`),
  CONSTRAINT `core_user_groups_group_id_fe8c697f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `core_user_groups_user_id_70b4d9b8_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_groups`
--

LOCK TABLES `core_user_groups` WRITE;
/*!40000 ALTER TABLE `core_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user_user_permissions`
--

DROP TABLE IF EXISTS `core_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `core_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `core_user_user_permissions_user_id_permission_id_73ea0daa_uniq` (`user_id`,`permission_id`),
  KEY `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` (`permission_id`),
  CONSTRAINT `core_user_user_permi_permission_id_35ccf601_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `core_user_user_permissions_user_id_085123d3_fk_core_user_id` FOREIGN KEY (`user_id`) REFERENCES `core_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_user_permissions`
--

LOCK TABLES `core_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `core_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'core','auction'),(13,'core','bid'),(12,'core','blog'),(8,'core','jewelry'),(11,'core','request'),(10,'core','transaction'),(9,'core','user'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES (1,'contenttypes','0001_initial','2024-12-19 15:54:44.763147'),(2,'auth','0001_initial','2024-12-19 15:54:45.313803'),(3,'admin','0001_initial','2024-12-19 15:54:45.441038'),(4,'admin','0002_logentry_remove_auto_add','2024-12-19 15:54:45.448174'),(5,'admin','0003_logentry_add_action_flag_choices','2024-12-19 15:54:45.456196'),(6,'contenttypes','0002_remove_content_type_name','2024-12-19 15:54:45.525470'),(7,'auth','0002_alter_permission_name_max_length','2024-12-19 15:54:45.582676'),(8,'auth','0003_alter_user_email_max_length','2024-12-19 15:54:45.601166'),(9,'auth','0004_alter_user_username_opts','2024-12-19 15:54:45.609545'),(10,'auth','0005_alter_user_last_login_null','2024-12-19 15:54:45.674905'),(11,'auth','0006_require_contenttypes_0002','2024-12-19 15:54:45.679759'),(12,'auth','0007_alter_validators_add_error_messages','2024-12-19 15:54:45.686229'),(13,'auth','0008_alter_user_username_max_length','2024-12-19 15:54:45.760410'),(14,'auth','0009_alter_user_last_name_max_length','2024-12-19 15:54:45.815769'),(15,'auth','0010_alter_group_name_max_length','2024-12-19 15:54:45.832146'),(16,'auth','0011_update_proxy_permissions','2024-12-19 15:54:45.840978'),(17,'auth','0012_alter_user_first_name_max_length','2024-12-19 15:54:45.898697'),(18,'core','0001_initial','2024-12-19 15:54:47.037839'),(19,'sessions','0001_initial','2024-12-19 15:54:47.068768');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-20  0:18:37
