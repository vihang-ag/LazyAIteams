CREATE DATABASE  IF NOT EXISTS `annotationdbname` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `annotationdbname`;
-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: annotationdbname
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `textdata`
--

DROP TABLE IF EXISTS `textdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `textdata` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `data` varchar(1000) DEFAULT NULL,
  `annotation` varchar(45) DEFAULT NULL,
  `human_effort` varchar(45) DEFAULT NULL,
  -- `prediction` varchar(45) DEFAULT NULL,
  -- `model_effort` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `textdata`
--

LOCK TABLES `textdata` WRITE;
/*!40000 ALTER TABLE `textdata` DISABLE KEYS */;
INSERT INTO `textdata` VALUES 
(1, 'and, uh, it was practically new when I moved in here', '', NULL),
(2, 'and, um, when I was at U T, I was in a group called Ensemble One oh Nine, just twelve singers', '', NULL),
(3, 'It\'s yucky.', '', NULL),
(4, 'So what they are  asking you to tell them is all the prescription drugs you are taking which are controlled substances.', '', NULL),
(5, 'Well, it is fun, what little I do.', '', NULL),
(6, 'he\'s the one of the two that votes,', '', NULL),
(7, 'it\'s kind of like learning a language, you know,', '', NULL),
(8, 'Uh-huh.', '', NULL),
(9, 'He, he kind of has free run of the place, and there is or somebody takes care of him.', '', NULL),
(10, 'Well, it sounds like you do quite a bit of it.', '', NULL),
(11, 'and what you\'re going to basically donate to a Goodwill or whatever, anyways, you can get a little bit of money for.', '', NULL),
(12, 'that\'s what they said it was kind of,  a little more  drama to it.', '', NULL),
(13, 'that\'s hard.', '', NULL),
(14, 'you know the governments taken care of that,', '', NULL),
(15, 'Right, I, I usually see her a, couple times a year', '', NULL),
(16, 'They knew, they knew the extras or the,', '', NULL),
(17, 'Third question was how serving for their own gains do you think goes on,', '', NULL),
(18, 'because it\'s not next day they have, the, start the trial, it\'s X number of months and just prolongs the situation that much more.', '', NULL),
(19, 'And, um, I think that if we had enough money and paid the teachers a little bit more, that maybe that could solve some of our problems.', '', NULL),
(20, 'dead, He\'s dead.', '', NULL),
(21, 'he started that', '', NULL),
(22, 'Instead of call waiting or call anything else.', '', NULL),
(23, 'He likes to help me design, um, you know, projects that are, a little more customized.', '', NULL),
(24, 'I was in the room when the emergency technicians brought him in from the ambulance', '', NULL),
(25, 'There\'s not really a lot here in Raleigh.', '', NULL),
(26, 'if, if it\'s on the credit card it doesn\'t seem like it\'s money out of your pocket.', '', NULL),
(27, 'I finally served on one last year.', '', NULL),
(28, 'I don\'t think necessarily that, things are being made better uh, you know,', '', NULL),
(29, 'Past a point it doesn\'t make any difference.', '', NULL),
(30, 'Well, we\'re geared to that.', '', NULL),
(31, 'You know, I, I, my, I remember my, my grandmother many years ago when she was in a nursing home before she died', '', NULL),
(32, 'Yeah,', '', NULL),
(33, 'they, uh, they basically reviewed Oregon\'s plan or The Oregon Plan toward, uh, nationalizing health care and that kind of thing.', '', NULL);
-- COMMIT;

/*!40000 ALTER TABLE `textdata` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-06  9:47:52
