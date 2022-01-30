-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: bookstoredb
-- ------------------------------------------------------
-- Server version	8.0.27

# 1.把文件中的所有的 utf8mb4_0900_ai_ci 替换为 utf8_general_ci
# 以及 utf8mb4 替换为 utf8
# 2.首行加入使用哪个库，use bookstoredb

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
use bookstoredb;
DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'library'),(1,'reader');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,2,29),(2,2,30);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add author',7,'add_author'),(26,'Can change author',7,'change_author'),(27,'Can delete author',7,'delete_author'),(28,'Can view author',7,'view_author'),(29,'Can add book',8,'add_book'),(30,'Can change book',8,'change_book'),(31,'Can delete book',8,'delete_book'),(32,'Can view book',8,'view_book'),(33,'Can add user info',9,'add_userinfo'),(34,'Can change user info',9,'change_userinfo'),(35,'Can delete user info',9,'delete_userinfo'),(36,'Can view user info',9,'view_userinfo'),(37,'Can add book extend',10,'add_bookextend'),(38,'Can change book extend',10,'change_bookextend'),(39,'Can delete book extend',10,'delete_bookextend'),(40,'Can view book extend',10,'view_bookextend'),(41,'Can add pub name',11,'add_pubname'),(42,'Can change pub name',11,'change_pubname'),(43,'Can delete pub name',11,'delete_pubname'),(44,'Can view pub name',11,'view_pubname'),(45,'Can add extend userinfo',12,'add_extenduserinfo'),(46,'Can change extend userinfo',12,'change_extenduserinfo'),(47,'Can delete extend userinfo',12,'delete_extenduserinfo'),(48,'Can view extend userinfo',12,'view_extenduserinfo'),(49,'Can add user',13,'add_user'),(50,'Can change user',13,'change_user'),(51,'Can delete user',13,'delete_user'),(52,'Can view user',13,'view_user'),(53,'Can add article',14,'add_article'),(54,'Can change article',14,'change_article'),(55,'Can delete article',14,'delete_article'),(56,'Can view article',14,'view_article'),(57,' Can View Index ',13,'can_view_index'),(58,'Can change the status of server',13,'change_server_status'),(59,'Can publish books',9,'publish_book'),(60,'Can comment books',9,'comment_book');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$CkXn3lN5ARlM32cOwDVNX4$HjpGCZr3rCcZEnKxIxG8fZBf31/WyFSfjAI2ySxuZzA=','2022-01-25 16:52:11.529083',1,'admin','','','123@qq.com',1,1,'2022-01-20 15:27:00.895884'),(2,'pbkdf2_sha256$320000$14xqWkyT7QPX8bINSp7ana$0a0QdjoElbe7cb7DUfkmtXN5WgZUQV7p0mIArpgyMLo=','2022-01-25 17:17:07.787451',0,'bookstore','','','123@163.com',0,1,'2022-01-23 16:30:40.773107'),(6,'pbkdf2_sha256$320000$MOgu4e1QxemZz97QF5Iluy$RCOZe3re00mEdRH1wcB3B1v3J9Qqf/GdUFmzBwZoVvo=','2022-01-25 17:32:39.942918',0,'jack','','','123@163.com',0,1,'2022-01-25 17:18:53.868485');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,1),(2,2,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (7,2,32),(8,6,32);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-01-20 16:18:27.252997','2','title:Redis pub:出版社: 清华出版社 price:30',2,'[{\"changed\": {\"fields\": [\"\\u5b9a\\u4ef7\"]}}]',8,1),(2,'2022-01-20 16:18:27.269156','1','title:Python Django pub:出版社: 清华出版社 price:60',2,'[{\"changed\": {\"fields\": [\"\\u5b9a\\u4ef7\"]}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(14,'index','article'),(7,'index','author'),(8,'index','book'),(10,'index','bookextend'),(12,'index','extenduserinfo'),(11,'index','pubname'),(9,'index','userinfo'),(6,'sessions','session'),(13,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-01-19 01:07:04.104504'),(2,'auth','0001_initial','2022-01-19 01:07:05.199746'),(3,'admin','0001_initial','2022-01-19 01:07:05.471939'),(4,'admin','0002_logentry_remove_auto_add','2022-01-19 01:07:05.490941'),(5,'admin','0003_logentry_add_action_flag_choices','2022-01-19 01:07:05.508895'),(6,'contenttypes','0002_remove_content_type_name','2022-01-19 01:07:05.717954'),(7,'auth','0002_alter_permission_name_max_length','2022-01-19 01:07:05.899990'),(8,'auth','0003_alter_user_email_max_length','2022-01-19 01:07:05.939676'),(9,'auth','0004_alter_user_username_opts','2022-01-19 01:07:05.957040'),(10,'auth','0005_alter_user_last_login_null','2022-01-19 01:07:06.037248'),(11,'auth','0006_require_contenttypes_0002','2022-01-19 01:07:06.043102'),(12,'auth','0007_alter_validators_add_error_messages','2022-01-19 01:07:06.054157'),(13,'auth','0008_alter_user_username_max_length','2022-01-19 01:07:06.139670'),(14,'auth','0009_alter_user_last_name_max_length','2022-01-19 01:07:06.233556'),(15,'auth','0010_alter_group_name_max_length','2022-01-19 01:07:06.261913'),(16,'auth','0011_update_proxy_permissions','2022-01-19 01:07:06.273757'),(17,'auth','0012_alter_user_first_name_max_length','2022-01-19 01:07:06.365783'),(18,'sessions','0001_initial','2022-01-19 01:07:06.425711'),(19,'index','0001_initial','2022-01-19 01:09:36.634431'),(20,'index','0002_bookextend','2022-01-18 17:11:28.610924'),(21,'index','0003_pubname_remove_book_public_book_pub','2022-01-18 17:11:28.789165'),(22,'index','0004_extenduserinfo','2022-01-18 17:26:08.726755'),(23,'index','0005_userinfo_gender','2022-01-18 17:30:27.755093'),(24,'index','0006_alter_userinfo_gender','2022-01-18 17:36:28.401795'),(25,'index','0007_author_books','2022-01-18 17:43:50.166704'),(26,'index','0008_remove_author_books','2022-01-18 18:20:19.043277'),(27,'user','0001_initial','2022-01-21 16:56:48.255984'),(28,'user','0002_alter_user_password','2022-01-21 16:56:48.263162'),(29,'user','0003_user_create_time_alter_user_password_and_more','2022-01-21 18:38:41.358743'),(30,'index','0008_article','2022-01-24 17:09:44.895191'),(31,'user','0004_alter_user_options','2022-01-24 17:09:44.904175'),(32,'user','0005_alter_user_options','2022-01-24 17:09:44.912730'),(33,'user','0006_user_email','2022-01-27 17:50:01.352968');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1t9p3fes0q364mdiv33w3ku907yzuidb','eyJ1c2VybmFtZSI6ImhoIn0:1nAcQY:dZ4jHpWgyh899e3RQgdgvcrpUbk_PhQXxFj_d27mPLA','2022-02-03 18:44:54.312361'),('44mhi45vwqqyjiz1kbvc2xcm7kv5i2re','eyJ1c2VybmFtZSI6ImhoIn0:1nAwnK:JTgA8J9f6T6aphK8bT18ZykTkapbwmmar2ciHnVAEuI','2022-02-04 16:29:46.899751'),('4wqmzs8skn2q51vj6elcuxfqcp4ovphs','.eJxVjDsOwjAQBe_iGlnxb5VQ0nMGa727xgFkS3FSIe4OkVJA-2bmvVTEbS1x67LEmdVZWXX63RLSQ-oO-I711jS1ui5z0ruiD9r1tbE8L4f7d1Cwl2-dwHjhkMRPHhKzc17IsgGQIQllZ6zFYcqCIxFBgAyQhVwQxpF9Vu8PCb85Uw:1nCOis:_MLJ643zwnqbjLR52V0a4U0XXDrzjKD1OZ7SnqfRxWE','2022-02-08 16:31:10.638084'),('5zper3sqlhmw8sgscdsddyo4806tevbr','.eJxVjDEOwjAMRe-SGUWxU0jMyN4zVLZjaAG1UtNOiLtDpQ6w_vfef7mO16Xv1mpzNxR3duAOv5uwPmzcQLnzeJu8TuMyD-I3xe-0-nYq9rzs7t9Bz7X_1tGCAEVCTDEm1SxHUGLJDVpQATYrCMrUACYmKdEw8xU5nBrKxO79Ad0gN_E:1nCObo:DbjzTrzkTkQEbnA6PBYh9M5YneGboRXvsLWRwz1cquQ','2022-02-08 16:23:52.030757'),('8uwbszt594boxacolwt9jegl13156m82','eyJ1c2VybmFtZSI6ImhoIn0:1nAx3U:OKcSqDLFNRtsd1kqbaj9FefacgpQYOxu14eB4EThWNw','2022-02-04 16:46:28.273005'),('c1fodmu8f13xs8c6gzo45ww4h1wmx8rk','eyJ1c2VybmFtZSI6ImhoIn0:1nAx5M:pXwp8zngGunJWd_uNzi7ScEXk8m8vDyj6lUz80DrEFI','2022-02-04 16:48:24.121520'),('gqaerodl3yez3f6ia61vrsf45v4c01gt','.eJxVjDEOwjAMRe-SGUWxU0jMyN4zVLZjaAG1UtNOiLtDpQ6w_vfef7mO16Xv1mpzNxR3duAOv5uwPmzcQLnzeJu8TuMyD-I3xe-0-nYq9rzs7t9Bz7X_1tGCAEVCTDEm1SxHUGLJDVpQATYrCMrUACYmKdEw8xU5nBrKxO79Ad0gN_E:1nCOQ5:jQy2x3jSCWms272PTghGXnPArrL8-XDQHT3SeBSyylw','2022-02-08 16:11:45.259284'),('hjeah9fq4m6d14toam3sl4yaw0wqxmi5','eyJ1c2VybmFtZSI6ImhoIn0:1nAx7c:tNq0AzrdgTkLmiizXZro7WYm7cOIl6MR39JC9R5cd18','2022-02-04 16:50:44.719993'),('iihiedqjnqu0okaxfbttawltzn1umao0','.eJxVjEsOwjAMBe-SNYoap9CYJfueobIdQ8onlfpZIe5OInUB2zfz5m0G2tY0bIvOwxjN2Thz-N2Y5KG5gninfJusTHmdR7ZVsTtdbD9FfV529y-QaEnl7bVhhx4BOu87kcBHJ0gcWtBG2JFqBCeErYOOkKNXCHQFak4tBqQSrblMLy21lMznC4bXPQ8:1nAcMU:cfELJH3d-_Dah-No28txfk6V3qxvGJSAu_QRzzDtySc','2022-02-03 18:40:42.339469'),('je0t4now6x155jn7smc0fvqwt65ju9wl','eyJ1c2VybmFtZSI6ImhoIn0:1nAwrU:uK-gN_-22-qMq3SwghXpaxBbdFC5XAqT8DQccTBMMjo','2022-02-04 16:34:04.737085'),('k4dt2gbx7172oqzax4q7tubf7adpzjo8','e30:1nAy6T:A5RvMac3w6cEEkyzYfmAGljjelUdPisZ_Vx8RZJtLHI','2022-02-04 17:53:37.027554'),('kthmpva9tu4logv89ws8t9we7d9zlq5k','eyJ1c2VybmFtZSI6ImphY2sifQ:1nAc1u:SNMs6_tASk0u5suJdac9AJSJOhfYWQHUMDx23SDFn4o','2022-02-03 18:19:26.431811'),('m03huw98k7y59x2hvpul57yehjng3nwo','e30:1nB7Vv:isL0ZgR6EH2CGKWEobTua8qiSQZVRKjXLEXT_NAALUo','2022-02-05 03:56:31.946042'),('mfldb70kgh3clg0vq1uuhudl1cimilu0','e30:1nAyIT:IR7-6j7IRfzMmPGIM64nFJrNN5Wm1fwpRIUHF19mG3I','2022-02-04 18:06:01.226638'),('p1vig67qccxm103yzwv7kf4yswuqm9o3','e30:1nB7Ni:oHpskUA4BbUAYFg2tAWuUmAmRsiMnc2miqYDj3FdPhU','2022-02-05 03:48:02.426910'),('p9lk67td4p6jnm84d97niyos9inom6zn','.eJxVjDEOwjAMRe-SGUWxU0jMyN4zVLZjaAG1UtNOiLtDpQ6w_vfef7mO16Xv1mpzNxR3duAOv5uwPmzcQLnzeJu8TuMyD-I3xe-0-nYq9rzs7t9Bz7X_1tGCAEVCTDEm1SxHUGLJDVpQATYrCMrUACYmKdEw8xU5nBrKxO79Ad0gN_E:1nCNoo:VQFF4u8PevHhqdX932Sh4nbzK2w9ifzeJKma1ld1j6s','2022-02-08 15:33:14.588790'),('pxt91egska4dur1evzhe1g6u1qoitimz','.eJxVjDEOwjAMRe-SGUWxU0jMyN4zVLZjaAG1UtNOiLtDpQ6w_vfef7mO16Xv1mpzNxR3duAOv5uwPmzcQLnzeJu8TuMyD-I3xe-0-nYq9rzs7t9Bz7X_1tGCAEVCTDEm1SxHUGLJDVpQATYrCMrUACYmKdEw8xU5nBrKxO79Ad0gN_E:1nCOKp:kIZRy5r81VlQ1eG6I9foge5aiRCcYej--otcm1cp_PE','2022-02-08 16:06:19.542837'),('q34s1e30d2k6smobfpfzmq8j5kq20a0j','eyJ1c2VybmFtZSI6ImhoIn0:1nAwi5:sGVeVvOS-7g0N2U_sUHhOIu1kXuyYGklASQmAeD1ko0','2022-02-04 16:24:21.798966'),('u0qcf32fgywnmv48aawbnoh0h1u0xvec','eyJ1c2VybmFtZSI6ImFkbWluIn0:1nAywe:-m2v7xMejs1mMWmuWxJSeNtdmyd3ffbC8LaWeYbzFYY','2022-02-04 18:47:32.232817'),('ub63quesmo8bajj3u9ufkg0bwe3zkhoi','.eJxVjDEOwjAMRe-SGUWxU0jMyN4zVLZjaAG1UtNOiLtDpQ6w_vfef7mO16Xv1mpzNxR3duAOv5uwPmzcQLnzeJu8TuMyD-I3xe-0-nYq9rzs7t9Bz7X_1tGCAEVCTDEm1SxHUGLJDVpQATYrCMrUACYmKdEw8xU5nBrKxO79Ad0gN_E:1nCOYG:TU_Y2XkbCqMokXUVKkh-9WJNdmZIRXPyfV8XoqT1NSo','2022-02-08 16:20:12.893535'),('wmqelulf8glqlo2g3qe995jouczv5uwk','.eJxVjEEOwiAQRe_C2pAyUECX7nsGMsOAVA0kpV0Z765NutDtf-_9lwi4rSVsPS1hZnERVpx-N8L4SHUHfMd6azK2ui4zyV2RB-1yapye18P9OyjYy7d2o2KlgRFg1DmCHpz3hGwIMBmnSXuvjKGY2YE15AHJ6nweB45kcRDvD9NrN74:1nCPgN:4wSpPx6eGk-wjcBuesuFaWrTKLNqsgMjje3Msfyvpj0','2022-02-08 17:32:39.950943'),('wzn8qohsugwgguc19f7mdk1mblrwt6rc','e30:1nAyFR:J5IUTHl6BVSsrVeFkgplS0KkpyB-UWLwfln1nZpPGBw','2022-02-04 18:02:53.669891'),('y4hne5r2x1flofbbe6xu8jixbawyk9l6','.eJxVjDEOwjAMRe-SGUWxU0jMyN4zVLZjaAG1UtNOiLtDpQ6w_vfef7mO16Xv1mpzNxR3duAOv5uwPmzcQLnzeJu8TuMyD-I3xe-0-nYq9rzs7t9Bz7X_1tGCAEVCTDEm1SxHUGLJDVpQATYrCMrUACYmKdEw8xU5nBrKxO79Ad0gN_E:1nAZLo:qdkWWWuYELq14MOzXt_yQUWat1EzEPowsXsDia1FxBU','2022-02-03 15:27:48.283339');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_article`
--

DROP TABLE IF EXISTS `index_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `index_article` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `author_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_article_author_id_7631e703_fk_auth_user_id` (`author_id`),
  CONSTRAINT `index_article_author_id_7631e703_fk_auth_user_id` FOREIGN KEY (`author_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_article`
--

LOCK TABLES `index_article` WRITE;
/*!40000 ALTER TABLE `index_article` DISABLE KEYS */;
/*!40000 ALTER TABLE `index_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_author`
--

DROP TABLE IF EXISTS `index_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `index_author` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_author`
--

LOCK TABLES `index_author` WRITE;
/*!40000 ALTER TABLE `index_author` DISABLE KEYS */;
INSERT INTO `index_author` VALUES (33,'Luncy','123456@qq.com'),(34,'Tom','456789@163.com');
/*!40000 ALTER TABLE `index_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_author_books`
--

DROP TABLE IF EXISTS `index_author_books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `index_author_books` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `author_id` bigint NOT NULL,
  `book_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_author_books_author_id_book_id_b0dd3503_uniq` (`author_id`,`book_id`),
  KEY `index_author_books_book_id_1c280bc9_fk_index_book_id` (`book_id`),
  CONSTRAINT `index_author_books_author_id_2bfd143c_fk_index_author_id` FOREIGN KEY (`author_id`) REFERENCES `index_author` (`id`),
  CONSTRAINT `index_author_books_book_id_1c280bc9_fk_index_book_id` FOREIGN KEY (`book_id`) REFERENCES `index_book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_author_books`
--

LOCK TABLES `index_author_books` WRITE;
/*!40000 ALTER TABLE `index_author_books` DISABLE KEYS */;
INSERT INTO `index_author_books` VALUES (78,33,1),(79,33,2),(81,34,1),(82,34,4),(83,34,5);
/*!40000 ALTER TABLE `index_author_books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_book`
--

DROP TABLE IF EXISTS `index_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `index_book` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(30) NOT NULL,
  `price` decimal(7,2) NOT NULL,
  `retail_price` decimal(7,2) NOT NULL,
  `pub_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `index_book_pub_id_20c860e2_fk_index_pubname_id` (`pub_id`),
  CONSTRAINT `index_book_pub_id_20c860e2_fk_index_pubname_id` FOREIGN KEY (`pub_id`) REFERENCES `index_pubname` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_book`
--

LOCK TABLES `index_book` WRITE;
/*!40000 ALTER TABLE `index_book` DISABLE KEYS */;
INSERT INTO `index_book` VALUES (1,'Python Django',60.00,69.00,1),(2,'Redis',40.02,45.00,1),(4,'Django',80.02,60.00,2),(5,'Flask',45.01,55.00,2),(6,'gRPC',60.00,100.00,7),(8,'面试算法',60.00,90.00,13),(9,'go 语言',60.00,90.00,13);
/*!40000 ALTER TABLE `index_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_extenduserinfo`
--

DROP TABLE IF EXISTS `index_extenduserinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `index_extenduserinfo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `signature` varchar(255) NOT NULL,
  `nickname` varchar(255) NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `index_extenduserinfo_user_id_25af9640_fk_index_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `index_userinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_extenduserinfo`
--

LOCK TABLES `index_extenduserinfo` WRITE;
/*!40000 ALTER TABLE `index_extenduserinfo` DISABLE KEYS */;
INSERT INTO `index_extenduserinfo` VALUES (1,'good good study,day day up','XH',2);
/*!40000 ALTER TABLE `index_extenduserinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_pubname`
--

DROP TABLE IF EXISTS `index_pubname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `index_pubname` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pubname` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pubname` (`pubname`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_pubname`
--

LOCK TABLES `index_pubname` WRITE;
/*!40000 ALTER TABLE `index_pubname` DISABLE KEYS */;
INSERT INTO `index_pubname` VALUES (2,'c语言中文网出版'),(7,'北大出版社'),(1,'清华出版社'),(13,'王者出版社');
/*!40000 ALTER TABLE `index_pubname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_userinfo`
--

DROP TABLE IF EXISTS `index_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `index_userinfo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(24) NOT NULL,
  `password` varchar(24) NOT NULL,
  `gender` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_userinfo`
--

LOCK TABLES `index_userinfo` WRITE;
/*!40000 ALTER TABLE `index_userinfo` DISABLE KEYS */;
INSERT INTO `index_userinfo` VALUES (1,'xiaoming','******','male'),(2,'xiaohong','*******','F'),(3,'admin','admin','M'),(4,'admin','admin','M'),(5,'admin','ff','M');
/*!40000 ALTER TABLE `index_userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `my_cache_table`
--

DROP TABLE IF EXISTS `my_cache_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `my_cache_table` (
  `cache_key` varchar(255) NOT NULL,
  `value` longtext NOT NULL,
  `expires` datetime(6) NOT NULL,
  PRIMARY KEY (`cache_key`),
  KEY `my_cache_table_expires` (`expires`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `my_cache_table`
--

LOCK TABLES `my_cache_table` WRITE;
/*!40000 ALTER TABLE `my_cache_table` DISABLE KEYS */;
INSERT INTO `my_cache_table` VALUES (':1:template.cache.test.d41d8cd98f00b204e9800998ecf8427e','gAWVVgAAAAAAAACMF2RqYW5nby51dGlscy5zYWZlc3RyaW5nlIwKU2FmZVN0cmluZ5STlIwlCiAgICAgICAgPHA+5oiR5piv57yT5a2Y55qEIDwvcD4KICAgIJSFlIGULg==','2022-01-27 17:29:31.000000'),(':1:views.decorators.cache.cache_header..0020caf973a67c9dcbeee2c406f3d490.zh-Hans.Asia/Shanghai','gAVdlC4=','2022-01-27 15:40:36.000000'),(':1:views.decorators.cache.cache_page..GET.0020caf973a67c9dcbeee2c406f3d490.d41d8cd98f00b204e9800998ecf8427e.zh-Hans.Asia/Shanghai','gAWVrAEAAAAAAACMFGRqYW5nby5odHRwLnJlc3BvbnNllIwMSHR0cFJlc3BvbnNllJOUKYGUfZQojAdoZWFkZXJzlGgAjA9SZXNwb25zZUhlYWRlcnOUk5QpgZR9lIwGX3N0b3JllH2UKIwMY29udGVudC10eXBllIwMQ29udGVudC1UeXBllIwYdGV4dC9odG1sOyBjaGFyc2V0PXV0Zi04lIaUjAdleHBpcmVzlIwHRXhwaXJlc5SMHVRodSwgMjcgSmFuIDIwMjIgMTY6MDk6MzYgR01UlIaUjA1jYWNoZS1jb250cm9slIwNQ2FjaGUtQ29udHJvbJSMCm1heC1hZ2U9NjCUhpR1c2KMCF9jaGFyc2V0lE6MEV9yZXNvdXJjZV9jbG9zZXJzlF2UjA5faGFuZGxlcl9jbGFzc5ROjAdjb29raWVzlIwMaHR0cC5jb29raWVzlIwMU2ltcGxlQ29va2lllJOUKYGUjAZjbG9zZWSUiYwOX3JlYXNvbl9waHJhc2WUTowKX2NvbnRhaW5lcpRdlEMXdDEgaXMgMTY0MzI5Nzk3My4yMDA2MDeUYXViLg==','2022-01-27 15:40:36.000000');
/*!40000 ALTER TABLE `my_cache_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_user`
--

DROP TABLE IF EXISTS `user_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `user_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_user`
--

LOCK TABLES `user_user` WRITE;
/*!40000 ALTER TABLE `user_user` DISABLE KEYS */;
INSERT INTO `user_user` VALUES (2,'hh','202cb962ac59075b964b07152d234b70','2022-01-21 18:38:41.131085','hh@163.com'),(3,'admin','21232f297a57a5a743894a0e4a801fc3','2022-01-21 18:47:32.221933','admin@129.com');
/*!40000 ALTER TABLE `user_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-30 23:25:17
