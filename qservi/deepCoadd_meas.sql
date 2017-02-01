/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
DROP TABLE IF EXISTS `deepCoadd_meas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deepCoadd_meas` (
`base_ClassificationExtendedness_flag` boolean NULL,
`ext_shapeHSM_HsmShapeRegauss_flag` boolean NULL,
`modelfit_CModel_fluxSigma` double NULL,
`modelfit_CModel_flux` double NULL,
`modelfit_CModel_flux_inner` double NULL,
`filter` char(5) NULL,
`coord_ra` double NULL,
`detect_isPrimary` boolean NULL,
`base_ClassificationExtendedness_value` double NULL,
`coord_dec` double NULL,
`id` bigint(20) NULL,
`modelfit_CModel_mag` double NULL,
`modelfit_CModel_magSigma` double NULL,
`x_Src` double NULL,
`y_Src` double NULL,
`coord_ra_deg` double NULL,
`coord_dec_deg` double NULL,
PRIMARY KEY (`id`),
KEY `IDX_filter` (`filter`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
