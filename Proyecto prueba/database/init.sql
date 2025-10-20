CREATE DATABASE IF NOT EXISTS sgssi_db;
USE sgssi_db;

-- Tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    dni VARCHAR(10) UNIQUE NOT NULL,
    telefono VARCHAR(9) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de elementos (ejemplo: discos de vinilo)
CREATE TABLE elementos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    artista VARCHAR(100) NOT NULL,
    año INT NOT NULL,
    genero VARCHAR(50) NOT NULL,
    descripcion TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Datos de ejemplo
INSERT INTO elementos (titulo, artista, año, genero, descripcion) VALUES
('Thriller', 'Michael Jackson', 1982, 'Pop', 'Álbum más vendido de la historia'),
('The Dark Side of the Moon', 'Pink Floyd', 1973, 'Rock progresivo', 'Obra maestra del rock progresivo');