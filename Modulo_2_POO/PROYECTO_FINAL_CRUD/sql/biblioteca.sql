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

-- USUARIOS (passwords en texto plano por ahora, luego los cifrarás en Flask)
INSERT INTO usuarios (username, password, rol_id) VALUES
('admin', 'admin123', 1),
('juan', 'juan123', 2),
('maria', 'maria123', 2);

-- CATEGORIAS
INSERT INTO categorias (nombre) VALUES
('Novela'),
('Ciencia'),
('Historia'),
('Cocina');

-- LIBROS
INSERT INTO libros (titulo, autor, categoria_id) VALUES
('Cien años de soledad', 'Gabriel García Márquez', 1),
('Breve historia del tiempo', 'Stephen Hawking', 2),
('Manual de historia del derecho español', 'Alfonso Garcia Gallo', 3),
('Cocina para todos', 'Carlos Arquiñano', 4);

-- PRESTAMOS
INSERT INTO prestamos (usuario_id, libro_id, fecha_inicio, fecha_fin) VALUES
(2, 1, '2026-05-01', NULL),
(3, 2, '2026-05-02', '2026-05-10');
