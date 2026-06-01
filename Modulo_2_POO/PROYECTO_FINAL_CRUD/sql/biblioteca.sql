-- ============================================
-- CREACIÓN BASE DE DATOS
-- ============================================

DROP DATABASE IF EXISTS biblioteca_db;
CREATE DATABASE biblioteca_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE biblioteca_db;

-- ============================================
-- TABLA ROLES
-- ============================================

CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- ============================================
-- TABLA USUARIOS
-- ============================================

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol_id INT NOT NULL,
    FOREIGN KEY (rol_id) REFERENCES roles(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

-- ============================================
-- TABLA CATEGORIAS
-- ============================================

CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

-- ============================================
-- TABLA LIBROS (TABLA PRINCIPAL)
-- ============================================

CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- ============================================
-- TABLA PRESTAMOS (TABLA INTERMEDIA)
-- ============================================

CREATE TABLE prestamos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    libro_id INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (libro_id) REFERENCES libros(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- ============================================
-- DATOS INICIALES
-- ============================================

-- ROLES
INSERT INTO roles (nombre) VALUES
('ADMIN'),
('USUARIO');

-- USUARIOS AQUÍ ESTABA EL ERRROR
INSERT INTO usuarios (username, password, rol_id) VALUES
('admin', 'scrypt:32768:8:1$QTiNaVgWoBoescas$a0ba6770365ac573895e904b3e48728171a9e823680c8cd3169b73ffa0bd0af6464d4d3797e49e28c139fe1021b86cfb69f2b016b1793b695a042cf4d4363032', 1),
('pepe', 'scrypt:32768:8:1$KzAqXZ6TSxF3cqXc$0340b8cb9f2b2d3cb590bc7f6184abc2cf795efd9d97f7a17253c354548d970f90581513ec62a6dcca3c545a033f798aff3bf4da3987b5a0d7e806823cfac005', 2),
('ana', 'scrypt:32768:8:1$juTxnk74xjicruy8$6ac4436d037ac596e2ea282609f5a1147e13c0aa1a2671764c72d676cc2a809748eb36ffa611c243dd5240a5cfa63392f8fd93b898eb80fcc9ea465039a90874', 2);

-- CATEGORIAS
INSERT INTO categorias (nombre) VALUES
('Novela'),
('Ciencia'),
('Historia'),
('Cocina');

-- LIBROS
INSERT INTO libros (titulo, autor, categoria_id) VALUES
('Guia de telefonos', 'Varios autores', 1),
('Paginas amarillas', 'Varios autores', 2),
('Manual de historia del derecho español', 'Alfonso Garcia Gallo', 3),
('Cocina para todos', 'Carlos Arquiñano', 4);

-- PRESTAMOS
INSERT INTO prestamos (usuario_id, libro_id, fecha_inicio, fecha_fin) VALUES
(2, 1, '2026-05-01', NULL),
(3, 2, '2026-05-02', '2026-05-10');
