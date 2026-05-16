-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital_management
-- ------------------------------------------------------
-- Server version	8.0.45

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'Azhar','','zia','Azhar zia','1234567890','azhar1062004@gmail.com','8840486526','2026-04-04 17:52:24'),(2,'Jannat','','Ansari','gul e jannat','Jannat@123','gul@gmail.com','9876543210','2026-04-04 18:00:02'),(3,'Tayyaba','','zia','tayyaba','tayyaba112233','tayyaba@15','7890123456','2026-04-05 18:34:06');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointments`
--

DROP TABLE IF EXISTS `appointments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointments` (
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  `patient_id` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `doctor_name` varchar(50) DEFAULT NULL,
  `appointment_date` date DEFAULT NULL,
  `appointment_time` time DEFAULT NULL,
  `token_number` int DEFAULT NULL,
  `status` varchar(20) DEFAULT 'scheduled',
  `full_name` varchar(50) DEFAULT NULL,
  `contact` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `consultation_start` datetime DEFAULT NULL,
  `consultation_end` datetime DEFAULT NULL,
  `consultation_duration` int DEFAULT NULL,
  PRIMARY KEY (`appointment_id`),
  UNIQUE KEY `unique_token` (`doctor_id`,`appointment_date`,`token_number`),
  KEY `patient_id` (`patient_id`),
  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`),
  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointments`
--

LOCK TABLES `appointments` WRITE;
/*!40000 ALTER TABLE `appointments` DISABLE KEYS */;
INSERT INTO `appointments` VALUES (1,2,1,'Ahmed Khan','2026-05-02','10:05:00',1,'completed','Atif Khan','99999999999','male','2004-10-10','2026-05-02 11:58:19','2026-05-02 11:58:26',0),(2,4,3,'John Khan','2026-05-02','09:00:00',1,'completed','Azmeer','7098765432','male','2005-10-01',NULL,NULL,NULL),(3,1,1,'Ahmed Khan','2026-05-02','09:00:00',2,'completed','Shamama','1234567890','female','2005-08-21','2026-05-02 11:58:30','2026-05-02 00:59:09',5),(12,1,3,'John Khan','2026-05-02','09:00:00',2,'completed','Jannat','9932443214','female','2002-11-20',NULL,NULL,NULL),(13,5,1,'Ahmed Khan','2026-05-02','11:30:00',3,'completed','Sana Zehra','7543278969','female','2002-01-26','2026-05-02 11:30:56','2026-05-02 11:31:03',0),(14,4,3,'John Khan','2026-05-02','11:30:00',3,'completed','Ali','7344550954','male','2004-02-22',NULL,NULL,NULL),(15,5,1,'Ahmed Khan','2026-05-02','14:15:00',4,'completed','Alia ali','7543278969','female','2020-10-20','2026-05-02 22:13:40','2026-05-02 22:13:52',0),(16,5,3,'John Khan','2026-05-02','11:30:00',4,'completed','Anam','7543278969','female','2026-06-02',NULL,NULL,NULL),(17,5,1,'Ahmed Khan','2026-05-02','09:00:00',5,'completed','aliakhan','7543278969','female','2026-05-04',NULL,NULL,NULL),(18,5,1,'Ahmed Khan','2026-05-02','00:00:00',6,'completed','alia khan','7543278969','female','',NULL,NULL,NULL),(19,3,NULL,'Ahmad khan','2026-05-02','00:00:00',1,'completed','Muskan','99350789456','female','2004-04-21',NULL,NULL,NULL),(20,3,5,'Gul E Jannat','2026-05-03','09:00:00',2,'scheduled','Muskan','99350789456','female','2004-04-21',NULL,NULL,NULL),(21,2,5,'Gul E Jannat','2026-05-03','09:00:00',1,'scheduled','Khadeeja','9876543210','female','2004-10-10',NULL,NULL,NULL);
/*!40000 ALTER TABLE `appointments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `department_id` int NOT NULL AUTO_INCREMENT,
  `department_name` varchar(100) NOT NULL,
  `description` text,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,'Cardiology','Heart related treatments'),(2,'Orthopedics','Bone and joint treatments'),(3,'General Medicine','General health issues'),(4,'Neurology','Brain and nervous system');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctors`
--

DROP TABLE IF EXISTS `doctors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctors` (
  `doctor_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `specialization` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `department_id` int DEFAULT NULL,
  `available_from` time DEFAULT NULL,
  `available_to` time DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `middle_name` char(20) DEFAULT NULL,
  `last_name` char(30) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`),
  UNIQUE KEY `username` (`username`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `doctors_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctors`
--

LOCK TABLES `doctors` WRITE;
/*!40000 ALTER TABLE `doctors` DISABLE KEYS */;
INSERT INTO `doctors` VALUES (1,'Ahmed','Cardiologist','9876543210','ahmed@hospital.com',1,'09:00:00','14:00:00','Ahmad khan','12345',NULL,'Khan'),(2,'Ravi','Orthopedic','9876543211','ravi@hospital.com',2,'10:00:00','15:00:00','ravi','ravi@123',NULL,'singh'),(3,'John','General Physician','9876543212','john@hospital.com',3,'08:00:00','13:00:00','john','john@123',NULL,'Khan'),(4,'Azhar','Cardiology','5555555','Azhar@123',NULL,NULL,NULL,'azh','11111',NULL,'Zia'),(5,'Gul','Radiologist','8840489765','jannat@2004',NULL,NULL,NULL,'jannat112233','jannat@123',NULL,'E Jannat'),(6,'Samra','Neurologist','8888777745','samra@123gmail.com',NULL,NULL,NULL,'saamra','samra1234','Fatma','Naqvi'),(7,'Zainab','Fever','9935442311','zainab@1234',NULL,'12:00:00','14:00:00','zainab','zainab1234','Fatma','Khan'),(8,'Tabish','Cardiology','994532145','tabish@123gmail.com',NULL,'10:00:00','13:00:00','tabish','Tabish@123','Naim','Azmi');
/*!40000 ALTER TABLE `doctors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emergency_cases`
--

DROP TABLE IF EXISTS `emergency_cases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emergency_cases` (
  `emergency_id` int NOT NULL AUTO_INCREMENT,
  `patient_id` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `priority_level` int DEFAULT NULL,
  `description` text,
  `arrival_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`emergency_id`),
  KEY `patient_id` (`patient_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `emergency_cases_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`),
  CONSTRAINT `emergency_cases_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emergency_cases`
--

LOCK TABLES `emergency_cases` WRITE;
/*!40000 ALTER TABLE `emergency_cases` DISABLE KEYS */;
/*!40000 ALTER TABLE `emergency_cases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medical_records`
--

DROP TABLE IF EXISTS `medical_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medical_records` (
  `record_id` int NOT NULL AUTO_INCREMENT,
  `patient_id` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `diagnosis` text,
  `prescription` text,
  `visit_date` date DEFAULT NULL,
  PRIMARY KEY (`record_id`),
  KEY `patient_id` (`patient_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `medical_records_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`),
  CONSTRAINT `medical_records_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medical_records`
