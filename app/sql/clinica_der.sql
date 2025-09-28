-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-09-2025 a las 19:36:19
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `clinica_der`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `atributo`
--

CREATE TABLE `atributo` (
  `idAtributo` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulo`
--

CREATE TABLE `modulo` (
  `idModulo` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulorol`
--

CREATE TABLE `modulorol` (
  `idModuloRol` int(11) NOT NULL,
  `idRol` int(11) NOT NULL,
  `idModulo` int(11) NOT NULL,
  `estado` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `idRol` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`idRol`, `nombre`, `descripcion`) VALUES
(1, 'administrador', NULL),
(2, 'paciente', NULL),
(3, 'doctor', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarioatributo`
--

CREATE TABLE `usuarioatributo` (
  `idUsuarioAtributo` int(11) NOT NULL,
  `idUsuario` int(11) NOT NULL,
  `idAtributo` int(11) NOT NULL,
  `valor` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `idUsuario` int(11) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `nombreCompleto` varchar(100) NOT NULL,
  `tipoDocumento` varchar(20) DEFAULT NULL,
  `numeroDocumento` varchar(20) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `sexo` varchar(1) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `direccion` varchar(150) DEFAULT NULL,
  `idRol` int(11) NOT NULL,
  `estado` int(11) DEFAULT NULL,
  `fechaRegistro` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`idUsuario`, `usuario`, `contrasena`, `nombreCompleto`, `tipoDocumento`, `numeroDocumento`, `fechaNacimiento`, `sexo`, `telefono`, `email`, `direccion`, `idRol`, `estado`, `fechaRegistro`) VALUES
(1, 'jernesto21', 'hola123', 'Ernesto Santa Rosa', 'C.C', '102453652', '1995-09-05', 'M', '3003652412', 'ernesto@gmail.com', 'Carrera 52 # 24-58 Las margaritas', 2, 1, '2025-09-28 17:21:39'),
(2, 'jperez', 'clave123', 'Juan Pérez', 'C.C', '1002345678', '1990-04-12', 'M', '3012345678', 'juanperez@gmail.com', 'Calle 45 # 12-34 San José', 2, 1, '2025-09-28 17:22:34'),
(3, 'mlopera', 'pass456', 'María López', 'C.C', '1019876543', '1988-11-23', 'F', '3023456789', 'marialopez@gmail.com', 'Carrera 10 # 8-20 El Prado', 3, 1, '2025-09-28 17:22:35'),
(4, 'cfernandez', 'qwerty789', 'Carlos Fernández', 'T.I', '1145236987', '2000-06-15', 'M', '3034567890', 'carlosf@gmail.com', 'Barrio Las Palmas, Cra 21 # 15-45', 2, 1, '2025-09-28 17:22:35'),
(5, 'andreaq', 'secure321', 'Andrea Quintero', 'C.C', '1023456987', '1993-02-18', 'F', '3045678901', 'andreaq@gmail.com', 'Urbanización Villa Campestre, Torre 3', 3, 1, '2025-09-28 17:22:35'),
(6, 'juan123', '$2b$12$a4iBGfzQSlE/vtoBf6akb.1ItnH2YmUKKZ3prgLiXmTumtTwff1gi', 'Juan Pérez', 'C.C', '1020304050', '1990-05-15', 'M', '3001234567', 'juan@example.com', 'Calle 123 #45-67', 2, 1, '2025-09-28 17:34:59'),
(7, 'testHash', '$2b$12$5/8HEcylKvoAYlyRVvv.jOGu1WY2GGWLuPyDkLhkC//x/De6GUrWK', 'Juan Pérez', 'C.C', '1020304050', '1990-05-15', 'M', '3001234567', 'hash@example.com', 'Calle 123 #45-67', 2, 1, '2025-09-28 17:35:42');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `atributo`
--
ALTER TABLE `atributo`
  ADD PRIMARY KEY (`idAtributo`);

--
-- Indices de la tabla `modulo`
--
ALTER TABLE `modulo`
  ADD PRIMARY KEY (`idModulo`);

--
-- Indices de la tabla `modulorol`
--
ALTER TABLE `modulorol`
  ADD PRIMARY KEY (`idModuloRol`),
  ADD KEY `idRol` (`idRol`),
  ADD KEY `idModulo` (`idModulo`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`idRol`);

--
-- Indices de la tabla `usuarioatributo`
--
ALTER TABLE `usuarioatributo`
  ADD PRIMARY KEY (`idUsuarioAtributo`),
  ADD KEY `idUsuario` (`idUsuario`),
  ADD KEY `idAtributo` (`idAtributo`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`idUsuario`),
  ADD UNIQUE KEY `usuario` (`usuario`),
  ADD KEY `idRol` (`idRol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `atributo`
--
ALTER TABLE `atributo`
  MODIFY `idAtributo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `modulo`
--
ALTER TABLE `modulo`
  MODIFY `idModulo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `modulorol`
--
ALTER TABLE `modulorol`
  MODIFY `idModuloRol` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `idRol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuarioatributo`
--
ALTER TABLE `usuarioatributo`
  MODIFY `idUsuarioAtributo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `idUsuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `modulorol`
--
ALTER TABLE `modulorol`
  ADD CONSTRAINT `modulorol_ibfk_1` FOREIGN KEY (`idRol`) REFERENCES `rol` (`idRol`),
  ADD CONSTRAINT `modulorol_ibfk_2` FOREIGN KEY (`idModulo`) REFERENCES `modulo` (`idModulo`);

--
-- Filtros para la tabla `usuarioatributo`
--
ALTER TABLE `usuarioatributo`
  ADD CONSTRAINT `usuarioatributo_ibfk_1` FOREIGN KEY (`idUsuario`) REFERENCES `usuarios` (`idUsuario`),
  ADD CONSTRAINT `usuarioatributo_ibfk_2` FOREIGN KEY (`idAtributo`) REFERENCES `atributo` (`idAtributo`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`idRol`) REFERENCES `rol` (`idRol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
