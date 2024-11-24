-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: apc_db
-- ------------------------------------------------------
-- Server version	8.0.40

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
  `hotel_id` int NOT NULL,
  `habilitado` tinyint(1) NOT NULL DEFAULT TRUE,
  PRIMARY KEY (`habitacion_id`),
  KEY `hotel_id` (`hotel_id`),
  CONSTRAINT `HABITACIONES_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `HOTELES` (`hotel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HABITACIONES`
--

LOCK TABLES `HABITACIONES` WRITE;
/*!40000 ALTER TABLE `HABITACIONES` DISABLE KEYS */;
INSERT INTO `HABITACIONES` VALUES (1,5,8,0),(2,12,8,0),(3,100,10,0),(4,12,8,0),(5,10,12,0);
/*!40000 ALTER TABLE `HABITACIONES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `HOTELES`
--

DROP TABLE IF EXISTS `HOTELES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `HOTELES` (
  `hotel_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `descripcion` text,
  `ubicacion` varchar(255) DEFAULT NULL,
  `habilitado` tinyint(1) NOT NULL DEFAULT TRUE,
  PRIMARY KEY (`hotel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HOTELES`
--

LOCK TABLES `HOTELES` WRITE;
/*!40000 ALTER TABLE `HOTELES` DISABLE KEYS */;
INSERT INTO `HOTELES` VALUES (16,'The Peninsula Paris','The Peninsula Paris, a palace recognised by Lartisien for its excellence. Enter a world of elegance and absolute luxury. Lartisien - For exceptional hotel stays. Membership Benefits.','19 Av. Kléber, 75116 Paris, Francia',0),(17,'Adlon Kempinski Berlin','Früh buchen & mehr sparen — Buchen Sie jetzt und genießen Sie exklusive Angebote für Suiten im Kempinski Adlon Berlin','Unter den Linden 77, 10117 Berlin, Alemania',0),(18,' Four Seasons Buenos Aires','Hotel de lujo en Buenos Aires — Descubra suites y habitaciones espaciosas con amplias vistas de La Mansión y la ciudad. Gastronomia gourmet. Piscina al aire libre. Masage Tango Porteño. Gimnasio.','Posadas 1086 88, C1011ABB Cdad. Autónoma de Buenos Aires',0),(19,'Hotel de prueba','prueba','una ubicacion',0);
/*!40000 ALTER TABLE `HOTELES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `IMAGENES`
--

DROP TABLE IF EXISTS `IMAGENES`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `IMAGENES` (
  `imagen_id` int NOT NULL AUTO_INCREMENT,
  `hotel_id` int NOT NULL,
  `url` text,
  `habilitado` tinyint(1) NOT NULL DEFAULT TRUE,
  PRIMARY KEY (`imagen_id`),
  KEY `hotel_id` (`hotel_id`),
  CONSTRAINT `imagenes_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `HOTELES` (`hotel_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `IMAGENES`
--

LOCK TABLES `IMAGENES` WRITE;
/*!40000 ALTER TABLE `IMAGENES` DISABLE KEYS */;
INSERT INTO `IMAGENES` VALUES (21,16,'https://res.cloudinary.com/grand-luxury/image/upload/w_1440,q_50,f_auto,c_fill,g_center,dpr_2/remote_glh/original/76412-root-hotel-setting-city-view.jpg',0),(22,17,'https://lh3.googleusercontent.com/p/AF1QipMguKmAp0EEBrzCCtfHmIoMqq5HOpsnNbwHeefr=s680-w680-h510',0),(23,18,'https://lh3.googleusercontent.com/p/AF1QipNeo4Kj5pLocfHK5O2MloETHtDhQ1ZJkzOcyje5=s1360-w1360-h1020',0),(24,19,'http://www.unaimagen.com',0);
/*!40000 ALTER TABLE `IMAGENES` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RESERVAS`
--

DROP TABLE IF EXISTS `RESERVAS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RESERVAS` (
  `reservas_id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `fecha_egreso` date NOT NULL,
  `hotel_id` int NOT NULL,
  `habilitado` tinyint(1) NOT NULL DEFAULT TRUE,
  PRIMARY KEY (`reservas_id`),
  KEY `hotel_id` (`hotel_id`),
  CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `HOTELES` (`hotel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RESERVAS`
--

LOCK TABLES `RESERVAS` WRITE;
/*!40000 ALTER TABLE `RESERVAS` DISABLE KEYS */;
INSERT INTO `RESERVAS` VALUES (1,'marcomasciulli96@gmail.com','2024-11-23','2024-11-22',16,0),(2,'marcomasciulli96@gmail.com','2024-11-17','2024-12-01',17,0),(3,'marcomasciulli96@gmail.com','2024-12-05','2024-10-12',18,0),(4,'marcomasciulli96@gmail.com','2024-11-23','2024-11-24',16,0),(5,'marcomasciulli96@gmail.com','2024-11-23','2024-11-24',16,0),(6,'marcomasciulli96@gmail.com','2024-11-24','2024-11-30',17,0),(7,'marcomasciulli96@gmail.com','2024-11-24','2024-11-23',16,0);
/*!40000 ALTER TABLE `RESERVAS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SERVICIOS`
--

DROP TABLE IF EXISTS `SERVICIOS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SERVICIOS` (
  `servicio_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `descripcion` text,
  `url_imagen` text,
  `ubicacion` varchar(100) NOT NULL,
  `habilitado` tinyint(1) NOT NULL DEFAULT TRUE,
  `categoria` varchar(100) NOT NULL,
  PRIMARY KEY (`servicio_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SERVICIOS`
--

LOCK TABLES `SERVICIOS` WRITE;
/*!40000 ALTER TABLE `SERVICIOS` DISABLE KEYS */;
INSERT INTO `SERVICIOS` VALUES (6,'Servicio de prueba','Una descripcion','http://www.unaImagen.com','Una ubicacion',0),(7,'Otro servicio','una descripcion\n','http://www.unaImagen.com','Una ubicacion',0);
/*!40000 ALTER TABLE `SERVICIOS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USUARIOS`
--

DROP TABLE IF EXISTS `USUARIOS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `USUARIOS` (
  `usuario_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contraseña` varchar(100) NOT NULL,
  `habilitado` tinyint(1) NOT NULL DEFAULT TRUE,
  PRIMARY KEY (`usuario_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USUARIOS`
--

LOCK TABLES `USUARIOS` WRITE;
/*!40000 ALTER TABLE `USUARIOS` DISABLE KEYS */;
/*!40000 ALTER TABLE `USUARIOS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `USUARIO_SERVICIOS`
--

DROP TABLE IF EXISTS `USUARIO_SERVICIOS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `USUARIO_SERVICIOS` (
  `servicio_id` int NOT NULL,
  `reserva_id` int NOT NULL,
  PRIMARY KEY (`servicio_id`,`reserva_id`),
  KEY `servicio_id` (`servicio_id`),
  KEY `reserva_id` (`reserva_id`),
  CONSTRAINT `USUARIO_SERVICIOS_ibfk_2` FOREIGN KEY (`servicio_id`) REFERENCES `SERVICIOS` (`servicio_id`),
  CONSTRAINT `USUARIO_SERVICIOS_ibfk_3` FOREIGN KEY (`reserva_id`) REFERENCES `RESERVAS` (`reservas_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `USUARIO_SERVICIOS`
--

LOCK TABLES `USUARIO_SERVICIOS` WRITE;
/*!40000 ALTER TABLE `USUARIO_SERVICIOS` DISABLE KEYS */;
/*!40000 ALTER TABLE `USUARIO_SERVICIOS` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-24 10:53:49
