-- MySQL dump 10.13  Distrib 5.1.58, for apple-darwin10.3.0 (i386)
--
-- Host: localhost    Database: ymei
-- ------------------------------------------------------
-- Server version	5.1.58

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Database ymei
--
DROP DATABASE IF EXISTS ymei;
CREATE DATABASE ymei;
USE ymei;

--
-- Table structure for table `ym_administrator`
--

DROP TABLE IF EXISTS `ym_administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ym_administrator` (
  `admin_id` int(7) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `reg_date` datetime NOT NULL,
  `visible` int(1) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ym_administrator`
--

LOCK TABLES `ym_administrator` WRITE;
/*!40000 ALTER TABLE `ym_administrator` DISABLE KEYS */;
/*!40000 ALTER TABLE `ym_administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ym_announcement`
--

DROP TABLE IF EXISTS `ym_announcement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ym_announcement` (
  `announce_id` int(7) NOT NULL AUTO_INCREMENT,
  `admin_id` int(7) NOT NULL,
  `content` varchar(256) DEFAULT NULL,
  `post_date` datetime DEFAULT NULL,
  `visible` int(1) DEFAULT NULL,
  PRIMARY KEY (`announce_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ym_announcement`
--

LOCK TABLES `ym_announcement` WRITE;
/*!40000 ALTER TABLE `ym_announcement` DISABLE KEYS */;
/*!40000 ALTER TABLE `ym_announcement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ym_member`
--

DROP TABLE IF EXISTS `ym_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ym_member` (
  `member_id` int(7) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `email` varchar(32) DEFAULT NULL,
  `qq` int(12) DEFAULT NULL,
  `phone` int(12) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `reg_date` datetime NOT NULL,
  `ip` varchar(16) NOT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ym_member`
--

LOCK TABLES `ym_member` WRITE;
/*!40000 ALTER TABLE `ym_member` DISABLE KEYS */;
/*!40000 ALTER TABLE `ym_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ym_message`
--

DROP TABLE IF EXISTS `ym_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ym_message` (
  `message_id` int(7) NOT NULL AUTO_INCREMENT,
  `member_id` int(7) DEFAULT NULL,
  `admin_id` int(7) DEFAULT NULL,
  `message_pid` int(7) DEFAULT NULL,
  `name` varchar(32) NOT NULL,
  `content` varchar(256) DEFAULT NULL,
  `visible` int(1) DEFAULT NULL,
  `homepage` varchar(32) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `qq` int(12) DEFAULT NULL,
  `msn` varchar(32) DEFAULT NULL,
  `phone` int(12) DEFAULT NULL,
  `address` varchar(128) DEFAULT NULL,
  `post_date` datetime NOT NULL,
  `ip` varchar(16) NOT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ym_message`
--

LOCK TABLES `ym_message` WRITE;
/*!40000 ALTER TABLE `ym_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `ym_message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-11-21 21:00:33
