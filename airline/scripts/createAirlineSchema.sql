## create airline DB

DROP DATABASE `airline`;
CREATE DATABASE `airline`;

USE airline;

CREATE TABLE `L_AIRLINE_ID` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_AIRLINE_ID_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_AIRPORT` (
  `Code` char(3) NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_AIRPORT_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_AIRPORT_ID` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_AIRPORT_ID_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_AIRPORT_SEQ_ID` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_AIRPORT_SEQ_ID_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_CANCELLATION` (
  `Code` char(1) NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_CANCELLATION_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_CITY_MARKET_ID` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_CITY_MARKET_ID_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_DEPARRBLK` (
  `Code` char(9) NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_DEPARRBLK_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_DISTANCE_GROUP_250` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_DISTANCE_GROUP_250_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_DIVERSIONS` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_DIVERSIONS_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_MONTHS` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_MONTHS_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_ONTIME_DELAY_GROUPS` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_ONTIME_DELAY_GROUPS_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_QUARTERS` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_QUARTERS_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_STATE_ABR_AVIATION` (
  `Code` char(2) NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_STATE_ABR_AVIATION_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_STATE_FIPS` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_STATE_FIPS_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_UNIQUE_CARRIERS` (
  `Code` varchar(255) NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_UNIQUE_CARRIERS_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_WEEKDAYS` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_WEEKDAYS_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_WORLD_AREA_CODES` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_WORLD_AREA_CODES_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

CREATE TABLE `L_YESNO_RESP` (
  `Code` int NOT NULL,
  `Description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Code`),
  UNIQUE KEY `L_YESNO_RESP_Code_key` (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE `On_Time_On_Time_Performance_2016_1` (
  `Year` int DEFAULT NULL,
  `Quarter` int DEFAULT NULL,
  `Month` int DEFAULT NULL,
  `DayofMonth` int DEFAULT NULL,
  `DayOfWeek` int DEFAULT NULL,
  `FlightDate` date DEFAULT NULL,
  `UniqueCarrier` varchar(255) DEFAULT 'NULL',
  `AirlineID` int NOT NULL,
  `Carrier` char(2) DEFAULT NULL,
  `TailNum` varchar(6) DEFAULT NULL,
  `FlightNum` int DEFAULT NULL,
  `OriginAirportID` int DEFAULT NULL,
  `OriginAirportSeqID` int DEFAULT NULL,
  `OriginCityMarketID` int DEFAULT NULL,
  `Origin` char(3) DEFAULT NULL,
  `OriginCityName` varchar(34) DEFAULT NULL,
  `OriginState` char(2) DEFAULT NULL,
  `OriginStateFips` int DEFAULT NULL,
  `OriginStateName` varchar(46) DEFAULT NULL,
  `OriginWac` int DEFAULT NULL,
  `DestAirportID` int DEFAULT NULL,
  `DestAirportSeqID` int DEFAULT NULL,
  `DestCityMarketID` int DEFAULT NULL,
  `Dest` char(3) DEFAULT NULL,
  `DestCityName` varchar(34) DEFAULT NULL,
  `DestState` char(2) DEFAULT NULL,
  `DestStateFips` int DEFAULT NULL,
  `DestStateName` varchar(46) DEFAULT NULL,
  `DestWac` int DEFAULT NULL,
  `CRSDepTime` int DEFAULT NULL,
  `DepTime` int DEFAULT NULL,
  `DepDelay` decimal(65,2) DEFAULT NULL,
  `DepDelayMinutes` float DEFAULT NULL,
  `DepDel15` int DEFAULT NULL,
  `DepartureDelayGroups` int DEFAULT NULL,
  `DepTimeBlk` char(9) DEFAULT NULL,
  `TaxiOut` float DEFAULT NULL,
  `WheelsOff` int DEFAULT NULL,
  `WheelsOn` int DEFAULT NULL,
  `TaxiIn` float DEFAULT NULL,
  `CRSArrTime` int DEFAULT NULL,
  `ArrTime` int DEFAULT NULL,
  `ArrDelay` decimal(65,2) DEFAULT NULL,
  `ArrDelayMinutes` float DEFAULT NULL,
  `ArrDel15` int DEFAULT NULL,
  `ArrivalDelayGroups` int DEFAULT NULL,
  `ArrTimeBlk` char(9) DEFAULT NULL,
  `Cancelled` int DEFAULT NULL,
  `CancellationCode` char(1) DEFAULT NULL,
  `Diverted` int DEFAULT NULL,
  `CRSElapsedTime` float DEFAULT NULL,
  `ActualElapsedTime` float DEFAULT NULL,
  `AirTime` float DEFAULT NULL,
  `Flights` float DEFAULT NULL,
  `Distance` float DEFAULT NULL,
  `DistanceGroup` int DEFAULT NULL,
  `CarrierDelay` decimal(65,2) DEFAULT NULL,
  `WeatherDelay` decimal(65,2) DEFAULT NULL,
  `NASDelay` decimal(65,2) DEFAULT NULL,
  `SecurityDelay` decimal(65,2) DEFAULT NULL,
  `LateAircraftDelay` decimal(65,2) DEFAULT NULL,
  `FirstDepTime` decimal(65,2) DEFAULT NULL,
  `TotalAddGTime` decimal(65,2) DEFAULT NULL,
  `LongestAddGTime` decimal(65,2) DEFAULT NULL,
  `DivAirportLandings` int DEFAULT NULL,
  `DivReachedDest` decimal(65,2) DEFAULT NULL,
  `DivActualElapsedTime` decimal(65,2) DEFAULT NULL,
  `DivArrDelay` decimal(65,2) DEFAULT NULL,
  `DivDistance` decimal(65,2) DEFAULT NULL,
  `Div1Airport` char(3) DEFAULT NULL,
  `Div1AirportID` int DEFAULT NULL,
  `Div1AirportSeqID` int DEFAULT NULL,
  `Div1WheelsOn` decimal(65,2) DEFAULT NULL,
  `Div1TotalGTime` decimal(65,2) DEFAULT NULL,
  `Div1LongestGTime` decimal(65,2) DEFAULT NULL,
  `Div1WheelsOff` decimal(65,2) DEFAULT NULL,
  `Div1TailNum` varchar(6) DEFAULT NULL,
  `Div2Airport` char(3) DEFAULT NULL,
  `Div2AirportID` int DEFAULT NULL,
  `Div2AirportSeqID` int DEFAULT NULL,
  `Div2WheelsOn` decimal(65,2) DEFAULT NULL,
  `Div2TotalGTime` decimal(65,2) DEFAULT NULL,
  `Div2LongestGTime` decimal(65,2) DEFAULT NULL,
  KEY `On_Time_On_Time_Performance_2016_1_DivAirportLandings_fkey` (`DivAirportLandings`),
  KEY `On_Time_On_Time_Performance_2016_1_DepartureDelayGroups_fkey` (`DepartureDelayGroups`),
  KEY `On_Time_On_Time_Performance_2016_1_ArrivalDelayGroups_fkey` (`ArrivalDelayGroups`),
  KEY `On_Time_On_Time_Performance_2016_1_Div1AirportSeqID_fkey` (`Div1AirportSeqID`),
  KEY `On_Time_On_Time_Performance_2016_1_Div2AirportSeqID_fkey` (`Div2AirportSeqID`),
  KEY `On_Time_On_Time_Performance_2016_1_Div1AirportID_fkey` (`Div1AirportID`),
  KEY `On_Time_On_Time_Performance_2016_1_Div2AirportID_fkey` (`Div2AirportID`),
  KEY `On_Time_On_Time_Performance_2016_1_Diverted_fkey` (`Diverted`),
  KEY `On_Time_On_Time_Performance_2016_1_Cancelled_fkey` (`Cancelled`),
  KEY `On_Time_On_Time_Performance_2016_1_ArrDel15_fkey` (`ArrDel15`),
  KEY `On_Time_On_Time_Performance_2016_1_DepDel15_fkey` (`DepDel15`),
  KEY `On_Time_On_Time_Performance_2016_1_CancellationCode_fkey` (`CancellationCode`),
  KEY `On_Time_On_Time_Performance_2016_1_DepTimeBlk_fkey` (`DepTimeBlk`),
  KEY `On_Time_On_Time_Performance_2016_1_DestState_fkey` (`DestState`),
  KEY `On_Time_On_Time_Performance_2016_1_Dest_fkey` (`Dest`),
  KEY `On_Time_On_Time_Performance_2016_1_OriginState_fkey` (`OriginState`),
  KEY `On_Time_On_Time_Performance_2016_1_Origin_fkey` (`Origin`),
  KEY `On_Time_On_Time_Performance_2016_1_UniqueCarrier_fkey` (`UniqueCarrier`),
  KEY `On_Time_On_Time_Performance_2016_1_DestStateFips_fkey` (`DestStateFips`),
  KEY `On_Time_On_Time_Performance_2016_1_OriginStateFips_fkey` (`OriginStateFips`),
  KEY `On_Time_On_Time_Performance_2016_1_OriginWac_fkey` (`OriginWac`),
  KEY `On_Time_On_Time_Performance_2016_1_DestWac_fkey` (`DestWac`),
  KEY `On_Time_On_Time_Performance_2016_1_DayOfWeek_fkey` (`DayOfWeek`),
  KEY `On_Time_On_Time_Performance_2016_1_DistanceGroup_fkey` (`DistanceGroup`),
  KEY `On_Time_On_Time_Performance_2016_1_Quarter_fkey` (`Quarter`),
  KEY `On_Time_On_Time_Performance_2016_1_Month_fkey` (`Month`),
  KEY `On_Time_On_Time_Performance_2016_1_DestCityMarketID_fkey` (`DestCityMarketID`),
  KEY `On_Time_On_Time_Performance_2016_1_OriginCityMarketID_fkey` (`OriginCityMarketID`),
  KEY `On_Time_On_Time_Performance_2016_1_DestAirportSeqID_fkey` (`DestAirportSeqID`),
  KEY `On_Time_On_Time_Performance_2016_1_OriginAirportSeqID_fkey` (`OriginAirportSeqID`),
  KEY `On_Time_On_Time_Performance_2016_1_DestAirportID_fkey` (`DestAirportID`),
  KEY `On_Time_On_Time_Performance_2016_1_OriginAirportID_fkey` (`OriginAirportID`),
  KEY `On_Time_On_Time_Performance_2016_1_AirlineID_fkey` (`AirlineID`),
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_AirlineID_fkey` FOREIGN KEY (`AirlineID`) REFERENCES `L_AIRLINE_ID` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_ArrDel15_fkey` FOREIGN KEY (`ArrDel15`) REFERENCES `L_YESNO_RESP` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_ArrivalDelayGroups_fkey` FOREIGN KEY (`ArrivalDelayGroups`) REFERENCES `L_ONTIME_DELAY_GROUPS` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_CancellationCode_fkey` FOREIGN KEY (`CancellationCode`) REFERENCES `L_CANCELLATION` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_Cancelled_fkey` FOREIGN KEY (`Cancelled`) REFERENCES `L_YESNO_RESP` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DayOfWeek_fkey` FOREIGN KEY (`DayOfWeek`) REFERENCES `L_WEEKDAYS` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DepartureDelayGroups_fkey` FOREIGN KEY (`DepartureDelayGroups`) REFERENCES `L_ONTIME_DELAY_GROUPS` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DepDel15_fkey` FOREIGN KEY (`DepDel15`) REFERENCES `L_YESNO_RESP` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DepTimeBlk_fkey` FOREIGN KEY (`DepTimeBlk`) REFERENCES `L_DEPARRBLK` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_Dest_fkey` FOREIGN KEY (`Dest`) REFERENCES `L_AIRPORT` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DestAirportID_fkey` FOREIGN KEY (`DestAirportID`) REFERENCES `L_AIRPORT_ID` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DestAirportSeqID_fkey` FOREIGN KEY (`DestAirportSeqID`) REFERENCES `L_AIRPORT_SEQ_ID` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DestCityMarketID_fkey` FOREIGN KEY (`DestCityMarketID`) REFERENCES `L_CITY_MARKET_ID` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DestState_fkey` FOREIGN KEY (`DestState`) REFERENCES `L_STATE_ABR_AVIATION` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DestStateFips_fkey` FOREIGN KEY (`DestStateFips`) REFERENCES `L_STATE_FIPS` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DestWac_fkey` FOREIGN KEY (`DestWac`) REFERENCES `L_WORLD_AREA_CODES` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DistanceGroup_fkey` FOREIGN KEY (`DistanceGroup`) REFERENCES `L_DISTANCE_GROUP_250` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_Div1AirportID_fkey` FOREIGN KEY (`Div1AirportID`) REFERENCES `L_AIRPORT_ID` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_Div1AirportSeqID_fkey` FOREIGN KEY (`Div1AirportSeqID`) REFERENCES `L_AIRPORT_SEQ_ID` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_Div2AirportID_fkey` FOREIGN KEY (`Div2AirportID`) REFERENCES `L_AIRPORT_ID` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_Div2AirportSeqID_fkey` FOREIGN KEY (`Div2AirportSeqID`) REFERENCES `L_AIRPORT_SEQ_ID` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_DivAirportLandings_fkey` FOREIGN KEY (`DivAirportLandings`) REFERENCES `L_DIVERSIONS` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_Diverted_fkey` FOREIGN KEY (`Diverted`) REFERENCES `L_YESNO_RESP` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_Month_fkey` FOREIGN KEY (`Month`) REFERENCES `L_MONTHS` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_Origin_fkey` FOREIGN KEY (`Origin`) REFERENCES `L_AIRPORT` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_OriginAirportID_fkey` FOREIGN KEY (`OriginAirportID`) REFERENCES `L_AIRPORT_ID` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_OriginAirportSeqID_fkey` FOREIGN KEY (`OriginAirportSeqID`) REFERENCES `L_AIRPORT_SEQ_ID` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_OriginCityMarketID_fkey` FOREIGN KEY (`OriginCityMarketID`) REFERENCES `L_CITY_MARKET_ID` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_OriginState_fkey` FOREIGN KEY (`OriginState`) REFERENCES `L_STATE_ABR_AVIATION` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_OriginStateFips_fkey` FOREIGN KEY (`OriginStateFips`) REFERENCES `L_STATE_FIPS` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_OriginWac_fkey` FOREIGN KEY (`OriginWac`) REFERENCES `L_WORLD_AREA_CODES` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_Quarter_fkey` FOREIGN KEY (`Quarter`) REFERENCES `L_QUARTERS` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `On_Time_On_Time_Performance_2016_1_UniqueCarrier_fkey` FOREIGN KEY (`UniqueCarrier`) REFERENCES `L_UNIQUE_CARRIERS` (`Code`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
