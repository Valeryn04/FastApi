-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-10-2025 a las 06:44:42
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `dermaia`
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
(3, 'departamento_gestion', 'Departamento o área de trabajo', '2025-10-15 19:37:54', '2025-10-16 03:55:05'),
(4, 'supervisor', 'Booleano si tiene supervisor', '2025-10-15 19:37:54', '2025-10-16 03:55:19'),
(5, 'codigo_empleado', 'Identificador interno del empleado', '2025-10-15 19:37:54', '2025-10-16 03:55:41'),
(6, 'fecha_ingreso', 'Fecha de inicio de relación laboral', '2025-10-15 19:37:54', '2025-10-16 03:56:12'),
(7, 'cedula_profesional', 'Número de licencia médica del doctor.', '2025-10-15 19:37:54', '2025-10-15 19:37:54'),
(8, 'especialidad\n', 'Rama médica o subespecialidad del doctor.', '2025-10-15 19:37:54', '2025-10-16 03:52:59'),
(9, 'horario_atencion', 'Horarios del doctor', '2025-10-15 19:37:54', '2025-10-16 03:52:54'),
(10, 'certificados y diplomas', 'Adicionales', '2025-10-15 19:37:54', '2025-10-16 03:56:39'),
(11, 'tipo_sangre', 'Tipo de sangre y factor', '2025-10-16 03:53:53', '2025-10-16 03:56:57'),
(12, 'alergias', 'Condiciones previas como acné u otras afecciones de piel del paciente.', '2025-10-16 03:53:53', '2025-10-16 03:54:38'),
(13, 'contacto_emergencia', 'Nombre y télefono contacto', '2025-10-16 03:53:53', '2025-10-16 03:57:19'),
(14, 'tipo_piel', 'Nivel del 1 al 6 según Fitzpatrick para medir sensibilidad solar del paciente.', '2025-10-16 03:53:53', '2025-10-16 03:54:18');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulos`
--

CREATE TABLE `modulos` (
  `id_modulo` int(11) NOT NULL,
  `nombre_modulo` varchar(50) NOT NULL,
  `url` varchar(150) DEFAULT NULL,
  `icono` varchar(100) DEFAULT 'bi bi-circle',
  `descripcion` varchar(255) DEFAULT NULL,
  `create_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_date` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `modulos`
--

INSERT INTO `modulos` (`id_modulo`, `nombre_modulo`, `url`, `icono`, `descripcion`, `create_date`, `update_date`) VALUES
(1, 'Dashboard', '/admin', 'bi bi-speedometer2', 'Panel principal del sistema', '2025-10-15 19:37:54', '2025-10-15 19:37:54'),
(2, 'Reportes', '/admin/reportes', 'bi bi-calendar-event', 'Gestión de citas médicas', '2025-10-15 19:37:54', '2025-10-16 00:39:40'),
(3, 'Usuarios', '/admin/usuarios', 'bi bi-people', 'Gestión de usuarios del sistema', '2025-10-15 19:37:54', '2025-10-15 19:37:54'),
(4, 'Permisos', '/admin/permisos', 'bi bi-shield-lock', 'Gestión de permisos y roles', '2025-10-15 19:37:54', '2025-10-15 19:37:54');

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
(1, 3, 1, 'Crear Usuario', '2025-10-15 19:37:54', '2025-10-15 19:42:37'),
(2, 3, 3, 'Actualizar usuario', '2025-10-15 22:42:31', '2025-10-15 22:42:31'),
(3, 4, 1, 'Crear Permisos', '2025-10-16 00:31:41', '2025-10-16 00:31:41'),
(4, 4, 3, 'Actualizar permisos', '2025-10-16 00:31:41', '2025-10-16 00:31:41'),
(5, 3, 2, 'Consultar Usuario', '2025-10-16 00:37:47', '2025-10-16 00:37:47'),
(6, 3, 4, 'Eliminar Usuario', '2025-10-16 00:37:47', '2025-10-16 00:37:47'),
(7, 3, 5, 'Desactivar Usuario', '2025-10-16 00:37:47', '2025-10-16 00:37:47'),
(8, 1, 2, 'Consultar Dashboard', '2025-10-16 00:37:47', '2025-10-16 00:37:47'),
(9, 4, 2, 'Consultar Permisos', '2025-10-16 00:37:47', '2025-10-16 00:37:47'),
(10, 4, 4, 'Eliminar Permisos', '2025-10-16 00:37:47', '2025-10-16 00:37:47'),
(11, 4, 5, 'Desactivar Permisos', '2025-10-16 00:37:47', '2025-10-16 00:37:47'),
(12, 2, 1, 'Crear Reportes', '2025-10-16 00:41:30', '2025-10-16 00:41:30'),
(13, 2, 3, 'Actualizar Reportes', '2025-10-16 00:41:30', '2025-10-16 00:41:30'),
(14, 2, 2, 'Consultar Reportes', '2025-10-16 00:41:30', '2025-10-16 00:41:30'),
(15, 2, 4, 'Eliminar Reportes', '2025-10-16 00:41:30', '2025-10-16 00:41:30'),
(16, 2, 5, 'Desactivar Reportes', '2025-10-16 00:41:30', '2025-10-16 00:41:30');

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
(1, 'crear', 'Permite crear registros', '2025-10-15 19:37:54', '2025-10-15 19:37:54'),
(2, 'consultar', 'Permite ver registros', '2025-10-15 19:37:54', '2025-10-15 19:37:54'),
(3, 'actualizar', 'Permite modificar registros', '2025-10-15 19:37:54', '2025-10-15 19:37:54'),
(4, 'eliminar', 'Permite eliminar registros', '2025-10-15 19:37:54', '2025-10-15 19:37:54'),
(5, 'desactivar', 'Permite desactivar registros sin eliminarlos', '2025-10-15 19:37:54', '2025-10-15 19:37:54');

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
(1, 'Administrador', 'Perfil Administrador', '2025-10-15 19:37:54', '2025-10-16 04:42:17'),
(2, 'Asistente', 'Perfil Asistente', '2025-10-15 19:37:54', '2025-10-16 03:32:50'),
(3, 'Medico', 'Acceso al módulo médico para la gestión de pacientes y diagnósticos.', '2025-10-15 19:37:54', '2025-10-15 19:37:54'),
(4, 'Paciente', 'Acceso al portal del paciente para citas y consulta de historial.', '2025-10-15 19:37:54', '2025-10-15 19:37:54'),
(5, 'SuperAdmin', 'Perfil SuperAdmin', '2025-10-16 00:39:03', '2025-10-16 03:33:08');

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
(82, 2, 8, '2025-10-16 03:32:50', '2025-10-16 03:32:50'),
(83, 2, 9, '2025-10-16 03:32:50', '2025-10-16 03:32:50'),
(84, 2, 13, '2025-10-16 03:32:50', '2025-10-16 03:32:50'),
(85, 2, 12, '2025-10-16 03:32:50', '2025-10-16 03:32:50'),
(86, 2, 16, '2025-10-16 03:32:50', '2025-10-16 03:32:50'),
(87, 2, 15, '2025-10-16 03:32:50', '2025-10-16 03:32:50'),
(88, 2, 5, '2025-10-16 03:32:50', '2025-10-16 03:32:50'),
(89, 5, 8, '2025-10-16 03:33:08', '2025-10-16 03:33:08'),
(90, 5, 4, '2025-10-16 03:33:08', '2025-10-16 03:33:08'),
(91, 5, 9, '2025-10-16 03:33:08', '2025-10-16 03:33:08'),
(92, 5, 3, '2025-10-16 03:33:08', '2025-10-16 03:33:08'),
(93, 5, 11, '2025-10-16 03:33:08', '2025-10-16 03:33:08'),
(94, 5, 10, '2025-10-16 03:33:08', '2025-10-16 03:33:08'),
(95, 5, 2, '2025-10-16 03:33:08', '2025-10-16 03:33:08'),
(96, 5, 5, '2025-10-16 03:33:08', '2025-10-16 03:33:08'),
(97, 5, 1, '2025-10-16 03:33:08', '2025-10-16 03:33:08'),
(98, 5, 7, '2025-10-16 03:33:08', '2025-10-16 03:33:08'),
(99, 5, 6, '2025-10-16 03:33:08', '2025-10-16 03:33:08'),
(108, 1, 8, '2025-10-16 04:42:17', '2025-10-16 04:42:17'),
(109, 1, 4, '2025-10-16 04:42:17', '2025-10-16 04:42:17'),
(110, 1, 9, '2025-10-16 04:42:17', '2025-10-16 04:42:17'),
(111, 1, 3, '2025-10-16 04:42:17', '2025-10-16 04:42:17'),
(112, 1, 14, '2025-10-16 04:42:17', '2025-10-16 04:42:17'),
(113, 1, 2, '2025-10-16 04:42:17', '2025-10-16 04:42:17'),
(114, 1, 5, '2025-10-16 04:42:17', '2025-10-16 04:42:17'),
(115, 1, 1, '2025-10-16 04:42:17', '2025-10-16 04:42:17'),
(116, 1, 7, '2025-10-16 04:42:17', '2025-10-16 04:42:17');

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
(1, 3, 3, 'TI/Sistemas', '2025-10-15 19:37:54', '2025-10-16 03:58:36'),
(2, 3, 4, 'Si', '2025-10-15 19:37:54', '2025-10-16 03:58:36'),
(3, 3, 5, 'A001', '2025-10-15 19:37:54', '2025-10-16 03:58:36'),
(4, 3, 6, '2020-10-10', '2025-10-15 19:37:54', '2025-10-16 03:58:36'),
(5, 1, 3, 'A002', '2025-10-16 04:00:46', '2025-10-16 04:01:32'),
(6, 2, 5, '003', '2025-10-16 04:02:50', '2025-10-16 04:02:50'),
(7, 2, 6, '2020-08-07', '2025-10-16 04:02:50', '2025-10-16 04:02:50');

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
(1, 'Asistente1', '$2b$12$isUbfdj0Ckc/CjWLzm8Ci.ztMDgEHcKGbU0tRPCpsHXguoiXi1Z5C', 'Asistente 1', 'Asistente', 'CC', '1001920351', '1993-02-18', 'M', '300356214', 'Asistente@gmail.com', 1, 'TV 52#37-95', 2, '2025-10-15 19:37:54', '2025-10-16 04:20:03'),
(2, 'admin2', '$2b$12$k96gTbgvNDolzni96k.G7eqd7c.Txn6bl6u6CPfxPCepFCUSb3wwK', 'Admin 2', 'Prueba', 'CC', '10567890122', '2000-05-12', 'M', '3004567890', 'prueba@example.com', 0, 'Cra 45 #67-12', 1, '2025-10-15 19:37:54', '2025-10-16 04:20:11'),
(3, 'admin', '$2b$12$h5MpkTn7zHNLYFUjlw7lcuaTkdd6gvWBn2sBh/BmEqLCoIFWTijw2', 'Administrador', 'Principal', 'CC', '1000000001', '1990-01-01', 'M', '3000000000', 'admin@sistema.com', 1, 'Oficina Central', 1, '2025-10-15 19:37:54', '2025-10-16 03:58:36'),
(4, 'superadmin', '$2b$12$q3UpR5vOVi3vxn8XJSRrze1qjRMVnm.jZfS/UWghoMCS4SLPg98zm', 'Super', 'admin', 'CC', '1234567890', '1990-05-12', 'M', '3005557777', 'juan.perez@example.com', 1, 'Calle 45 #12-30', 5, '2025-10-15 19:37:54', '2025-10-16 04:25:59'),
(13, 'admin3', '$2b$12$X9wxgxFj/C2pQZKLIpcIle9UPsW21q11ZCr042tsOeOg4vDA7Wdiy', 'admin3', 'admin3', 'CC', '1061551666', '2000-05-04', 'M', '3008276522', 'admin3@gmail.com', 1, 'xsjjdhddn', 2, '2025-10-15 22:37:59', '2025-10-16 04:21:08');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `atributo`
--
ALTER TABLE `atributo`
  ADD PRIMARY KEY (`id_atributo`);

--
-- Indices de la tabla `modulos`
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
  MODIFY `id_atributo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `modulos`
--
ALTER TABLE `modulos`
  MODIFY `id_modulo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `modulo_permisos`
--
ALTER TABLE `modulo_permisos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id_permiso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_rol` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `rol_modulo_permisos`
--
ALTER TABLE `rol_modulo_permisos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=117;

--
-- AUTO_INCREMENT de la tabla `usuarioatributo`
--
ALTER TABLE `usuarioatributo`
  MODIFY `id_usuario_atributo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
