DROP TABLE IF EXISTS `deepCoadd_meas`;
CREATE TABLE `deepCoadd_meas` (
`base_ClassificationExtendedness_flag` boolean NOT NULL,
`coord_dec` float NOT NULL,
`patch` int(11) NOT NULL,
`filter` char(5) NOT NULL,
`coord_ra` float NOT NULL,
`detect_isPrimary` boolean NOT NULL,
`base_ClassificationExtendedness_value` float NOT NULL,
`tract` char(5) NOT NULL,
`ext_shapeHSM_HsmShapeRegauss_flag` boolean NOT NULL,
`id` int(11) NOT NULL,
`x_Src` float NOT NULL,
`y_Src` float NOT NULL,
`coord_ra_deg` float NOT NULL,
`coord_dec_deg` float NOT NULL,
PRIMARY KEY (`id`),
KEY `IDX_tract_patch_filter` (`tract`,`patch`,`filter`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
