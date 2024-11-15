-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: apc_db
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `HABITACIONES`
--

DROP TABLE IF EXISTS `HABITACIONES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `HABITACIONES` (
  `habitacion_id` int NOT NULL AUTO_INCREMENT,
  `capacidad` int NOT NULL,
  `hotel_id` int DEFAULT NULL,
  PRIMARY KEY (`habitacion_id`),
  KEY `hotel_id` (`hotel_id`),
  CONSTRAINT `HABITACIONES_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `HOTELES` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HABITACIONES`
--

LOCK TABLES `HABITACIONES` WRITE;
/*!40000 ALTER TABLE `HABITACIONES` DISABLE KEYS */;
/*!40000 ALTER TABLE `HABITACIONES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HOTELES`
--

DROP TABLE IF EXISTS `HOTELES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `HOTELES` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HOTELES`
--

LOCK TABLES `HOTELES` WRITE;
/*!40000 ALTER TABLE `HOTELES` DISABLE KEYS */;
/*!40000 ALTER TABLE `HOTELES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RESERVAS`
--

DROP TABLE IF EXISTS `RESERVAS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RESERVAS` (
  `reserva_id` int NOT NULL AUTO_INCREMENT,
  `cant_personas` int NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `fecha_egreso` date NOT NULL,
  `habitacion_id` int NOT NULL,
  PRIMARY KEY (`reserva_id`),
  KEY `habitacion_id` (`habitacion_id`),
  CONSTRAINT `RESERVAS_ibfk_1` FOREIGN KEY (`habitacion_id`) REFERENCES `HABITACIONES` (`habitacion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RESERVAS`
--

LOCK TABLES `RESERVAS` WRITE;
/*!40000 ALTER TABLE `RESERVAS` DISABLE KEYS */;
/*!40000 ALTER TABLE `RESERVAS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-15 14:23:34
