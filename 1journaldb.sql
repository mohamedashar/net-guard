-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 18, 2025 at 10:22 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1journaldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `UserName` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`UserName`, `Password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `newstb`
--

CREATE TABLE `newstb` (
  `id` bigint(20) NOT NULL auto_increment,
  `category` varchar(250) NOT NULL,
  `Title` varchar(250) NOT NULL,
  `Date` varchar(250) NOT NULL,
  `Keypoint` varchar(500) NOT NULL,
  `News` varchar(500) NOT NULL,
  `Image` varchar(500) NOT NULL,
  `Author` varchar(500) NOT NULL,
  `Status` varchar(500) NOT NULL,
  `time` varchar(50) NOT NULL,
  `location` varchar(500) NOT NULL,
  `video` varchar(100) NOT NULL,
  `amount` varchar(10) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `newstb`
--

INSERT INTO `newstb` (`id`, `category`, `Title`, `Date`, `Keypoint`, `News`, `Image`, `Author`, `Status`, `time`, `location`, `video`, `amount`) VALUES
(1, 'Advertisement', 'job details', '2025-03-19', 'job', 'test', 'news.png', 'sample', 'Completed', '10.00', 'trichy', 'g8.jpg', '500'),
(2, 'Advertisement', 'sample job details', '2025-03-19', 'job', 'sample test', 'news.png', 'test', 'Completed', '10.00', 'trichy', 'news.png', '1000');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `id` int(50) NOT NULL auto_increment,
  `nid` varchar(10) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `amount` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL,
  `ctype` varchar(10) NOT NULL,
  `cardno` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`id`, `nid`, `uname`, `amount`, `date`, `ctype`, `cardno`) VALUES
(1, '1', 'sample', '500', '2025-03-18 15:42:34.874141', 'Visacard', '1234567899'),
(2, '2', 'test', '1000', '2025-03-18 15:49:17.730822', 'Visacard', '1234567899');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Phone` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserType` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`Name`, `Gender`, `Age`, `Email`, `Phone`, `Address`, `UserType`, `UserName`, `Password`) VALUES
('san', 'male', '20', 'sundarv06@gmail.com', '9486365535', 'no', 'Author', 'san', 'san'),
('san', 'male', '20', 'san@gmail.com', '9486365535', 'no 6 trichy', 'Reviewer', 'san', 'san'),
('nandha', 'male', '20', 'nandha@gmail.com', '8124602893', 'no ', 'Author', 'nandha', 'nandha'),
('nandha', 'male', '20', 'nandha@gmail.com', '8124602893', 'no ', 'Editor', 'nandha', 'nandha'),
('nandha', 'male', '20', 'nandha@gmail.com', '8124602893', 'no ', 'Reviewer', 'nandha', 'nandha'),
('ragul', 'male', '20', 'ragul@gmail.com', '9600357839', 'dgh', 'Author', 'ragul', 'ragul'),
('sundar', 'male', '32', 'sundarv06@gmail.com', '7904461600', 'trichy', '', 'admin', 'admin'),
('sundar', 'male', '24', 'mani@gmail.com', '7904461601', 'trichy', '', 'mani', '1234'),
('sundar', 'male', '32', 'sundarv06@gmail.com', '7904461600', 'trichy', '', 'admin', 'admin'),
('Anbu', 'male', '30', 'anbu@gmail.com', '9876543210', 'asdf', '', 'anbu', 'anbu'),
('sam', 'male', '22', 'test@gmail.com', '7904461601', 'trichy', '', 'admin34', 'admin34'),
('sundar', 'male', '32', 'sundarv06@gmail.com', '7904461600', 'trichy', 'Advertisement', 'sundar', 'sundar'),
('sam', 'male', '32', 'test@gmail.com', '7904461600', 'trichy', 'Marketing', 'sam', 'sam'),
('sample', 'male', '32', 'sundarv06@gmail.com', '7904461600', 'trichy', 'Production ', 'sample', 'sample'),
('pandiyan', 'male', '32', 'sundarv06@gmail.com', '7904461600', 'trichy', 'Accounts ', 'pandiyan', 'pandiyan');

-- --------------------------------------------------------

--
-- Table structure for table `userregtb`
--

CREATE TABLE `userregtb` (
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Phone` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userregtb`
--

INSERT INTO `userregtb` (`Name`, `Gender`, `Age`, `Email`, `Phone`, `Address`, `UserName`, `Password`) VALUES
('sample', 'male', '32', 'sundarv06@gmail.com', '7904461600', 'trichy', 'sample', 'sample'),
('test', 'male', '32', 'sundarv06@gmail.com', '7904461600', 'trichy', 'test', 'test');
