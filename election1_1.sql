-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost dsdsdsd
-- Generation Time: Mar 04, 2025 at 11:27 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `election1`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `name` varchar(50) NOT NULL,
  `psw` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`name`, `psw`) VALUES
('admin', '11');

-- --------------------------------------------------------

--
-- Table structure for table `booth`
--

CREATE TABLE `booth` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `ward` varchar(50) NOT NULL,
  `loc` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `booth`
--

INSERT INTO `booth` (`id`, `name`, `ward`, `loc`, `address`, `phone`) VALUES
(1, 'sample', '1', 'trichy', 'trichy', '7904461600');

-- --------------------------------------------------------

--
-- Table structure for table `boothslip`
--

CREATE TABLE `boothslip` (
  `id` int(10) NOT NULL auto_increment,
  `vname` varchar(100) NOT NULL,
  `vid` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `village` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `tal` varchar(100) NOT NULL,
  `wardno` varchar(100) NOT NULL,
  `boothname` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `boothslip`
--

INSERT INTO `boothslip` (`id`, `vname`, `vid`, `address`, `gender`, `village`, `district`, `tal`, `wardno`, `boothname`, `location`) VALUES
(1, 'sam', 'RTR433071', 'trichy', 'male', 'karumalai', 'Trichy', 'manapparai', '1', 'sample', 'trichy');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `id` int(50) NOT NULL auto_increment,
  `uname` varchar(100) NOT NULL,
  `ctype` varchar(100) NOT NULL,
  `details` varchar(1000) NOT NULL,
  `status` varchar(100) NOT NULL,
  `comstatus` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`id`, `uname`, `ctype`, `details`, `status`, `comstatus`) VALUES
(2, 'sundar', 'crime', 'sample', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `emp`
--

CREATE TABLE `emp` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `age` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `quali` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `psw` varchar(50) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `emp`
--

INSERT INTO `emp` (`id`, `name`, `gender`, `age`, `email`, `phone`, `quali`, `address`, `psw`) VALUES
(1, 'sundar', 'male', '24', 'sundarv06@gmail.com', '7904461600', 'trichy', 'trichy', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `newvoter`
--

CREATE TABLE `newvoter` (
  `id` int(50) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `dob` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `quali` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  `ward` varchar(50) NOT NULL,
  `idp` varchar(50) NOT NULL,
  `fname` varchar(50) NOT NULL,
  `status` varchar(10) NOT NULL,
  `city` varchar(100) NOT NULL,
  `village` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `tal` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `newvoter`
--

INSERT INTO `newvoter` (`id`, `name`, `gender`, `dob`, `email`, `phone`, `quali`, `address`, `ward`, `idp`, `fname`, `status`, `city`, `village`, `district`, `tal`) VALUES
(2, 'sam', 'male', '2025-03-05', 'sundarv06@gmail.com', '7904461600', '10th', 'trichy', '1', 'img_2.jpg', 'kumar', 'Accepted', 'trichy', 'karumalai', 'Trichy', 'manapparai');

-- --------------------------------------------------------

--
-- Table structure for table `voters`
--

CREATE TABLE `voters` (
  `id` int(10) NOT NULL auto_increment,
  `name` varchar(50) NOT NULL,
  `vid` varchar(50) NOT NULL,
  `ward` varchar(50) NOT NULL,
  `booth` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `address` varchar(100) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `voters`
--

