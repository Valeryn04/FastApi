-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-10-2025 a las 02:30:35
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

--
-- Volcado de datos para la tabla `atributo`
--

INSERT INTO `atributo` (`id_atributo`, `nombre`, `descripcion`, `create_date`, `update_date`) VALUES
(3, 'tipo_piel', 'Nivel del 1 al 6 según Fitzpatrick para medir sensibilidad solar del paciente.', '2025-10-09 23:43:56', '2025-10-09 23:48:28'),
(4, 'antecedentes_dermatologicos', 'Condiciones previas como acné u otras afecciones de piel del paciente.', '2025-10-09 23:43:56', '2025-10-09 23:48:21'),
(5, 'alergias', 'Sustancias o medicamentos que provocan reacción al paciente.', '2025-10-09 23:43:56', '2025-10-09 23:43:56'),
(6, 'ultimo_diagnostico', 'Último diagnóstico emitido por el sistema o el médico del paciente.', '2025-10-09 23:43:56', '2025-10-09 23:48:06'),
(7, 'cedula_profesional', 'Número de licencia médica del doctor.', '2025-10-09 23:45:13', '2025-10-09 23:45:13'),
(8, 'horario_atencion', 'Horarios en los que el doctor atiende consultas.', '2025-10-09 23:45:13', '2025-10-09 23:45:13'),
(9, 'num_pacientes_atendidos', 'Cantidad de pacientes atendidos por el doctor.', '2025-10-09 23:45:13', '2025-10-09 23:47:52'),
(10, 'especialidad', 'Rama médica o subespecialidad del doctor.', '2025-10-09 23:45:13', '2025-10-09 23:45:13');

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
-- Estructura de tabla para la tabla `modulo_permisos`
--

CREATE TABLE `modulo_permisos` (
  `id` int(11) NOT NULL,
  `id_modulo_fk` int(11) NOT NULL,
  `id_permiso_fk` int(11) NOT NULL,
  `nombre_funcionalidad` varchar(100) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `modulo_permisos`
--

INSERT INTO `modulo_permisos` (`id`, `id_modulo_fk`, `id_permiso_fk`, `nombre_funcionalidad`, `created_at`, `updated_at`) VALUES
(1, 1, 1, 'Crear Usuario', '2025-10-10 20:07:32', '2025-10-10 20:49:43');

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
-- Estructura de tabla para la tabla `rol_modulo_permisos`
--

CREATE TABLE `rol_modulo_permisos` (
  `id` int(11) NOT NULL,
  `id_rol_fk` int(11) NOT NULL,
  `id_modulo_permiso_fk` int(11) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol_modulo_permisos`
--

INSERT INTO `rol_modulo_permisos` (`id`, `id_rol_fk`, `id_modulo_permiso_fk`, `created_at`, `updated_at`) VALUES
(1, 1, 1, '2025-10-10 20:07:46', '2025-10-10 20:07:46');

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

--
-- Volcado de datos para la tabla `usuarioatributo`
--

INSERT INTO `usuarioatributo` (`id_usuario_atributo`, `id_usuario`, `id_atributo`, `valor`, `create_date`, `update_date`) VALUES
(1, 12, 3, 'Tipo II', '2025-10-10 00:27:19', '2025-10-10 00:27:19'),
(2, 12, 4, 'Acné leve', '2025-10-10 00:27:19', '2025-10-10 00:27:19'),
(3, 12, 5, 'Ninguna', '2025-10-10 00:27:19', '2025-10-10 00:27:19'),
(4, 12, 6, 'Dermatitis leve', '2025-10-10 00:27:19', '2025-10-10 00:27:19');

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
(11, 'sa', '$2b$12$k96gTbgvNDolzni96k.G7eqd7c.Txn6bl6u6CPfxPCepFCUSb3wwK', 'Wisisn', 'La W', 'CC', '10567890122', '2000-05-12', 'M', '3004567890', 'extraterrestze@example.com', 1, 'Cra 45 #67-12', 2, '2025-10-08 23:25:35', '2025-10-08 23:25:35'),
(12, 'paciente01', '$2b$12$q3UpR5vOVi3vxn8XJSRrze1qjRMVnm.jZfS/UWghoMCS4SLPg98zm', 'Juan', 'Pérez', 'CC', '1234567890', '1990-05-12', 'M', '3005557777', 'juan.perez@example.com', 1, 'Calle 45 #12-30', 2, '2025-10-10 00:27:19', '2025-10-10 00:27:19');

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
ALTER TABLE `modulos`
  ADD PRIMARY KEY (`id_modulo`);


--
-- Indices de la tabla `modulo_permisos`
--
ALTER TABLE `modulo_permisos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uk_modulo_permiso` (`id_modulo_fk`,`id_permiso_fk`),
  ADD KEY `id_permiso_fk` (`id_permiso_fk`);

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
-- Indices de la tabla `rol_modulo_permisos`
--
ALTER TABLE `rol_modulo_permisos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `uk_rol_funcionalidad` (`id_rol_fk`,`id_modulo_permiso_fk`),
  ADD KEY `id_modulo_permiso_fk` (`id_modulo_permiso_fk`);

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
  MODIFY `id_atributo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `modulos`
--
ALTER TABLE `modulos`
  MODIFY `id_modulo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `modulo_permisos`
--
ALTER TABLE `modulo_permisos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

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
-- AUTO_INCREMENT de la tabla `rol_modulo_permisos`
--
ALTER TABLE `rol_modulo_permisos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `usuarioatributo`
--
ALTER TABLE `usuarioatributo`
  MODIFY `id_usuario_atributo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `modulo_permisos`
--
ALTER TABLE `modulo_permisos`
  ADD CONSTRAINT `modulo_permisos_ibfk_1` FOREIGN KEY (`id_modulo_fk`) REFERENCES `modulos` (`id_modulo`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `modulo_permisos_ibfk_2` FOREIGN KEY (`id_permiso_fk`) REFERENCES `permisos` (`id_permiso`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `rol_modulo_permisos`
--
ALTER TABLE `rol_modulo_permisos`
  ADD CONSTRAINT `rol_modulo_permisos_ibfk_1` FOREIGN KEY (`id_rol_fk`) REFERENCES `roles` (`id_rol`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `rol_modulo_permisos_ibfk_2` FOREIGN KEY (`id_modulo_permiso_fk`) REFERENCES `modulo_permisos` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

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