--

LOCK TABLES `medical_records` WRITE;
/*!40000 ALTER TABLE `medical_records` DISABLE KEYS */;
/*!40000 ALTER TABLE `medical_records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `message_id` int NOT NULL AUTO_INCREMENT,
  `sender_type` varchar(20) DEFAULT NULL,
  `sender_id` int DEFAULT NULL,
  `receiver_type` varchar(20) DEFAULT NULL,
  `receiver_id` int DEFAULT NULL,
  `subject` varchar(255) DEFAULT NULL,
  `message_body` text NOT NULL,
  `is_read` tinyint(1) DEFAULT '0',
  `sent_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patients`
--

DROP TABLE IF EXISTS `patients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patients` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `address` text,
  `registered_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`patient_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patients`
--

LOCK TABLES `patients` WRITE;
/*!40000 ALTER TABLE `patients` DISABLE KEYS */;
INSERT INTO `patients` VALUES (1,'AZ','HAR','ZIA','Male','2004-06-10','1234567890','Azhar@123456',NULL,'2026-04-04 19:31:38','ZIA','1234567'),(2,'Saamra','Fatma','MCA','Female','2004-06-10','9988776655','saamra@123','Azamgarh UP','2026-04-05 12:34:38','Saamra','saamra123'),(3,'Shamama','','Zia','Female','2005-08-14','94545667321','shamama@1111','Gorakhpur','2026-04-05 18:33:06','Mama','shamama@2005'),(4,'Tanveer','Ahmad','Khan','Male','2005-06-13','7890654321','tanveer@112233','Gorakhpur','2026-04-06 08:34:28','tannu','tannu112233'),(5,'Alia','khan','ali','Female','2023-01-10','7543278969','aliakhan@gmail.com','lucknow','2026-04-06 09:26:51','aliakhan','alia1234'),(29,'Mohd','Zeeshan','Siddiqui','Male','2000-05-29','9876123456','Zeeshan@123','Sandeela, Malihabaad','2026-04-28 13:00:19','Zeeshu','Zeeshan@123');
/*!40000 ALTER TABLE `patients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payments` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  `appointment_id` int NOT NULL,
  `patient_id` int NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `payment_method` enum('online','clinic') DEFAULT NULL,
  `payment_status` enum('pending','completed','failed') DEFAULT 'pending',
  `transaction_id` varchar(100) DEFAULT NULL,
  `payment_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`payment_id`),
  UNIQUE KEY `transaction_id` (`transaction_id`),
  KEY `appointment_id` (`appointment_id`),
  KEY `patient_id` (`patient_id`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`appointment_id`) REFERENCES `appointments` (`appointment_id`) ON DELETE CASCADE,
  CONSTRAINT `payments_ibfk_2` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `queue_tokens`
--

DROP TABLE IF EXISTS `queue_tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `queue_tokens` (
  `token_id` int NOT NULL AUTO_INCREMENT,
  `patient_id` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `token_number` int DEFAULT NULL,
  `visit_date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT 'waiting',
  `called_at` timestamp NULL DEFAULT NULL,
  `completed_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`token_id`),
  KEY `patient_id` (`patient_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `queue_tokens_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`),
  CONSTRAINT `queue_tokens_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `queue_tokens`
--

LOCK TABLES `queue_tokens` WRITE;
/*!40000 ALTER TABLE `queue_tokens` DISABLE KEYS */;
/*!40000 ALTER TABLE `queue_tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receptionists`
--

DROP TABLE IF EXISTS `receptionists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receptionists` (
  `receptionist_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`receptionist_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receptionists`
--

LOCK TABLES `receptionists` WRITE;
/*!40000 ALTER TABLE `receptionists` DISABLE KEYS */;
INSERT INTO `receptionists` VALUES (1,'Sara',NULL,'Ahmed','9876543200','sara@hospital.com','password123','sara'),(2,'Salwa','','Fatma','990000','asdf@123','111111','1234'),(3,'Fiza','','Farheen','666655555','fiza@2003','fiza@1234','fiza'),(4,'Salooni','Singh','Rathoor','9956784321','singh@123','Salooni@123','salooni123');
/*!40000 ALTER TABLE `receptionists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` enum('admin','doctor','patient','receptionist') DEFAULT NULL,
  `admin_id` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `patient_id` int DEFAULT NULL,
  `receptionist_id` int DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`),
  KEY `admin_id` (`admin_id`),
  KEY `doctor_id` (`doctor_id`),
  KEY `patient_id` (`patient_id`),
  KEY `receptionist_id` (`receptionist_id`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`admin_id`),
  CONSTRAINT `users_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`),
  CONSTRAINT `users_ibfk_3` FOREIGN KEY (`patient_id`) REFERENCES `patients` (`patient_id`),
  CONSTRAINT `users_ibfk_4` FOREIGN KEY (`receptionist_id`) REFERENCES `receptionists` (`receptionist_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-15 17:10:32
