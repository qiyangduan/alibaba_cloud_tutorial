-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: rm-gs5za51i7trp7x83aio.mysql.singapore.rds.aliyuncs.com    Database: db1
-- ------------------------------------------------------
-- Server version	5.6.16-log

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED='285806ab-2972-11e9-b11e-506b4b0c20a8:1-38606';

--
-- Table structure for table `apply1`
--

DROP TABLE IF EXISTS `apply1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apply1` (
  `index` bigint(20) DEFAULT NULL,
  `Unnamed: 0` bigint(20) DEFAULT NULL,
  `job` text,
  `age_avg` double DEFAULT NULL,
  `duration_avg` double DEFAULT NULL,
  `cust_count` bigint(20) DEFAULT NULL,
  KEY `ix_apply1_index` (`index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apply1`
--

LOCK TABLES `apply1` WRITE;
/*!40000 ALTER TABLE `apply1` DISABLE KEYS */;
INSERT INTO `apply1` VALUES (0,0,'admin.',38.08357628765793,256.310009718173,1029),(1,1,'blue-collar',39.5456595264938,263.51409244644873,887),(2,2,'entrepreneur',42.392857142857146,277.29285714285714,140),(3,3,'housemaid',45.64347826086957,260.97391304347826,115),(4,4,'management',43.03448275862069,251.03103448275863,290),(5,5,'retired',62.82051282051282,265.0833333333333,156),(6,6,'self-employed',40.44078947368421,262.4078947368421,152),(7,7,'services',37.81679389312977,281.2849872773537,393),(8,8,'student',25.74468085106383,262.69148936170205,94),(9,9,'technician',38.74748923959828,246.1736011477762,697),(10,10,'unemployed',39.90217391304348,282.1847826086956,92),(11,11,'unknown',40.03703703703704,253.22222222222226,27);
/*!40000 ALTER TABLE `apply1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apply_stat`
--

DROP TABLE IF EXISTS `apply_stat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `apply_stat` (
  `apply_day` varchar(100) DEFAULT NULL,
  `job` varchar(500) DEFAULT NULL,
  `age_avg` float DEFAULT NULL,
  `duration_avg` float DEFAULT NULL,
  `cust_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apply_stat`
--

LOCK TABLES `apply_stat` WRITE;
/*!40000 ALTER TABLE `apply_stat` DISABLE KEYS */;
INSERT INTO `apply_stat` VALUES ('2019-02-01','admin.',38.0836,256.31,1029),('2019-02-01','blue-collar',39.5457,263.514,887),('2019-02-01','entrepreneur',42.3929,277.293,140),('2019-02-01','housemaid',45.6435,260.974,115),('2019-02-01','management',43.0345,251.031,290),('2019-02-01','retired',62.8205,265.083,156),('2019-02-01','self-employed',40.4408,262.408,152),('2019-02-01','services',37.8168,281.285,393),('2019-02-01','student',25.7447,262.691,94),('2019-02-01','technician',38.7475,246.174,697),('2019-02-01','unemployed',39.9022,282.185,92),('2019-02-01','unknown',40.037,253.222,27),('2019-02-02','admin.',38.6257,256.512,1098),('2019-02-02','blue-collar',39.2995,274.337,925),('2019-02-02','entrepreneur',40.7386,295.02,153),('2019-02-02','housemaid',46.8182,241.764,110),('2019-02-02','management',41.9483,238.362,290),('2019-02-02','retired',62.7143,292.911,168),('2019-02-02','self-employed',39.9,254.3,150),('2019-02-02','services',37.171,255.211,427),('2019-02-02','student',25.254,201.73,63),('2019-02-02','technician',38.5205,258.051,707),('2019-02-02','unemployed',40.8854,219.188,96),('2019-02-02','unknown',45.6591,203.659,44);
/*!40000 ALTER TABLE `apply_stat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people` (
  `name` varchar(100) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people`
--

LOCK TABLES `people` WRITE;
/*!40000 ALTER TABLE `people` DISABLE KEYS */;
INSERT INTO `people` VALUES ('mysql1:02:29AM on February 08, 2019',20),('mysql1:12:00AM on February 01, 2019',20),('mysql1:12:00AM on February 02, 2019',20),('mysql1:12:00AM on February 03, 2019',20),('mysql1:12:00AM on February 04, 2019',20),('mysql1:12:00AM on February 05, 2019',20),('mysql1:12:00AM on February 06, 2019',20),('mysql1:06:29PM on February 07, 2019',20);
/*!40000 ALTER TABLE `people` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-08 21:11:55
