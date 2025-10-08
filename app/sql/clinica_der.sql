-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-10-2025 a las 01:53:21
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
  `id_atributo` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `create_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulorol`
--

CREATE TABLE `modulorol` (
  `id_modulo_rol` int(11) NOT NULL,
  `id_rol` int(11) NOT NULL,
  `id_modulo` int(11) NOT NULL,
  `estado` tinyint(1) DEFAULT 1,
  `create_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `modulorol`
--

INSERT INTO `modulorol` (`id_modulo_rol`, `id_rol`, `id_modulo`, `estado`, `create_date`, `update_date`) VALUES
(1, 1, 1, 1, '2025-10-08 19:22:26', '2025-10-08 19:22:26'),
(2, 1, 2, 1, '2025-10-08 19:22:26', '2025-10-08 19:22:26'),
(3, 2, 2, 1, '2025-10-08 19:22:45', '2025-10-08 19:22:45');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulos`
--

CREATE TABLE `modulos` (
  `id_modulo` int(11) NOT NULL,
  `nombre_modulo` varchar(50) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `create_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `modulos`
--

INSERT INTO `modulos` (`id_modulo`, `nombre_modulo`, `descripcion`, `create_date`, `update_date`) VALUES
(1, 'Usuarios', 'Gestión de usuarios del sistema', '2025-10-08 19:20:42', '2025-10-08 19:20:42'),
(2, 'Citas', 'Gestión de citas médicas', '2025-10-08 19:20:42', '2025-10-08 19:20:42');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permisos`
--

CREATE TABLE `permisos` (
  `id_permiso` int(11) NOT NULL,
  `nombre_permiso` varchar(50) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `permisos`
--

INSERT INTO `permisos` (`id_permiso`, `nombre_permiso`, `descripcion`, `created_at`, `updated_at`) VALUES
(1, 'crear', 'Permite crear registros', '2025-10-08 19:21:04', '2025-10-08 19:21:04'),
(2, 'consultar', 'Permite ver registros', '2025-10-08 19:21:04', '2025-10-08 19:21:04'),
(3, 'actualizar', 'Permite modificar registros', '2025-10-08 19:21:04', '2025-10-08 19:21:04'),
(4, 'eliminar', 'Permite eliminar registros', '2025-10-08 19:21:04', '2025-10-08 19:21:04'),
(5, 'desactivar', 'Permite desactivar registros sin eliminarlos', '2025-10-08 19:21:04', '2025-10-08 19:21:04');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `nombre_rol` varchar(50) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `create_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id_rol`, `nombre_rol`, `descripcion`, `create_date`, `update_date`) VALUES
(1, 'Administrador', 'Acceso total al sistema', '2025-10-08 19:20:23', '2025-10-08 19:20:23'),
(2, 'Asistente', 'Acceso limitado a funciones de consulta', '2025-10-08 19:20:23', '2025-10-08 19:20:23');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol_permisos`
--

CREATE TABLE `rol_permisos` (
  `id_rol_permiso` int(11) NOT NULL,
  `id_modulo_rol` int(11) NOT NULL,
  `id_permiso` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol_permisos`
--

INSERT INTO `rol_permisos` (`id_rol_permiso`, `id_modulo_rol`, `id_permiso`, `created_at`, `updated_at`) VALUES
(1, 1, 1, '2025-10-08 19:23:15', '2025-10-08 19:23:15'),
(2, 2, 3, '2025-10-08 19:25:54', '2025-10-08 19:25:54'),
(3, 3, 2, '2025-10-08 19:26:15', '2025-10-08 19:26:15');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarioatributo`
--

CREATE TABLE `usuarioatributo` (
  `id_usuario_atributo` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_atributo` int(11) NOT NULL,
  `valor` varchar(255) DEFAULT NULL,
  `create_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `nombre` varchar(50) DEFAULT NULL,
  `apellido` varchar(50) NOT NULL,
  `tipo_documento` varchar(20) DEFAULT NULL,
  `numero_documento` varchar(20) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `sexo` varchar(1) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT 1,
  `direccion` varchar(150) DEFAULT NULL,
  `id_rol` int(11) NOT NULL,
  `create_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `usuario`, `contrasena`, `nombre`, `apellido`, `tipo_documento`, `numero_documento`, `fecha_nacimiento`, `sexo`, `telefono`, `email`, `estado`, `direccion`, `id_rol`, `create_date`, `update_date`) VALUES
(8, 'yandel150', '$2b$12$isUbfdj0Ckc/CjWLzm8Ci.ztMDgEHcKGbU0tRPCpsHXguoiXi1Z5C', 'Yandel', 'Extraterreste', 'CC', '1001920351', '1993-02-18', 'M', '300356214', 'yandel@gmail.com', 1, 'TV 52#37-95', 1, '2025-10-08 22:16:57', '2025-10-08 22:48:44'),
(11, 'sa', '$2b$12$k96gTbgvNDolzni96k.G7eqd7c.Txn6bl6u6CPfxPCepFCUSb3wwK', 'Wisisn', 'La W', 'CC', '10567890122', '2000-05-12', 'M', '3004567890', 'extraterrestze@example.com', 1, 'Cra 45 #67-12', 2, '2025-10-08 23:25:35', '2025-10-08 23:25:35');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `atributo`
--
ALTER TABLE `atributo`
  ADD PRIMARY KEY (`id_atributo`);

--
-- Indices de la tabla `modulorol`
--
ALTER TABLE `modulorol`
  ADD PRIMARY KEY (`id_modulo_rol`),
  ADD KEY `idRol` (`id_rol`),
  ADD KEY `idModulo` (`id_modulo`);

--
-- Indices de la tabla `modulos`
--
ALTER TABLE `modulos`
  ADD PRIMARY KEY (`id_modulo`);

--
-- Indices de la tabla `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`id_permiso`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `rol_permisos`
--
ALTER TABLE `rol_permisos`
  ADD PRIMARY KEY (`id_rol_permiso`),
  ADD UNIQUE KEY `unique_modulorol_permiso` (`id_modulo_rol`,`id_permiso`),
  ADD KEY `fk_permiso` (`id_permiso`);

--
-- Indices de la tabla `usuarioatributo`
--
ALTER TABLE `usuarioatributo`
  ADD PRIMARY KEY (`id_usuario_atributo`),
  ADD KEY `idUsuario` (`id_usuario`),
  ADD KEY `idAtributo` (`id_atributo`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `usuario` (`usuario`),
  ADD UNIQUE KEY `uq_email` (`email`),
  ADD UNIQUE KEY `uq_num_documento` (`numero_documento`),
  ADD KEY `id_rol` (`id_rol`) USING BTREE;

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `atributo`
--
ALTER TABLE `atributo`
  MODIFY `id_atributo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `modulorol`
--
ALTER TABLE `modulorol`
  MODIFY `id_modulo_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `modulos`
--
ALTER TABLE `modulos`
  MODIFY `id_modulo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id_permiso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `rol_permisos`
--
ALTER TABLE `rol_permisos`
  MODIFY `id_rol_permiso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `usuarioatributo`
--
ALTER TABLE `usuarioatributo`
  MODIFY `id_usuario_atributo` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `modulorol`
--
ALTER TABLE `modulorol`
  ADD CONSTRAINT `modulorol_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`),
  ADD CONSTRAINT `modulorol_ibfk_2` FOREIGN KEY (`id_modulo`) REFERENCES `modulos` (`id_modulo`);

--
-- Filtros para la tabla `rol_permisos`
--
ALTER TABLE `rol_permisos`
  ADD CONSTRAINT `fk_modulorol` FOREIGN KEY (`id_modulo_rol`) REFERENCES `modulorol` (`id_modulo_rol`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_permiso` FOREIGN KEY (`id_permiso`) REFERENCES `permisos` (`id_permiso`) ON DELETE CASCADE;

--
-- Filtros para la tabla `usuarioatributo`
--
ALTER TABLE `usuarioatributo`
  ADD CONSTRAINT `usuarioatributo_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`),
  ADD CONSTRAINT `usuarioatributo_ibfk_2` FOREIGN KEY (`id_atributo`) REFERENCES `atributo` (`id_atributo`);

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
