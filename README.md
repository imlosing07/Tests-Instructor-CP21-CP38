# Tests - Instructor CP21-CP38

Este repositorio contiene una suite de pruebas automatizadas para la plataforma **TEAMMATES** utilizando Selenium WebDriver y pytest. Las pruebas están diseñadas para validar las funcionalidades del módulo de instructor en la aplicación web.

## 📋 Descripción General

El proyecto incluye 18 casos de prueba (CP21 a CP38) que cubren las principales funcionalidades del sistema TEAMMATES desde la perspectiva de un instructor, incluyendo:

- Gestión de cursos
- Administración de estudiantes
- Funciones de búsqueda
- Interacciones con la interfaz web

## 🏗️ Estructura del Proyecto

```text
tests/
├── conftest.py                 # Configuración de pytest y fixture del driver
├── requirements.txt            # Dependencias del proyecto
├── test_cp21.py               # CP21 - Crear curso estando logueado
├── test_cp22.py               # CP22 - [Funcionalidad específica]
├── test_cp23.py               # CP23 - [Funcionalidad específica]
├── test_cp24.py               # CP24 - [Funcionalidad específica]
├── test_cp25.py               # CP25 - [Funcionalidad específica]
├── test_cp26.py               # CP26 - [Funcionalidad específica]
├── test_cp27.py               # CP27 - [Funcionalidad específica]
├── test_cp28.py               # CP28 - [Funcionalidad específica]
├── test_cp29.py               # CP29 - [Funcionalidad específica]
├── test_cp30.py               # CP30 - Inscribir estudiante
├── test_cp31.py               # CP31 - [Funcionalidad específica]
├── test_cp32.py               # CP32 - [Funcionalidad específica]
├── test_cp33.py               # CP33 - [Funcionalidad específica]
├── test_cp34.py               # CP34 - [Funcionalidad específica]
├── test_cp35.py               # CP35 - [Funcionalidad específica]
├── test_cp36.py               # CP36 - [Funcionalidad específica]
├── test_cp37.py               # CP37 - [Funcionalidad específica]
├── test_cp38.py               # CP38 - Buscar combinado
├── capturas/                   # Directorio de evidencias
│   ├── entradas/              # Screenshots de estados iniciales
│   │   ├── CP21_entrada.png   # Captura antes de ejecutar CP21
│   │   ├── CP22_entrada.png   # Captura antes de ejecutar CP22
│   │   └── ...                # Capturas para CP23-CP38
│   └── salidas/               # Screenshots de resultados
│       ├── CP21_salida.png    # Captura después de ejecutar CP21
│       ├── CP22_salida.png    # Captura después de ejecutar CP22
│       └── ...                # Capturas para CP23-CP38
└── __pycache__/               # Archivos compilados de Python
```

## ⚙️ Configuración Técnica

### Dependencias

Las dependencias principales están definidas en `requirements.txt`:

- **selenium**: Framework para automatización de navegadores web
- **pytest**: Framework de testing para Python
- **webdriver-manager**: Gestión automática de drivers de navegador

### Configuración del Driver (conftest.py)

El archivo `conftest.py` contiene la configuración global de Selenium:

- **Navegador**: Google Chrome
- **Perfil de usuario**: Perfil personalizado en `C:/Users/Usuario/selenium-profile`
- **Opciones del navegador**:
  - Ventana maximizada
  - Deshabilitación de extensiones
  - Configuración para entornos sin interfaz gráfica
  - Tiempo de espera implícito: 10 segundos

## 🚀 Ejecución de Pruebas

### Prerrequisitos

1. Python 3.x instalado
2. Google Chrome instalado
3. Dependencias instaladas:

```bash
pip install -r requirements.txt
```

### Comandos de Ejecución

```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar una prueba específica
pytest test_cp21.py

# Ejecutar con salida detallada
pytest -v

# Ejecutar un rango de pruebas
pytest test_cp21.py test_cp22.py test_cp23.py
```

## 📸 Sistema de Capturas

Cada caso de prueba implementa un sistema de documentación visual:

### Capturas de Entrada (`capturas/entradas/`)

- Documentan el estado inicial de la aplicación
- Se toman antes de ejecutar las acciones principales del test
- Formato: `CP##_entrada.png`

### Capturas de Salida (`capturas/salidas/`)

- Documentan el resultado final después de ejecutar el test
- Validan visualmente que las acciones se completaron correctamente
- Formato: `CP##_salida.png`

## 🎯 Casos de Prueba Específicos

### CP21 - Crear Curso Estando Logueado

- **Objetivo**: Validar la creación de un nuevo curso
- **Datos de prueba**:
  - ID del curso: "CS2024-S2"
  - Nombre del curso: "Software Engineering II"

### CP30 - Inscribir Estudiante

- **Objetivo**: Validar la inscripción de estudiantes en un curso
- **Funcionalidades**: Manejo de tablas dinámicas, inserción de datos

### CP38 - Búsqueda Combinada

- **Objetivo**: Validar búsqueda avanzada con múltiples criterios
- **Datos de prueba**: Combinación de nombre, grupo tutorial, equipo y email

## 🌐 Plataforma de Pruebas

- **URL Base**: `https://teammates-hormiga-1.uc.r.appspot.com`
- **Módulo**: Instructor
- **Funcionalidades principales**:
  - Home del instructor
  - Gestión de cursos
  - Administración de estudiantes
  - Sistema de búsqueda

## 📝 Convenciones de Código

- **Nomenclatura**: `test_cp##.py` donde ## es el número del caso de prueba
- **Función principal**: `test_[descripción_funcionalidad](driver)`
- **Documentación**: Prints descriptivos para cada paso de la prueba
- **Esperas**: Uso de `time.sleep()` para estabilizar la ejecución
- **Capturas**: Automáticas en puntos clave del flujo

## 🔧 Mantenimiento

### Archivos Compilados

El directorio `__pycache__/` contiene archivos compilados de Python que se generan automáticamente. Estos archivos no requieren modificación manual.

### Actualización de Dependencias

Para actualizar las dependencias:

```bash
pip install --upgrade selenium pytest webdriver-manager
```

## 📊 Resultados y Reporting

Las pruebas generan:

1. **Salida de consola**: Información detallada de cada paso
2. **Capturas de pantalla**: Evidencia visual en formato PNG
3. **Reportes de pytest**: Resultados de ejecución y errores

## 🤝 Contribución

Para agregar nuevos casos de prueba:

1. Crear archivo `test_cp##.py` siguiendo la nomenclatura establecida
2. Implementar la función de prueba con el patrón existente
3. Incluir capturas de entrada y salida
4. Actualizar documentación si es necesario

---

**Nota**: Este proyecto forma parte del curso de Proceso de Software (PSoft) del séptimo semestre.
