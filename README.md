# Seguridad Informatica - Ilan

Una aplicación web desarrollada con Flask que implementa algoritmos de compresión y criptografía, para la Codificación de Huffman y el Método DES.

## 📋 Descripción

Resolución de los algoritmos en seguridad informática:

1. **Codificación de Huffman**: Un algoritmo de compresión sin pérdida que utiliza códigos de longitud variable para representar símbolos, asignando códigos más cortos a los símbolos más frecuentes.

2. **Cifrado DES (Data Encryption Standard)**: Un algoritmo de cifrado simétrico que opera en bloques de 64 bits con una clave de 56 bits.

La aplicación proporciona una interfaz intuitiva para comprimir texto utilizando el algoritmo de Huffman, visualizar el árbol de Huffman generado, y cifrar/descifrar texto utilizando el algoritmo DES.

## ✨ Características

- **Compresión de Huffman**:
  - Compresión de texto en tiempo real
  - Visualización del árbol de Huffman
  - Estadísticas de compresión (tamaño original, tamaño comprimido, ratio de compresión)
  - Visualización de los códigos generados para cada carácter

- **Cifrado DES**:
  - Cifrado y descifrado de texto
  - Implementación en modo ECB (Electronic Codebook)
  - Visualización del texto cifrado en formato Base64

- **Interfaz de Usuario**:
  - Diseño responsivo con Bootstrap 5
  - Navegación intuitiva
  - Visualizaciones claras de los resultados

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Librerías**:
  - `pycryptodome` para implementación de DES
  - Bibliotecas estándar de Python para la implementación de Huffman

## 📦 Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/ilanangelesrodriguez/SecureCompressionApp.git
   cd SecureCompressionApp
