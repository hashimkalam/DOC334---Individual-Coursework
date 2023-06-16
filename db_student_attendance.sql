-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 17, 2022 at 09:40 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_student_attendance`
--

-- --------------------------------------------------------

--
-- Table structure for table `keeping_track`
--

CREATE TABLE `keeping_track` (
  `studentNo` int(10) NOT NULL,
  `date` varchar(24) NOT NULL,
  `attendance` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `keeping_track`
--

INSERT INTO `keeping_track` (`studentNo`, `date`, `attendance`) VALUES
(1234, '8/15/2021', 'Present'),
(4321, '8/15/2021', 'Present'),
(1241, '8/15/2021', 'Absent'),
(2143, '8/15/2021', 'Present'),
(2131, '8/15/2021', 'Absent');

-- --------------------------------------------------------

--
-- Table structure for table `student_info`
--

CREATE TABLE `student_info` (
  `studentNo` int(10) NOT NULL,
  `fName` varchar(18) NOT NULL,
  `lName` varchar(18) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_info`
--

INSERT INTO `student_info` (`studentNo`, `fName`, `lName`) VALUES
(4321, 'Malik', 'Zak'),
(1241, 'Nial', 'Hor'),
(2143, 'Larry', 'Khan'),
(2131, 'Nazim', 'Kalm');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
