# Artisan Market Back-End with Django

![logo](assets/logo.png)

**Artisan Market Back-End** es un proyecto desarrollado con Django Rest Framework, diseñado para impulsar una tienda en línea especializada en la venta de productos artesanales. Este repositorio alberga el código fuente del backend de la aplicación, proporcionando las capacidades esenciales para gestionar productos, usuarios, órdenes y más en la plataforma.

## Funcionalidades Clave

- **Gestión de Productos**: Administra una amplia variedad de productos artesanales, incluyendo detalles como nombre, descripción, precio y cantidad en stock.

- **Control de Usuarios**: Permite a los vendedores y administradores registrarse, autenticarse y gestionar sus cuentas.

- **Órdenes y Compras**: Facilita la creación, seguimiento y finalización de órdenes de compra, incluyendo estados como "pagado", "pendiente" y "cancelado".

- **Revisiones y Calificaciones**: Los clientes pueden dejar revisiones y calificaciones para los productos, proporcionando retroalimentación valiosa.

- **Estadísticas de Venta**: Ofrece estadísticas detalladas sobre las ventas, incluyendo el número de órdenes pagadas, pendientes, canceladas y más.

## Requisitos

Asegúrate de tener instaladas las siguientes herramientas y dependencias antes de empezar:

- [Django Rest Framework](https://www.django-rest-framework.org/) - Framework de Python utilizado para desarrollar la aplicación.

- [Pipenv](https://pypi.org/) - Gestor de dependencias para Python para instalar las bibliotecas requeridas.

- [Base de Datos](https://dev.mysql.com/downloads/mysql/) - Base de datos en MySQL trabajando con Django.

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

**Clona este repositorio:**

```bash
  git clone https://github.com/chicho69-cesar/artisan-market-django.git
  cd artisan-market-django
```

**Crea un archivo de configuración .env y configura la conexión a la base de datos. Puedes usar el archivo .env.example como plantilla:**

```bash
cp artisan_market/artisan_market/.env.example artisan_market/artisan_market/.env
```

**Inicia el entorno de ejecución de Python, para esto ubícate en la carpeta raíz del proyecto y ejecuta el siguiente comando en la terminal:**

```bash
.\venv\Scripts\activate
```

**Instala las dependencias del archivo requirements.txt en la carpeta raíz para el entorno de ejecución:**

```bash
pip install -r requirements.txt
```

**Entra a la carpeta base del proyecto desde la raíz:**

```bash
cd artisan_market
```

**Crea las migraciones si faltan por crear:**

```bash
py manage.py makemigrations
```

**Aplica las migraciones para crear las tablas de la base de datos:**

```bash
py manage.py migrate
```

**Inicia el servidor de desarrollo:**

```bash
py manage.py runserver
```

Accede a la aplicación en tu navegador visitando <http://localhost:8000>

**Inicia el servidor para acceder dentro de una LAN:**

```bash
py manage.py runserver 0.0.0.0:8000
```

Accede a la aplicación desde otro dispositivo conectado a la misma red visitando <http://IP:8000>

**¡Importante! Si al momento de ejecutar el servidor aparece un error aunque antes funcionaba correctamente es debido a que se necesita volver a instalar los paquetes en el entorno, por lo que se debe hacer lo siguiente:**

```bash
.\venv\Scripts\activate
pip install -r requirements.txt
```

**Si se instala un nuevo paquete en el proyecto es de mucha utilidad agregarlo como dependencia al archivo requirements.txt:**

```bash
pip freeze
pip freeze > requirements.txt
```
