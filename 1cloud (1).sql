-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 13, 2025 at 08:04 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1cloud`
--

-- --------------------------------------------------------

--
-- Table structure for table `admintb`
--

CREATE TABLE `admintb` (
  `UserName` varchar(10) NOT NULL,
  `Password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admintb`
--

INSERT INTO `admintb` (`UserName`, `Password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `attacker1`
--

CREATE TABLE `attacker1` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(10) NOT NULL,
  `ipaddress` varchar(50) NOT NULL,
  `date` varchar(20) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `attacker1`
--

INSERT INTO `attacker1` (`id`, `name`, `ipaddress`, `date`) VALUES
(1, 'DESKTOP-LU', '192.168.1.4', '2023-01-30 11:27:50.'),
(2, 'DESKTOP-LU', '192.168.1.4', '2023-01-30 11:28:43.'),
(3, 'DESKTOP-LU', '192.168.1.4', '2023-01-30 12:35:32.'),
(4, 'DESKTOP-LU', '192.168.1.4', '2023-01-30 12:36:36.'),
(5, 'DESKTOP-LU', '192.168.1.4', '2023-01-30 12:37:05.'),
(6, 'DESKTOP-LU', '192.168.1.10', '2023-03-15 11:14:33.'),
(7, 'DESKTOP-LU', '192.168.1.10', '2023-03-15 11:27:11.'),
(8, 'DESKTOP-LU', '192.168.1.5', '2023-04-16 15:44:29.'),
(9, 'DESKTOP-LU', '192.168.1.5', '2023-04-16 15:48:43.'),
(10, 'DESKTOP-LU', '192.168.1.21', '2025-01-27 17:35:39.'),
(11, 'DESKTOP-LU', '192.168.1.14', '2025-03-01 15:14:24.'),
(12, 'DESKTOP-LU', '192.168.1.47', '2025-03-06 11:37:21.'),
(13, 'DESKTOP-LU', '192.168.1.13', '2025-03-13 10:05:20.'),
(14, 'DESKTOP-LU', '192.168.1.12', '2025-03-13 13:08:41.');

-- --------------------------------------------------------

--
-- Table structure for table `file`
--

CREATE TABLE `file` (
  `id` int(10) NOT NULL auto_increment,
  `fname` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `username` varchar(50) NOT NULL,
  `filename` varchar(200) NOT NULL,
  `size` varchar(200) NOT NULL,
  `pubkey` varchar(10) NOT NULL,
  `prkey` varchar(10) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `file`
--

INSERT INTO `file` (`id`, `fname`, `details`, `username`, `filename`, `size`, `pubkey`, `prkey`) VALUES
(1, 'Smart home services', 'TEST', 's123', 'pic1.jpg', '7347', 'SGGUK0', 'J3NM34'),
(2, 'das', 'testsample', 's123', 'election1 (1).sql', '5253', 'VCANHR', 'YRQ1Z1'),
(3, 'sample', 'test', 'pandiyan', 'adminhome.jsp', '5253', '8R7HK7', 'CKJPE8');

-- --------------------------------------------------------

--
-- Table structure for table `imgpass`
--

CREATE TABLE `imgpass` (
  `uid` varchar(50) NOT NULL,
  `img` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `imgpass`
--

INSERT INTO `imgpass` (`uid`, `img`) VALUES
('1', '00.png'),
('1', '01.png'),
('1', '02.png'),
('1', '10.png'),
('1', '11.png'),
('1', '12.png'),
('1', '20.png'),
('1', '21.png'),
('1', '22.png'),
('2', '00.png'),
('2', '01.png'),
('2', '02.png'),
('2', '10.png'),
('2', '11.png'),
('2', '12.png'),
('2', '20.png'),
('2', '21.png'),
('2', '22.png'),
('3', '00.png'),
('3', '01.png'),
('3', '02.png'),
('3', '10.png'),
('3', '11.png'),
('3', '12.png'),
('3', '20.png'),
('3', '21.png'),
('3', '22.png'),
('4', '00.png'),
('4', '01.png'),
('4', '02.png'),
('4', '10.png'),
('4', '11.png'),
('4', '12.png'),
('4', '20.png'),
('4', '21.png'),
('4', '22.png'),
('5', '00.png'),
('5', '01.png'),
('5', '02.png'),
('5', '10.png'),
('5', '11.png'),
('5', '12.png'),
('5', '20.png'),
('5', '21.png'),
('5', '22.png'),
('6', '00.png'),
('6', '01.png'),
('6', '02.png'),
('6', '10.png'),
('6', '11.png'),
('6', '12.png'),
('6', '20.png'),
('6', '21.png'),
('6', '22.png');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pnumber` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `UserName` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `name`, `gender`, `age`, `email`, `pnumber`, `address`, `UserName`, `Password`) VALUES
(5, 'sundar', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', '798654'),
(6, 'admin', 'male', '24', 'sundarv06@gmail.com', '9840234119', 'trichy', 'admin', '12345'),
(7, 'admin', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'admin', 'admin'),
(8, 's123', 'male', '30', 'sundarv06@gmail.com', '9840234119', 'trichy', 's123', 's123'),
(9, 'mani', 'male', '21', 'yogisamcore5@gmail.com', '8890334522', 'trichy', 'user', 'user'),
(10, 'pandiyan', 'male', '30', 'sundarv06@gmail.com', '7904461600', 'trichy', 'pandiyan', 'pandiyan');

-- --------------------------------------------------------

--
-- Table structure for table `userfilerequest`
--

CREATE TABLE `userfilerequest` (
  `id` int(50) NOT NULL auto_increment,
  `fid` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `details` varchar(100) NOT NULL,
  `oname` varchar(100) NOT NULL,
  `filename` varchar(100) NOT NULL,
  `prkey` varchar(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `email` varchar(500) NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `userfilerequest`
--

INSERT INTO `userfilerequest` (`id`, `fid`, `fname`, `details`, `oname`, `filename`, `prkey`, `uname`, `email`, `status`) VALUES
(1, '1', 'Smart home services', 'TEST', 's123', 'pic1.jpg', 'J3NM34', 'mani', 'sundarv06@gmail.com', 'Accepted'),
(2, '3', 'sample', 'test', 'pandiyan', 'adminhome.jsp', 'CKJPE8', 'sam', 'sundarv06@gmail.com', 'Accepted'),
(3, '2', 'das', 'testsample', 's123', 'election1 (1).sql', 'YRQ1Z1', 'sam', 'sundarv06@gmail.com', 'Waiting');

-- --------------------------------------------------------

--
-- Table structure for table `userregtb`
--

CREATE TABLE `userregtb` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(100) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `age` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `pnumber` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `UserName` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `userregtb`
--

INSERT INTO `userregtb` (`id`, `name`, `gender`, `age`, `email`, `pnumber`, `address`, `UserName`, `Password`) VALUES
(10, 'mani', 'male', '21', 'sundarv06@gmail.com', '8890334522', 'trichy', 'mani', 'mani'),
(11, 'sam', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'sam', 'sam');
