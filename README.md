# Laboratorio 2 - DVWA

Repositorio de trabajo para el Laboratorio 2 de Criptografía y Seguridad en Redes.

## Descripción

En este laboratorio se analiza la vulnerabilidad de un formulario de autenticación en **DVWA (Damn Vulnerable Web Application)** mediante distintos enfoques de fuerza bruta. Se estudia tanto la obtención de credenciales como el tráfico generado por las herramientas utilizadas, junto con medidas de mitigación aplicables a sistemas reales.

## Herramientas utilizadas

- Docker
- DVWA
- Burp Suite
- cURL
- Hydra
- Wireshark
- Python 3
- librería `requests`

## Estructura del repositorio

```text
lab2-cripto/
├── codigo/
│   └── fuerza_bruta.py
├── notas/
│   ├── fiveusernames.txt
│   ├── millionpasswords.txt
│   └── archivos auxiliares
├── informe/
│   ├── Lab_de_Criptografia_n_2.tex
│   ├── Lab_de_Criptografia_n_2.pdf
│   └── img/
│       └── capturas usadas en el informe
├── .gitignore
└── README.md
