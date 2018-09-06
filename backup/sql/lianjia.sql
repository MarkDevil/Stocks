-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.6.24 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 导出 lianjia 的数据库结构
CREATE DATABASE IF NOT EXISTS `lianjia` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `lianjia`;


-- 导出  表 lianjia.house 结构
CREATE TABLE IF NOT EXISTS `house` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL COMMENT '标题',
  `region` varchar(50) DEFAULT NULL COMMENT '区',
  `building` varchar(30) DEFAULT NULL COMMENT '小区',
  `struct` varchar(10) DEFAULT NULL COMMENT '格局',
  `housesize` varchar(10) DEFAULT NULL COMMENT '面积',
  `floor` varchar(50) DEFAULT NULL COMMENT '楼层',
  `syear` varchar(50) DEFAULT NULL COMMENT '建成时间',
  `price` varchar(50) DEFAULT NULL COMMENT '价格',
  `url_addr` varchar(50) DEFAULT NULL COMMENT '房源链接地址',
  `houseinfo` varchar(50) DEFAULT NULL COMMENT '房屋信息',
  `posinfo` varchar(50) DEFAULT NULL COMMENT '位置信息',
  PRIMARY KEY (`id`),
  UNIQUE KEY `titlehouse` (`title`,`houseinfo`),
  KEY `posinfo` (`posinfo`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='链家二手房数据库';

-- 数据导出被取消选择。
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
