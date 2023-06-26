-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 26, 2023 at 04:42 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_team`
--

-- --------------------------------------------------------

--
-- Table structure for table `author`
--

CREATE TABLE `author` (
  `author_id` char(10) NOT NULL,
  `author_name` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `author`
--

INSERT INTO `author` (`author_id`, `author_name`) VALUES
('01', 'Agus Ardi'),
('02', 'Hussain Abdillah'),
('03', 'Arwinda'),
('04', 'Mirashanti'),
('05', 'Fajar Suryawan');

-- --------------------------------------------------------

--
-- Table structure for table `author_write_book`
--

CREATE TABLE `author_write_book` (
  `book_id` char(10) NOT NULL,
  `author_id` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `author_write_book`
--

INSERT INTO `author_write_book` (`book_id`, `author_id`) VALUES
('01', '01'),
('02', '02'),
('03', '02'),
('04', '03'),
('05', '03'),
('06', '04'),
('07', '04'),
('08', '04'),
('09', '05'),
('10', '05'),
('11', '05'),
('12', '05'),
('13', '01'),
('14', '03'),
('15', '01');

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `book_id` char(10) NOT NULL,
  `book_title` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`book_id`, `book_title`) VALUES
('01', 'Sebaiknya Diselesaikan'),
('02', 'Filosofi UMS'),
('03', 'Sistem Basis Data 101'),
('04', 'Algoritma dan Pemrograman: expert'),
('05', 'Data Mining for Beginners'),
('06', 'Java Script for Script Kiddie'),
('07', 'Pemrograman Web Berbasis Framework'),
('08', 'Sistem Operasi'),
('09', 'Principles of Physics'),
('10', 'Calculus I'),
('11', 'Calculus II'),
('12', 'Calculus III'),
('13', 'Hukum Perdata'),
('14', 'Chemistry'),
('15', 'Discrete Math');

-- --------------------------------------------------------

--
-- Table structure for table `loan`
--

CREATE TABLE `loan` (
  `book_id` char(10) NOT NULL,
  `member_id` char(10) NOT NULL,
  `loan_id` int(11) NOT NULL,
  `loan_date` date NOT NULL,
  `return_date` date DEFAULT NULL,
  `due_return_date` date NOT NULL,
  `lateness_tax` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `loan`
--

INSERT INTO `loan` (`book_id`, `member_id`, `loan_id`, `loan_date`, `return_date`, `due_return_date`, `lateness_tax`) VALUES
('01', '01', 1, '2023-01-01', '2023-01-14', '2023-01-15', 0),
('02', '02', 2, '2023-02-05', '2023-02-22', '2023-02-20', 5000),
('03', '03', 3, '2023-03-10', '2023-03-26', '2023-03-25', 10000),
('04', '04', 4, '2023-04-15', NULL, '2023-05-01', NULL),
('05', '05', 5, '2023-05-20', '2023-06-04', '2023-06-05', NULL),
('06', '01', 6, '2023-06-25', NULL, '2023-07-10', NULL),
('07', '02', 7, '2023-07-30', '2023-08-15', '2023-08-14', 15000),
('08', '03', 8, '2023-08-10', '2023-08-24', '2023-08-25', NULL),
('09', '04', 9, '2023-09-15', NULL, '2023-09-30', NULL),
('10', '05', 10, '2023-10-20', '2023-11-06', '2023-11-05', 20000),
('12', '01', 11, '2023-05-25', NULL, '2023-07-11', NULL),
('05', '02', 12, '2023-01-25', NULL, '2023-03-11', NULL),
('12', '02', 13, '2023-06-24', NULL, '2023-07-01', NULL),
('07', '03', 14, '2023-06-24', NULL, '2023-07-01', NULL),
('13', '03', 15, '2023-06-25', NULL, '2023-07-02', NULL),
('14', '01', 16, '2023-06-25', NULL, '2023-07-02', NULL),
('02', '01', 17, '2023-06-25', '2023-06-25', '2023-07-02', 0),
('03', '01', 18, '2023-06-25', '2023-06-25', '2023-07-02', 0),
('15', '01', 19, '2023-06-25', NULL, '2023-07-02', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `member`
--

CREATE TABLE `member` (
  `member_id` char(10) NOT NULL,
  `member_name` varchar(250) DEFAULT NULL,
  `member_email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `member`
--

INSERT INTO `member` (`member_id`, `member_name`, `member_email`) VALUES
('01', 'Ardiansyah Nh', 'agusadi@example.com'),
('02', 'Budi Santoso', 'budisantoso@example.com'),
('03', 'Citra Wardhani', 'citrawardhani@example.com'),
('04', 'Dewi Sari', 'dewisari@example.com'),
('05', 'Eko Prasetyo', 'ekoprasetyo@example.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `author`
--
ALTER TABLE `author`
  ADD PRIMARY KEY (`author_id`);

--
-- Indexes for table `author_write_book`
--
ALTER TABLE `author_write_book`
  ADD PRIMARY KEY (`book_id`,`author_id`),
  ADD KEY `book_has_author_FKIndex1` (`book_id`),
  ADD KEY `book_has_author_FKIndex2` (`author_id`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `loan`
--
ALTER TABLE `loan`
  ADD PRIMARY KEY (`loan_id`),
  ADD KEY `book_has_member_FKIndex1` (`book_id`),
  ADD KEY `book_has_member_FKIndex2` (`member_id`);

--
-- Indexes for table `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`member_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `loan`
--
ALTER TABLE `loan`
  MODIFY `loan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
